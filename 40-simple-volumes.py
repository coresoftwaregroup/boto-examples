import boto.ec2

conn = boto.ec2.connect_to_region('us-east-1')

# Let's just list the volumes

volumes = conn.get_all_volumes()
for v in volumes:
    print 'Volume Attach Data: ', v.attach_data.id
    print 'Volume Attach Data: ', v.attach_data.instance_id
    print 'Volume Attach Data: ', v.attach_data.attach_time
    print 'Volume Attach Data: ', v.attach_data.device
    print 'Volume Status: ', v.status
    print 'Volume Zone: ', v.zone
    print '----------------------'

