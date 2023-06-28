import json
import time

def lambda_handler(event, context):
    try:
        # Call Dependency ....
        dependencyClient.uploadFile( ... )
    except:
        # Catch the exception and emit a metric
        cloudwatchClient.putMetric('Upload Error', 1)
        print('UploadError 1')
        print('UploadLatency 255')