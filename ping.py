import time
import requests

endpoint = 'https://peso-backend.onrender.com/general/all-info'

def ping_endpoint():
    while True:
        try:
            response = requests.get(endpoint)
            print(f"Pinged {endpoint} - Status Code: {response.status_code}")
            
            # Check if response is successful (status code 200)
            if response.status_code == 200:
                # Log the response payload
                print(f"Response Payload: {response.json()}")  # Assuming JSON response
        except Exception as e:
            print(f"Failed to ping {endpoint}: {e}")
        time.sleep(50)

if __name__ == "__main__":
    ping_endpoint()