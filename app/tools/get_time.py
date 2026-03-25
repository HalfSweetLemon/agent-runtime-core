from datetime import datetime

class GetTimeTool:
  name = "get_time"
  description = "Get the current system time"
  
  def run(self, arguments: dict) -> str:
    return datetime.now().strftime("%H:%M")