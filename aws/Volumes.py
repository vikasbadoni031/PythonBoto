import boto.ec2

class Volumes:
	def __init__(self):
		print "Inside volume construtor"

	def list_volumes(self,conn):
		print "Inside list volume function"
		vols = conn.get_all_volumes()

		if vols:
			for v in vols:
				print "volume id:", v.id
				print "Volume status", v.status
				print "Volume size", v.size
				print "volume zone", v.zone

				attachementData= v.attach_data
				print "Instance Id :", attachementData.instance_id
				print "attachment time :", attachementData.attach_time
				print "attachment device :", attachementData.device
