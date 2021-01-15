from urllib.parse import urlparse

from requests import post


def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://da.gd/s/?url={big_url}").text


def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"
