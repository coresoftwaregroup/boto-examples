import boto.ec2.autoscale
import time

autoscale_conn = boto.ec2.autoscale.connect_to_region('us-east-1')


ag = autoscale_conn.get_all_groups(names=['pywebdev_as_group'])[0]
print "PyWebDev AS Group: ", ag

# Once the instances have been shutdown, you can delete the autoscale group:
ag.shutdown_instances()
time.sleep(60)
ag.delete()
time.sleep(20)

# Now get the Launch Configuration
lc = autoscale_conn.get_all_launch_configurations(names=['pywebdev_launch_config'])[0]
print "PyWebDev LC: ", lc

lc.delete()


