from src.agentic_hindi.tools.eligibility import load_schemes, check_eligibility


def test_eligibility_basic():
    schemes = load_schemes()
    user = {'age': 32, 'annual_income': 25000, 'employment_status': 'unemployed'}
    matches = check_eligibility(user, schemes)
    assert any(m['id']=='scheme_nirdhan' for m in matches)
