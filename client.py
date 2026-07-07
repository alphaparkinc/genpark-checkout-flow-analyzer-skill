"""
checkout-flow-analyzer-skill: Client SDK
Analyzes e-commerce checkout funnel drops and outputs targeted UX recommendations.
"""
from __future__ import annotations
from typing import Optional


class CheckoutFlowAnalyzerClient:
    """
    SDK for analyzing checkout funnel statistics.
    """

    def analyze_funnel(self, funnel_steps: dict) -> dict:
        cart = float(funnel_steps.get("cart_views", 1))
        contact = float(funnel_steps.get("contact_info", 0))
        shipping = float(funnel_steps.get("shipping_method", 0))
        payment = float(funnel_steps.get("payment_method", 0))
        purchase = float(funnel_steps.get("purchase", 0))

        # Funnel stage conversion rates (relative to previous stage)
        r_contact = round((contact / max(1.0, cart)) * 100, 1)
        r_shipping = round((shipping / max(1.0, contact)) * 100, 1)
        r_payment = round((payment / max(1.0, shipping)) * 100, 1)
        r_purchase = round((purchase / max(1.0, payment)) * 100, 1)

        overall = round((purchase / max(1.0, cart)) * 100, 1)

        # Drop-off rates
        drops = {
            "contact_info": 100 - r_contact,
            "shipping_method": 100 - r_shipping,
            "payment_method": 100 - r_payment,
            "purchase": 100 - r_purchase
        }

        bottleneck = max(drops, key=drops.get)
        
        recs = []
        if bottleneck == "contact_info":
            recs.append("Enable express checkout buttons (Shop Pay, Apple Pay) to bypass forms.")
            recs.append("Reduce required checkout fields to the absolute minimum.")
        elif bottleneck == "shipping_method":
            recs.append("Offer a clear free shipping threshold or flatter rates.")
            recs.append("Provide estimated delivery dates instead of generic transit times.")
        elif bottleneck == "payment_method":
            recs.append("Support popular local payment options (e.g. Klarna, PayPal, Venmo).")
            recs.append("Display security and SSL trust badges prominently on the billing step.")
        else:
            recs.append("Implement one-click purchase capabilities.")
            recs.append("Optimise page load speeds and error-checking validation times.")

        return {
            "stage_conversion_rates": {
                "cart_to_contact_pct": r_contact,
                "contact_to_shipping_pct": r_shipping,
                "shipping_to_payment_pct": r_payment,
                "payment_to_purchase_pct": r_purchase
            },
            "overall_conversion_rate": overall,
            "bottleneck_stage": bottleneck,
            "highest_dropoff_pct": round(drops[bottleneck], 1),
            "recommendations": recs
        }
