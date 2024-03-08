# -*- coding: utf-8 -*-
import requests, re
from bs4 import BeautifulSoup
from base64 import b64encode
from ru_mvd_search_wanted.settings import HEADERS, BASE_URL, CAPTCHA_URL


class MVDParser:
    """
        A class for interacting with the MVD website\'s Wanted section.
        It manages the session and performs search queries.
    """

    def __init__(
        self,
        last_name: str,
        first_name: str,
        middle_name: str,
        year: str,
        month: str,
        day: str,
        mail: str,
        proxy: str = "",
    ) -> None:
        # Initializes with person\'s data and session details.
        self.proxy = (
            {"http": f"http://{proxy}", "https": f"https://{proxy}"} if proxy else {}
        )
        self.params = {
            "s_family": last_name.upper(),
            "fio": first_name.upper(),
            "s_patr": middle_name.upper(),
            "d_year": year,
            "d_month": month,
            "d_day": day,
            "email": mail,
            "captcha": "",
            "sec_csrftoken": "",
        }

    def __enter__(self):
        # Initializes the HTTP client session when entering the context.
        self.client = requests.Session()
        if self.proxy:
            self.client.proxies.update(self.proxy)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closes the HTTP client session upon exiting the context.
        self.client.close()

    @staticmethod
    def encode_to_base64(content) -> str:
        # Encodes content to base64.
        return b64encode(content).decode("ascii")

    def get_csrf_token(self, html_str) -> str:
        # Extracts CSRF token from HTML.
        match = re.search(
            r"<meta name=\'csrf-token-value\' content=\'(.*?)\'/>", html_str
        )
        return match.group(1) if match else ""

    def fetch_get_request(self, url: str, headers) -> requests.Response:
        # Fetches a GET request synchronously and returns the response. Logs error on failure.
        try:
            response = self.client.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise e
        return response

    def fetch_post_request(self, url: str, params, headers) -> requests.Response:
        # Fetches a POST request synchronously and returns the response. Logs error on failure.
        try:
            response = self.client.post(url, headers=headers, data=params)
            response.raise_for_status()
        except requests.RequestException as e:
            raise e
        return response

    def initialize(self) -> str:
        # Initializes by synchronously obtaining tokens and captcha.
        csrf_token = self.get_csrf_token(self.fetch_get_request(BASE_URL, HEADERS["h1"]).text)
        self.params["sec_csrftoken"] = csrf_token

        response = self.fetch_get_request(CAPTCHA_URL, HEADERS["h2"])
        captcha_base64 = self.encode_to_base64(response.content)

        return captcha_base64

    def get_result(self, captcha_word: str) -> dict:
        # Submits the query parameters to the website.
        self.params["captcha"] = captcha_word
        response = self.fetch_post_request(BASE_URL, self.params, HEADERS["h3"])

        # Handle various response cases
        if "Введен неверный код с изображения" in response.text:
            return {"error": "Incorrect captcha code entered"}

        if "По вашему запросу нет информации" in response.text:
            return {"result": None}

        if "можно отправить запрос не более 1 раза в 5 минут" in response.text:
            return {"error": "Requests can be made no more than once every 5 minutes"}

        html = BeautifulSoup(response.text, features="lxml")
        results = html.find("div", {"class": "bs-item clearfix"})
        image = results.find("img")["src"].strip() if results.find("img") else ""
        fio = results.find("div", {"class": "bs-item-title"}).text

        return {
            "result": {
                "image": image,
                "fio": fio.title(),
            }
        }
