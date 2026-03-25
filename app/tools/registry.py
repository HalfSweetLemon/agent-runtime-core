from app.tools.get_time import GetTimeTool
from app.tools.calculator import CalculatorTool

class ToolRegistry:
  def __init__(self) -> None:
    self._tools = {}
    
  def register(self, tool) -> None:
    self._tools[tool.name] = tool
    
  def get(self, name:str):
    return self._tools.get(name)
  
registry = ToolRegistry()
registry.register(GetTimeTool())
registry.register(CalculatorTool())