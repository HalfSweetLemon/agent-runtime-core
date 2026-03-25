from app.schemas.agent import AgentRequest, AgentResponse, ToolCall, ToolResult
from app.tools.registry import registry

def detect_tool(text: str) -> tuple[str | None, dict]:
  if "时间" in text or "几点" in text:
    return "get_time", {}
  
  if "计算" in text:
    return "calculator", {
      "a": 12,
      "b": 3,
      "operator": "divide"
    }
    
  return None, {}

def run_agent(req: AgentRequest) -> AgentResponse:
  text = req.message
  tool_name, arguments = detect_tool(text)
  
  if tool_name:
    tool = registry.get(tool_name)
    
    if tool is None:
      return AgentResponse(
        reply=f"工具 {tool_name} 不存在",
        action="respond"
      )
    try:
      output = tool.run(arguments)
      tool_call = ToolCall(name=tool_name, arguments=arguments)
      tool_result = ToolResult(
        name=tool_name,
        success=True,
        output=output
      )
      
      return AgentResponse(
        reply=f"工具 {tool_name} 执行结果：{output}",
        action="tool_call",
        tool_call=tool_call,
        tool_result=tool_result,
      )
    except Exception as exc:
      tool_call = ToolCall(name=tool_name,arguments=arguments)
      tool_result = ToolResult(
        name=tool_name,
        success=False,
        output=str(exc)
      )
      return AgentResponse(
        reply=f"工具执行失败：{exc}",
        action="tool_call",
        tool_call=tool_call,
        tool_result=tool_result
      )
  return AgentResponse(
    reply=f"收到你的消息：{text}",
    action="respond"
  )
  
