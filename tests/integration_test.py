
import requests
import time
import sys

# Simple script to check if the app is up and connected to DB
url = "http://localhost:5000/"

print(f"Testing connectivity to {url}...")
try:
    response = requests.get(url)
    if response.status_code == 200 and "DB Connected!" in response.text:
        print("✅ Integration Test Passed!")
        sys.exit(0)
    else:
        print(f"❌ Test Failed: Status {response.status_code}, Body: {response.text}")
        sys.exit(1)
except Exception as e:
    print(f"❌ Connection Error: {e}")
    sys.exit(1)
