import boto.ec2.autoscale
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup

autoscale_conn = boto.ec2.autoscale.connect_to_region('us-east-1')

# Get all autoscale groups
ag = autoscale_conn.get_all_groups()
print 'My Autoscale Groups: ', ag

for group in ag:
    print "Auto Scale Group, name: ", group.name
    print "Auto Scale Group, launch configuration: ", group.launch_config_name
    print "Auto Scale Group, load balancers: ", group.load_balancers
    print '-----------------------------------'

