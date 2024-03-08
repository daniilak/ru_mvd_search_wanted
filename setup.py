import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ru_mvd_search_wanted",
    version="0.0.2",
    author="Daniil Agniashvili",
    author_email="dortos123456@gmail.com",
    description="Parser of information from the website of the Ministry of Internal Affairs Search",
    long_description_content_type="text/markdown",
    url="https://github.com/daniilak/ru_mvd_search_wanted",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    install_requires=['httpx','beautifulsoup4', 'pip_system_certs', 'fake-useragent'],
    python_requires='>3.7',
)
