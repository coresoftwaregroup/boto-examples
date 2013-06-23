import boto.ec2.elb
from boto.ec2.elb import HealthCheck

elb_conn = boto.ec2.elb.connect_to_region('us-east-1')

# ELB requires a few pieces to be setup
hc = HealthCheck(
        interval=20,
        healthy_threshold=3,
        unhealthy_threshold=5,
        target='TCP:22'
#       target='HTTP:8080/health'
    )

zones = ['us-east-1a', 'us-east-1b', 'us-east-1c', 'us-east-1d']
ports = [(80, 80, 'http')]
#ports = [(80, 8080, 'http'), (443, 8443, 'tcp')]

# Now create a new load balancer
lb = elb_conn.create_load_balancer('pywebdev-lb', zones, ports)
print 'New ELB: ', lb
print 'New ELB public DNS: ', lb.dns_name

# Add the health check configuration to the ELB.
lb.configure_health_check(hc)



