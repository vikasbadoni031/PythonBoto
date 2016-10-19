import boto.ec2

class Connection:
	def __init__(self):
		print "Inside the connection constructor"
		self.region = 'ap-southeast-2'

	def ec2Connection(self):
		print "Getting the ec2 connection"
		conn = boto.ec2.connect_to_region(self.region)
		return conn

	def s3Connection(self):
		print "Getting the s3 connection"
		conn = boto.connect_s3()
		return conn

	