from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_chat_returns_respond_action_for_plain_message() -> None:
    response = client.post(
        "/chat",
        json={
            "message": "你好",
            "session_id": "demo-001",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["action"] == "respond"
    assert body["reply"] == "收到你的消息：你好"
    assert body["tool_call"] is None
    assert body["tool_result"] is None


def test_chat_calls_get_time_tool() -> None:
    response = client.post(
        "/chat",
        json={
            "message": "现在几点",
            "session_id": "demo-002",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["action"] == "tool_call"
    assert body["tool_call"]["name"] == "get_time"


def test_chat_calls_calculator_tool_successfully() -> None:
    response = client.post(
        "/chat",
        json={
            "message": "计算 12 divide 3",
            "session_id": "demo-003",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["action"] == "tool_call"
    assert body["tool_call"]["name"] == "calculator"
    assert body["tool_result"]["success"] is True
