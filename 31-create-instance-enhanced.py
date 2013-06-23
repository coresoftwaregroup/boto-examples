import boto.ec2
import time

conn = boto.ec2.connect_to_region('us-east-1')

# Enhanced creation with Name tag and loop until it is running.

# Red Hat Enterprise Linux 6.4 (ami-7d0c6314)
new_reservation = conn.run_instances(
                        'ami-7d0c6314',
                        key_name='csg',
                        instance_type='t1.micro',
                        security_groups=['default'])
print "New instance created."

# Add a Name to the instance, then loop to wait for it to be running.
instance = new_reservation.instances[0]
conn.create_tags([instance.id], {"Name":"PyWebDev Example 3a"})
while instance.state == u'pending':
    print "Instance state: %s" % instance.state
    time.sleep(10)
    instance.update()

print "Instance state: %s" % instance.state
print "Public dns: %s" % instance.public_dns_name
 
