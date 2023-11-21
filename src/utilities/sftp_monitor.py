import boto3
import json
import requests


def lambda_handler(event, context):
    print(f"Event called {event}")

    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    presigned_url = generate_presigned_url(s3_bucket, s3_key)

    api_url = "https://hooks.slack.com/services/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"
    response = call_api(api_url, presigned_url, s3_key)

    print("API Response:", response)
    return {'statusCode': 200, 'body': json.dumps('Presigned Url sent to Slack!')}


def generate_presigned_url(bucket, key):
    s3_client = boto3.client('s3')

    presigned_url = s3_client.generate_presigned_url(
        'get_object', Params={'Bucket': bucket, 'Key': key}, ExpiresIn=28800
    )

    return presigned_url


def call_api(api_url, presigned_url, key):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "pretext": "Presigned URL",
        "color": "#000D00",
        "fields": [
            {
                "title": f"Presigned URL {key}",
                "value": f"Presigned URL is {presigned_url}",
            }
        ],
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    return response.text
