from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_chat_returns_mock_reply() -> None:
    response = client.post(
        "/chat",
        json={
            "message": "你好",
            "session_id": "demo-001",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "reply": "收到你的消息：你好",
        "session_id": "demo-001",
        "status": "ok",
    }
