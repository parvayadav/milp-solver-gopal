"""
Optimization Data Structures and Default Problem Instances
go, pal! Team Capacity & Client Allocation Model
"""

import pandas as pd

CONSULTANTS = ["M", "A", "T", "AI"]

# Display names. Internal keys (M/A/T/AI) stay untouched — solver.py reads them directly.
CONSULTANT_NAMES = {
    "M": "Parva Yadav (M)",
    "A": "Abhimanyu Vyas (A)",
    "T": "Vinayak Vishvakarma (T)",
    "AI": "Puneet Agarwal (AI)"
}

CONSULTANT_TITLES = {
    "M": "CEO & Managing Director — Marketing Technology",
    "A": "Strategy & Performance Media — Advertising",
    "T": "Whole-time Director, Tech & Engineering — Technology",
    "AI": "Engagement Lead, Research & AI — Artificial Intelligence"
}

CAPACITIES_DEFAULT = {
    "M": 40.0,
    "A": 40.0,
    "T": 40.0,
    "AI": 40.0
}

CLIENT_PRIORITIES = {
    "KFC": "Strategic", "Disney": "Strategic", "HDFC": "Strategic", "IOB": "Standard",
    "Kotak": "Strategic", "FnP": "Standard", "Nykaa": "Important", "Masaba": "Important",
    "Wildcraft": "Important", "Woodland": "Important", "Axestrack": "Strategic",
    "Coca-Cola": "Strategic"
}

# Axestrack holds a hard exclusivity lock on Parva's (M's) full weekly capacity.
# Required_Hours == CAPACITIES_DEFAULT["M"] and M_Min == the same value forces
# x_{M,Axestrack} = Cap_M exactly, leaving zero M-hours for every other client.
CLIENT_REQUIREMENTS_DEFAULT = {
    "KFC":       {"Priority": "Strategic", "Required_Hours": 13, "M_Min": 0, "A_Min": 4, "T_Min": 3, "AI_Min": 0, "PM_Min": 6, "Locked_Consultant": ""},
    "Disney":    {"Priority": "Strategic", "Required_Hours": 14, "M_Min": 0, "A_Min": 0, "T_Min": 6, "AI_Min": 4, "PM_Min": 6, "Locked_Consultant": ""},
    "HDFC":      {"Priority": "Strategic", "Required_Hours": 13, "M_Min": 0, "A_Min": 5, "T_Min": 0, "AI_Min": 3, "PM_Min": 4, "Locked_Consultant": ""},
    "IOB":       {"Priority": "Standard",  "Required_Hours": 8,  "M_Min": 0, "A_Min": 3, "T_Min": 0, "AI_Min": 0, "PM_Min": 3, "Locked_Consultant": ""},
    "Kotak":     {"Priority": "Strategic", "Required_Hours": 13, "M_Min": 0, "A_Min": 0, "T_Min": 5, "AI_Min": 4, "PM_Min": 4, "Locked_Consultant": ""},
    "FnP":       {"Priority": "Standard",  "Required_Hours": 6,  "M_Min": 0, "A_Min": 3, "T_Min": 0, "AI_Min": 0, "PM_Min": 3, "Locked_Consultant": ""},
    "Nykaa":     {"Priority": "Important", "Required_Hours": 11, "M_Min": 0, "A_Min": 4, "T_Min": 0, "AI_Min": 3, "PM_Min": 4, "Locked_Consultant": ""},
    "Masaba":    {"Priority": "Important", "Required_Hours": 9,  "M_Min": 0, "A_Min": 4, "T_Min": 0, "AI_Min": 0, "PM_Min": 3, "Locked_Consultant": ""},
    "Wildcraft": {"Priority": "Important", "Required_Hours": 10, "M_Min": 0, "A_Min": 0, "T_Min": 3, "AI_Min": 0, "PM_Min": 3, "Locked_Consultant": ""},
    "Woodland":  {"Priority": "Important", "Required_Hours": 9,  "M_Min": 0, "A_Min": 0, "T_Min": 0, "AI_Min": 4, "PM_Min": 4, "Locked_Consultant": ""},
    "Axestrack": {"Priority": "Strategic", "Required_Hours": CAPACITIES_DEFAULT["M"], "M_Min": CAPACITIES_DEFAULT["M"], "A_Min": 0, "T_Min": 0, "AI_Min": 0, "PM_Min": 6, "Locked_Consultant": "M"},
    "Coca-Cola": {"Priority": "Strategic", "Required_Hours": 12, "M_Min": 0, "A_Min": 0, "T_Min": 5, "AI_Min": 4, "PM_Min": 6, "Locked_Consultant": ""},
}

BILLING_RATES_DEFAULT = {
    "KFC":       {"M": 5000, "A": 5800, "T": 6800, "AI": 8800},
    "Disney":    {"M": 5200, "A": 5900, "T": 7200, "AI": 9200},
    "HDFC":      {"M": 5100, "A": 5900, "T": 7000, "AI": 9000},
    "IOB":       {"M": 4700, "A": 5300, "T": 6100, "AI": 7700},
    "Kotak":     {"M": 5000, "A": 5800, "T": 7100, "AI": 9100},
    "FnP":       {"M": 4600, "A": 5200, "T": 6000, "AI": 7600},
    "Nykaa":     {"M": 4900, "A": 5600, "T": 6600, "AI": 8500},
    "Masaba":    {"M": 4900, "A": 5600, "T": 6500, "AI": 8400},
    "Wildcraft": {"M": 4800, "A": 5500, "T": 6500, "AI": 8300},
    "Woodland":  {"M": 4800, "A": 5500, "T": 6400, "AI": 8300},
    "Axestrack": {"M": 5300, "A": 5900, "T": 7000, "AI": 9000},
    "Coca-Cola": {"M": 5200, "A": 6000, "T": 7300, "AI": 9200},
}

DELIVERY_COSTS_DEFAULT = {
    "KFC":       {"M": 2000, "A": 2500, "T": 3100, "AI": 4300},
    "Disney":    {"M": 2100, "A": 2500, "T": 3300, "AI": 4600},
    "HDFC":      {"M": 2000, "A": 2500, "T": 3200, "AI": 4400},
    "IOB":       {"M": 1900, "A": 2300, "T": 2900, "AI": 3900},
    "Kotak":     {"M": 2000, "A": 2400, "T": 3200, "AI": 4500},
    "FnP":       {"M": 1900, "A": 2200, "T": 2800, "AI": 3800},
    "Nykaa":     {"M": 2000, "A": 2400, "T": 3000, "AI": 4200},
    "Masaba":    {"M": 2000, "A": 2400, "T": 3000, "AI": 4100},
    "Wildcraft": {"M": 1950, "A": 2350, "T": 2950, "AI": 4050},
    "Woodland":  {"M": 1950, "A": 2350, "T": 2900, "AI": 4050},
    "Axestrack": {"M": 2100, "A": 2400, "T": 3100, "AI": 4400},
    "Coca-Cola": {"M": 2100, "A": 2600, "T": 3300, "AI": 4600},
}

def get_default_client_df() -> pd.DataFrame:
    rows = []
    for cid, data in CLIENT_REQUIREMENTS_DEFAULT.items():
        rows.append({
            "Client": cid,
            "Priority": data["Priority"],
            "Required_Hours": data["Required_Hours"],
            "M_Min": data["M_Min"],
            "A_Min": data["A_Min"],
            "T_Min": data["T_Min"],
            "AI_Min": data["AI_Min"],
            "PM_Min": data["PM_Min"],
            "Locked_Consultant": data["Locked_Consultant"]
        })
    return pd.DataFrame(rows)

def get_default_billing_df() -> pd.DataFrame:
    rows = []
    for cid, rates in BILLING_RATES_DEFAULT.items():
        rows.append({
            "Client": cid,
            "M": rates["M"],
            "A": rates["A"],
            "T": rates["T"],
            "AI": rates["AI"]
        })
    return pd.DataFrame(rows)

def get_default_costs_df() -> pd.DataFrame:
    rows = []
    for cid, costs in DELIVERY_COSTS_DEFAULT.items():
        rows.append({
            "Client": cid,
            "M": costs["M"],
            "A": costs["A"],
            "T": costs["T"],
            "AI": costs["AI"]
        })
    return pd.DataFrame(rows)

def get_default_capacities_df() -> pd.DataFrame:
    rows = []
    for cid, cap in CAPACITIES_DEFAULT.items():
        rows.append({
            "Consultant": cid,
            "Role": CONSULTANT_NAMES[cid],
            "Capacity_Hours": cap
        })
    return pd.DataFrame(rows)
