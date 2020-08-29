import httpx

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Api-Key": "1234ABCD",
}

with httpx.Client() as client:
    resp = client.get("http://localhost:4000/api-a/123", headers=headers)
    resp_json = resp.json()

# Check successful status code
assert resp.status_code == 200

# Print JSON response
print(resp_json)
