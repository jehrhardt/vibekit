from fastapi import FastAPI
from fastapi.testclient import TestClient

import vibekit


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(vibekit.router)
    return app


def test_info_returns_ok_status() -> None:
    client = TestClient(create_app())

    response = client.get("/vibekit/info")

    assert response.status_code == 200
    assert response.json() == {"status": "✅"}
