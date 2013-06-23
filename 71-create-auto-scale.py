import boto.ec2.autoscale
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup

autoscale_conn = boto.ec2.autoscale.connect_to_region('us-east-1')

# 3 Core Concepts
#
# 1. Launch Configuration
# 2. Autoscale Group
# 3. Triggers

# First setup a Launch Configuration
lc = LaunchConfiguration(name='pywebdev_launch_config', image_id='ami-7bf28712',
                             instance_type='t1.micro', # defaults to m1.small
                             key_name='csg',
                             security_groups=['default'])
result = autoscale_conn.create_launch_configuration(lc)
print 'Launch Configuration Creation Result: ', result


# Now we have a Launch Configuration and an ELB.  Create and launch the AutoScalingGroup
ag = AutoScalingGroup(group_name='pywebdev_as_group', load_balancers=['pywebdev-lb'],
                          availability_zones=['us-east-1a', 'us-east-1b', 'us-east-1c', 'us-east-1d'],
                          launch_config=lc, min_size=2, max_size=4,
                          connection=autoscale_conn)
result = autoscale_conn.create_auto_scaling_group(ag)
print 'Auto Scaling Group Creation Result: ', result



