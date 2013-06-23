import boto.ec2
conn = boto.ec2.connect_to_region('us-east-1')
conn.start_instances(instance_ids=['i-d8b25cbb'])
