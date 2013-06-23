import boto.ec2

conn = boto.ec2.connect_to_region('us-east-1')

conn.detach_volume('vol-d57de68e')
