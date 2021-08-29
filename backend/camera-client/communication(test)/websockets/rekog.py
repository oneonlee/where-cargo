import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# client = boto3.client('rekognition')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    

# response = client.detect_labels(
#     Image={
#         'S3Object': {
#             'Bucket': 'mybucket',
#             'Name': 'myphoto',
#         },
#     },
#     MaxLabels=123,
#     MinConfidence=70,
# )

# print(response)
