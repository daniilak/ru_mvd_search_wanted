"""
    settings
"""
from fake_useragent import UserAgent

TIMEOUT_SEC = 30
BASE_URL = "https://xn--b1aew.xn--p1ai/wanted"
CAPTCHA_URL = "https://xn--b1aew.xn--p1ai/captcha"

ua = UserAgent()

user_agent = ua.random
HEADERS = {
    "h1": {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
    },
    "h2": {
        "User-Agent": user_agent,
        "Accept": "image/avif,image/webp,*/*",
        "Accept-Language": "ru-RU",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://xn--b1aew.xn--p1ai/wanted",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    },
    "h3": {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://xn--b1aew.xn--p1ai/wanted",
        "Origin": "https://xn--b1aew.xn--p1ai",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "TE": "trailers",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    },
}
