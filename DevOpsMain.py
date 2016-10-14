from aws import Connection
from aws import EC2Instance
from aws import Volumes

connInstance = Connection()

conn = connInstance.ec2Connection()

print conn

"""
ec2 = EC2Instance()
ec2.list_instances(conn)
"""

vol = Volumes()
vol.list_volumes(conn)