"""
example_usage.py -- Demonstrates CheckoutFlowAnalyzerClient
"""
from client import CheckoutFlowAnalyzerClient

def main():
    client = CheckoutFlowAnalyzerClient()
    result = client.analyze_funnel({
        "cart_views": 5000,
        "contact_info": 3200,
        "shipping_method": 1500,
        "payment_method": 1400,
        "purchase": 1100
    })
    print("[Funnel Analysis Result]")
    print(f"Overall CR: {result['overall_conversion_rate']}%")
    print(f"Bottleneck: {result['bottleneck_stage']} (Dropoff: {result['highest_dropoff_pct']}%)")
    print(f"Recs: {result['recommendations']}")

if __name__ == "__main__":
    main()
