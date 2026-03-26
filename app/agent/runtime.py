from app.schemas.agent import AgentRequest, AgentResponse, ToolCall, ToolResult
from app.tools.registry import registry


def detect_tool_name(text: str) -> str | None:
  if "时间" in text or "几点" in text:
    return "get_time"
  
  if "计算" in text:
    return "calculator"
  return None

def detect_tool_arguments(tool_name: str, text: str) -> tuple[dict, str | None]:
  if tool_name == "get_time":
    return {}, None
  if tool_name == "calculator":
    try:
      return parse_calculator_arguments(text), None
    except ValueError:
      return {}, "计算参数格式无效，需要提供两个数字和一个运算符(add/subtract/multiply/divide)"
  return {}, None

def parse_calculator_arguments(text: str) -> dict:
  parts = text.split()
  numbers = []
  operator = None
  
  for part in parts:
    if part.replace(".", "", 1).isdigit():
      numbers.append(float(part))
    if part in {"add", "subtract", "multiply", "divide"}:
      operator = part
  
  if len(numbers) < 2 or operator is None:
    raise ValueError("Invalid calculator input")

  return {
    "a": numbers[0],
    "b": numbers[1],
    "operator": operator,
  }

def run_agent(req: AgentRequest) -> AgentResponse:
  text = req.message
  tool_name = detect_tool_name(text)
  
  
  if tool_name is None:
    return AgentResponse(
      reply=f"收到你的消息：{text}",
      action="respond",
    )
    
  arguments, error = detect_tool_arguments(tool_name, text)
  if error is not None:
    tool_call = ToolCall(name=tool_name, arguments={})
    tool_result = ToolResult(
      name=tool_name,
      success=False,
      output=error
    )
    return AgentResponse(
      reply=f"工具执行失败：{error}",
      action="tool_call",
      tool_call=tool_call,
      tool_result=tool_result,
    )
  return execute_tool_and_build_response(tool_name, arguments)
  

def execute_tool_and_build_response(tool_name: str, arguments: dict) -> AgentResponse:
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
