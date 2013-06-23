import boto.ec2

conn = boto.ec2.connect_to_region('us-east-1')


# Simplest example
# Creates an instance with all defaults - you will not be able to SSH into the server.
#conn.run_instances('<ami-image-id>')

# Let's not do that.  Let's be more specific.

# More complex
# Red Hat Enterprise Linux 6.4 (ami-7d0c6314)
new_reservation = conn.run_instances(
                        'ami-7d0c6314',
                        key_name='csg',
                        instance_type='t1.micro',
                        security_groups=['default'])

print 'New Instance: ', new_reservation

 
