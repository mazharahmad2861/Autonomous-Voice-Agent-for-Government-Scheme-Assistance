import json
from typing import Dict, List

# Very simple rule-based eligibility engine using JSON schemes.

SCHEMES_PATH = "data/schemes.json"


def load_schemes(path: str = SCHEMES_PATH) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_eligibility(user_info: Dict, schemes: List[Dict]) -> List[Dict]:
    matches = []
    age = user_info.get("age")
    income = user_info.get("annual_income")
    employment = user_info.get("employment_status")

    for s in schemes:
        ok = True
        crit = s.get("eligibility", {})
        min_age = crit.get("min_age")
        max_income = crit.get("max_income")
        require_unemployed = crit.get("require_unemployed")

        if min_age and (age is None or age < min_age):
            ok = False
        if max_income and (income is None or income > max_income):
            ok = False
        if require_unemployed and employment != "unemployed":
            ok = False
        if ok:
            matches.append(s)
    return matches
