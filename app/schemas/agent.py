from pydantic import BaseModel, Field
from typing import Literal

class Message(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]
    content: str
    
class AgentRequest(BaseModel):
    message: str
    session_id: str | None = None
    history: list[Message] = Field(default_factory=list)
    
class ToolCall(BaseModel):
    name: str
    arguments: dict = Field(default_factory=dict)
class ToolResult(BaseModel):
    name: str
    success: bool
    output: str
    
class AgentResponse(BaseModel):
    reply: str
    action: Literal["respond", "tool_call"]
    tool_call: ToolCall | None = None
    tool_result: ToolResult | None = None