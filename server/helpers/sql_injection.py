import requests

def test_sql_injection(url, payload):
    response = requests.post(url, data=payload)

    if "error" in response.text.lower() or "exception" in response.text.lower():
        print("Possible SQL injection vulnerability detected.")
    else:
        print("No SQL injection vulnerability detected.")

form_url = "http://localhost:5000/api/add-user"


sql_injection_payload = {
    "email": "'; DROP TABLE users; --",
    "name": "John Doe",
    "city": "New York"
}

test_sql_injection(form_url, sql_injection_payload)
