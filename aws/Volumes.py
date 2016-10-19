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
				print "\n Next volume \n"

	def attach_volume(self,conn,volume_id,instance_id):
		print "atttaching volume function"

		vols=conn.get_all_volumes(volume_id)

		print "printing volume info",vols

		if vols:

			volume=vols[0]

			if(volume.status== 'available'):
				isattached=volume.attach(instance_id,'/dev/xvdf')

				if isattached:
					print "Volume", volume_id,"attached successfully to the instance :",instance_id
				else:
					print "error attaching volume", volume_id, "to instance", instance_id

			else:
				print "Volume is in-use"

