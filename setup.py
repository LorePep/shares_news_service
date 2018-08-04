import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shares_news_service",
    version="1.0",
    author="Lorenzo Peppoloni",
    author_email="l.peppoloni@gmail.com",
    description="A small to scrape potential interesting shares news and post them on telegram.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LorePep/shares_news_service",
    packages=setuptools.find_packages(),
    install_requires=[
        "mock",
        "requests",
        "BeautifulSoup4",
    ],
    entry_points={
        "console_scripts": [
            "shares_news_service = shares_news_service.main:main",
        ]
    },
)