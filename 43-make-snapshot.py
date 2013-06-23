import boto.ec2

conn = boto.ec2.connect_to_region('us-east-1')

# Creating snapshots of your volumes is crazy easy
snapshot = conn.create_snapshot('vol-a468e1ff', 'pywebdev - a sample description')
print 'Snapshot Id: ', snapshot
