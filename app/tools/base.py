from typing import Any, Protocol

class Tool(Protocol):
  name: str
  description: str
  
  def run(self, arguments: dict[str, Any]) -> str:
    return ''