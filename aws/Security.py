import boto.ec2

class Security:
	def __init__(self):
		print "Security constructor"

	def list_security_groups(self,conn):
		print "Listing security group"

		groups= conn.get_all_security_groups()

		if groups:

			for g in groups:
				print "\nSG"
				print "group name", g.name
				print "Description", g.description
				print "VPC ID", g.vpc_id
				rules= g.rules

				if rules:
					rulestr=""
					for r in range(len(rules)):
						protocol=rules[r].ip_protocol
						from_port=rules[r].from_port
						to_port=rules[r].to_port
						grants=rules[r].grants

						if r==0:
							rulestr=""
						else:
							rulestr= rulestr + '\n'

						if protocol:
							rulestr=rulestr + "Protocol" + protocol
						if from_port:
							rulestr=rulestr + " | from port: " + from_port
						if to_port:
							rulestr=rulestr + " | to port: " + to_port
						if grants:
							rulestr=rulestr + ' | grants:' + str(grants).strip('[]')

						print rulestr
						print "****************************"



