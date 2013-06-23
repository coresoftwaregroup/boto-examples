import boto.sns

sns_conn = boto.sns.connect_to_region('us-east-1')

# Name of a SNS topic
arn = 'arn:aws:sns:us-east-1:988683046438:pywebdevdemo'

message = 'My pyweb SNS'
result = sns_conn.publish(arn,message,'Finished AWS snapshotting')

print 'Result: ', result


