# Dead Stock Detector Non-LLM Tool 

## Purpose
In supply chain management, dead stock refers to inventory that remains unsold — often sitting in warehouses for a long amount of time. This ends up costing more to store it than what the product would generate in revenue. This tool allows users to compute total financial holding cost of slow-moving products and classifies its severity risk of becoming a dead stock. This gives users a clear, deterministic answer which products are a liability and gives an idea of what to do next with that product.
**Installation/Setup**
This tool simply just requires the `enum` built-in Python module, so no further installations are needed. 
To begin using this tool download the `tool.py` file, and place it into your project directory. 

You can simply run the file by using:
```bash
python tool.py
```
Or you can incorporate it into a LLM project by including 
```python
from tool import detect_dead_stock
```
**Usage Example**
An example of when this tool can be helpful is with this following code snippet
```python
from tool import detect_dead_stock

result = detect_dead_stock(
    units_on_hand= 100,
    daily_demand= 5,
    holding_cost_per_day= 2.0,
    cost_per_unit= 10.0
)
print(result)
```

Output:
```bash
{
    "result": 4000.0,
    "unit": "USD ($)",
    "days_of_stock_remaining": 20.0,
    "severity": <Severity.HEALTHY: "healthy">,
    "detail": "100 units on hand with 5 units/day demand represents 20.0 days of stock, classified as 'healthy', costing $4,000.00 in holding costs."
}
```

## How This is Helpful in a SNAP Project
In a SNAP project, this tool will be registered by LangChain via `LangChain.tools` as using the `@tool` decorator, allowing the agent to invoke it automatically when a user asks about inventory-related questions regarding inventory health or holding costs. The agent will parse the returned dictionary and respond with a more human-readable analysis back to the user without the user having to do any manual intervention.