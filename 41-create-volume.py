import boto.ec2

conn = boto.ec2.connect_to_region('us-east-1')

# Create a volume
# create_volume(size, zone, snapshot=None, volume_type=None, iops=None)
vol = conn.create_volume(50, "us-east-1d")
print 'Volume Id: ', vol.id

# Add a Name tag to the new volume so we can find it.
conn.create_tags([vol.id], {"Name":"PyWebDev Example 3"})

#You can check that the volume is now ready and available:
curr_vol = conn.get_all_volumes([vol.id])[0]
print 'Current Volume Status: ', curr_vol.status
print 'Current Volume Zone: ', curr_vol.zone
print 'Current Volume Device: ', curr_vol.attach_data.device

# Since that is pretty boring, let's attach it to a real instance
instance_id = 'i-d8b25cbb'
result = conn.attach_volume (vol.id, instance_id, "/dev/sdy")
print 'Attach Volume Result: ', result

# NOTE:
# <Response><Errors><Error><Code>InvalidParameterValue</Code><Message>Value (/dev/sdZZ) for parameter device is invalid. /dev/sdZZ is not a valid EBS device name.</Message></Error></Errors><RequestID>a9c4a3c3-b7fc-4344-94a9-0d412f1981e2</RequestID></Response>

# RHEL requires some extra work...
# To start, on RHEL, Amazon uses your device above, 'sdx', in the console, but at the hardware level creates a device named something like: /dev/xvdad

# Then you have to format and mount it.
#  mkfs.ext3 /dev/xvdad
#  echo "/dev/xvdad /mnt/sillyname ext3 noatime 0 0" >> /etc/fstab
