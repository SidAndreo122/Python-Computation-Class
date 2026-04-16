# tool.py
# -------------------------------------------------------
# Tool Name : Dead Stock Detector
# Domain : Supply Chain/Inventory
# Author : Sidney Andreano
# Description: <one sentence on what this computes
# and why it matters in the domain>
# Usage : See README.md for a sample call.
# -------------------------------------------------------
from enum import Enum

from enum import Enum
class Severity(Enum):
    HEALTHY = "healthy"
    SLOW = "slow-moving"
    RISK = "at risk"
    DEAD = "dead stock"

def get_severity(days):
    if days <= 30:
        return Severity.HEALTHY
    if days > 30 and days <= 90:
        return Severity.SLOW
    if days > 90 and days <= 180:
        return Severity.RISK
    return Severity.DEAD

def detect_dead_stock(units_on_hand: float, daily_demand: float, holding_cost_per_day: float, cost_per_unit: float) -> dict:
    """
        One-sentence summary.
        Args:
            param1 (type): description.
            param2 (type): description.
        Returns:
            dict: {
                "result": <primary computed value>,
                "unit": <string label, e.g. "USD" or "liters">,
                "detail": <optional breakdown or explanation string>
            }
        Raises:
            ValueError: if any input is out of expected range or type.
    # --- Input Validation ---
        units_on_hand:
            This parameter is invalid if the value is negative.
        daily_demand:
            This parameter is invalid if the value is negative and the special case when demand
            is zero, meaning days_of_stock cannot be computed (days/0).
        holding_cost_per_day:
            This parameter is invalid if the value is negative and taking the assumption that
            the cost cannot be zero.
        cost_per_unit:
            This parameter is invalid if the value is negative and the product cannot be sold for free.
        
    # --- Core Logic ---
    """

    # Input Validation
    if units_on_hand < 0:
        raise ValueError(f"units_on_hand must be positive, got {units_on_hand}.")
    if daily_demand < 0:
        raise ValueError(f"daily_demand must be positive, got {daily_demand}.")
    if daily_demand == 0:
        demand_warning = input("WARNING: You have set daily_demand as 0, which will automatically cause a dead stock. Do you want to continue (Y/N)? ").upper()
        if input == 'Y':
            days_of_stock = float('inf')
            get_severity(days_of_stock)
        else:
            raise ValueError(f"You have chosen not to continue, calculation canceled.")
    if holding_cost_per_day <= 0:
        raise ValueError(f"holding_cost_per_day must be positive and must not be 0, got {holding_cost_per_day}.")
    if cost_per_unit <= 0:
        raise ValueError(f"cost_per_unit must be positive and must not be zero, got {cost_per_unit}.")

    days_of_stock = units_on_hand / daily_demand # days of stock remaining based on demand
    total_holding_cost = units_on_hand * holding_cost_per_day * days_of_stock # financial loss 
    severity = get_severity(days_of_stock) # severity label for levels of risk (risk of dead stock)
    return {
        "result": total_holding_cost,
        "unit": "USD ($)", 
        "days_of_stock_remaining": days_of_stock,
        "severity": severity,
        "detail": f"{units_on_hand} units on hand with {daily_demand} units/day demand represents {days_of_stock:.1f} days of stock, classified as '{severity.value}', costing ${total_holding_cost:,.2f} in holding costs."
        }