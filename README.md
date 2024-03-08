
# API MVD Search Wanted Client

> Поиск указанного человека в базе данных [Розыск МВД](https://xn--b1aew.xn--p1ai/wanted)

[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]


Requirements:

-   Python 3.7+
-   [httpx](https://pypi.org/project/httpx/)
-   [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
-   [fake-useragent](https://pypi.org/project/fake-useragent/)

## Installation

```sh
pip install ru_mvd_search_wanted
```


## Usage

Import client:

```python
from ru_mvd_search_wanted.sync import MVDParser
```

Set proxy:

```python
proxy = "user:pass@host:port"
```

Use `with MVDParser()` if you want a context-managed client:

```python


with MVDParser(
    "Фамилия", "Имя", "Отчество", "YYYY", "MM", "DD", "123455@gmail.com", proxy
) as mvd:
    captcha_base64 = mvd.initialize()

    # solve captcha
    # captcha_word = solve(captcha_base64)
    result = mvd.get_result(captcha_word)

if "error" in result:
    print(result["error"])
else:
    print(result["result"])

```

## Usage  (async)

Import client:

```python
from ru_mvd_search_wanted.asynchr import MVDParserAsync
```

Set proxy:

```python
proxy = "user:pass@host:port"
```

Use `async with MVDParserAsync()` Example:

```python

import asyncio

proxy = "user:pass@host:port"

async def main():
    async with MVDParserAsync(
        "Фамилия",
        "Имя",
        "Отчество",
        "YYYY",
        "MM",
        "DD",
        "123456@gmail.com",
        proxy
    ) as mvd:
        captcha_base64 = await mvd.initialize()

        # solve captcha
        # captcha_word = await solve(captcha_base64)
        result = await mvd.get_result(captcha_word)

    if "error" in result:
        print(result["error"])
    else:
        print(result["result"])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
