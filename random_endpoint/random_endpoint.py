import requests
import random
import time

endpoint = "http://prometheus:5001"  # Replace with your actual endpoint

random_times = random.randint(1, 10)
while True:
    for i in range(random_times):
        try:
            # Perform a GET request to the endpoint
            response = requests.get(endpoint)
            print("Response:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", e)
    
    # Wait for a random interval between 1 and 5 seconds
    wait_time = random.uniform(10, 30)
    time.sleep(wait_time)
    random_times = random.randint(1, 10)

