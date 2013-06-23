import boto.ec2

# Uses keys from .boto file
conn = boto.ec2.connect_to_region('us-east-1')

# Alternatively,
#conn = boto.ec2.connect_to_region("us-west-2",
#           aws_access_key_id='<aws access key>',
#           aws_secret_access_key='<aws secret key>')

# A reservation corresponds to a command to start instances. You can see what instances are associated with a reservation:
reservations = conn.get_all_instances()

# Can filter
filters = {'instance-state-name' : 'running'} 
filters = {'tag:Name': 'PyWebDev Example 3'}
reservations = conn.get_all_instances(filters=filters)

# An instance object allows you get more meta-data available about the instance:
for r in reservations:
    print 'r: ', r

instances = reservations[0].instances
print 'instances: ', instances

inst = instances[0]
print inst.instance_type
print inst.placement
print inst.state
print inst.public_dns_name
print dir(inst)


# We can then do a few things on an instance:
#conn.stop_instances(instance_ids=['instance-id-1','instance-id-2', ...])

# And we can terminate!!!!  Danger!
