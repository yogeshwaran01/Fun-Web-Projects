from .fixtures import simple_client
from .fixtures import captured_templates
from app.utils.flames import flames_for


def test_flames(simple_client):
    with captured_templates() as templates:
        simple_client.post("/fun/flames", data=dict(p1="python", p2="java"))
        _, context = templates[0]
        assert context["signal"] == flames_for("python", "java")["result"][0]
