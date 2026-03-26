class CalculatorTool:
  name = "calculator"
  description = "Perform basic arithmetic operations"
  
  def run(self, arguments: dict) -> str:
    a = arguments["a"]
    b = arguments["b"]
    operator = arguments["operator"]

    if operator == "add":
      return str(a + b)
    if operator == "subtract":
      return str(a - b)
    if operator == "multiply":
      return str(a * b)
    if operator == "divide":
      if b == 0:
        raise ValueError("Cannot divide by zero")
      return str(a / b)

    raise ValueError(f"Unsupported operator: {operator}")