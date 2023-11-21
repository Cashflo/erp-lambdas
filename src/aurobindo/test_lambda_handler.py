from aurobindo_file_filter import lambda_handler

# Test case for valid input
def test_valid_input():
    event = {
        "Records": [
            {
                "eventVersion": "2.0",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "1970-01-01T00:00:00.000Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {
                    "principalId": "EXAMPLE"
                },
                "requestParameters": {
                    "sourceIPAddress": "127.0.0.1"
                },
                "responseElements": {
                    "x-amz-request-id": "EXAMPLE123456789",
                    "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "testConfigRule",
                    "bucket": {
                    "name": "cf-dev-temp-bukkit",
                    "ownerIdentity": {
                        "principalId": "EXAMPLE"
                    },
                    "arn": "arn:aws:s3:::example-bucket"
                    },
                    "object": {
                    "key": "TempFileDumpErp/prod_2xlfbrab_guwahati_vm_001_20230113134055_srv01.csv",
                    "size": 1024,
                    "eTag": "0123456789abcdef0123456789abcdef",
                    "sequencer": "0A1B2C3D4E5F678901"
                    }
                }
            }
        ]
    }
    context = None
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert response['body'] == 'Files moved successfully!'