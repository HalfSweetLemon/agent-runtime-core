from app.schemas.agent import AgentRequest, AgentResponse, ToolCall, ToolResult

def run_agent(req: AgentRequest) -> AgentResponse:
  text = req.message
  
  if "时间" in text or "几点" in text:
    tool_call = ToolCall(name="get_time", arguments={})
    tool_result = ToolResult(
      name="get_time",
      success=True,
      output="10:30"
    )
    
    return AgentResponse(
      reply=f"现在时间是 {tool_result.output}",
      action="tool_call",
      tool_call=tool_call,
      tool_result=tool_result
    )
    
  return AgentResponse(
    reply=f"收到你的消息：{text}",
    action="respond"
  )