import boto.ec2.elb

# Uses keys from .boto file
conn = boto.ec2.elb.connect_to_region('us-east-1')

# Get all ELB's
# You can also filter:
#    conn.get_all_load_balancers(load_balancer_names=['load-balancer-prod'])
all_elb = conn.get_all_load_balancers()
print 'My ELBs: ', all_elb








