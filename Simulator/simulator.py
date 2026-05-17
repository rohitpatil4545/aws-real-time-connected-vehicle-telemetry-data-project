import json
import random
import boto3
import time
from datetime import datetime

# Create Kinesis client
kinesis_client = boto3.client(
    'kinesis',
    region_name='us-east-1'   # Change your region
)

# Number of vehicles
NUM_VEHICLES = 100

def generate_vehicle_data(vehicle_id):
    data = {
        "vehicle_id": f"V{vehicle_id}",
        "speed": random.randint(40, 140),
        "engine_temp": random.randint(70, 130),
        "fuel_level": random.randint(10, 100),
        "timestamp": datetime.utcnow().isoformat()
    }
    return data

while True:
    for vehicle_id in range(1, NUM_VEHICLES + 1):

        vehicle_data = generate_vehicle_data(vehicle_id)

        # Convert to JSON
        json_data = json.dumps(vehicle_data)

        # Print output
        print(json_data)

        # Send to Kinesis
        response = kinesis_client.put_record(
            StreamName='vehicle-streamdata',
            Data=json_data,
            PartitionKey=str(vehicle_id) 
        )
        # print("Data sent to Kinesis successfully")

    # Wait 1 second
    time.sleep(1)