# checkout-flow-analyzer-skill

> **GenPark AI Agent Skill** -- Checkout funnel metrics and UX analyzer.

## Quick Start

```python
from client import CheckoutFlowAnalyzerClient
client = CheckoutFlowAnalyzerClient()
res = client.analyze_funnel({"cart_views": 100, "purchase": 5})
print(res["overall_conversion_rate"])
```
