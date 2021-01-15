import requests

from .fixtures import simple_client
from .fixtures import captured_templates

from app.utils.mask_url import MaskUrl
from app.utils.mask_url import Shortner


def test_url_mask(simple_client):
    with captured_templates() as templates:
        simple_client.post(
            "/tools/maskurl",
            data=dict(turl="https://python.org", hurl="https://google.com", kw="more"),
        )
        _, context = templates[0]
        assert context["url"] == MaskUrl(
            "https://python.org", "https://google.com", "more"
        )

        assert requests.get(context["url"].strip(), allow_redirects=True).ok is True


def test_url_mask(simple_client):
    with captured_templates() as templates:
        simple_client.post("/tools/shorturl", data=dict(url="https://python.org"))
        _, context = templates[0]
        assert context["url"] == Shortner("https://python.org")

        assert requests.get(context["url"].strip(), allow_redirects=True).ok is True
