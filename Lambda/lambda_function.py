import json
import base64
import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'vehicle-telemetry-dataproject'         

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('vehicle_live_status')   

def lambda_handler(event, context):

    for record in event['Records']:

        payload = base64.b64decode(
            record['kinesis']['data']
        ).decode('utf-8')

        data = json.loads(payload)

        print("Vehicle Data:", data)

        # Anomaly Detection
        if data['engine_temp'] > 120:
            print(f"ALERT: High engine temp for {data['vehicle_id']}")  

        table.put_item(
            Item={
                'vehicle_id': data['vehicle_id'],
                'speed': data['speed'],
                'engine_temp': data['engine_temp'],
                'fuel_level': data['fuel_level'], 
                'timestamp': data['timestamp']
            }
        )    

        # Generate filename
        file_name = f"telemetry/{datetime.utcnow().isoformat()}.json"

        # Store into S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data)
        )

    return {
        'statusCode': 200,
        'body': 'Data stored in S3 successfully'
    }