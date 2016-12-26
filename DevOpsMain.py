from aws import Connection
from aws import EC2Instance
from aws import Volumes
from aws import Security
from aws import S3_Functions


connInstance = Connection()

#conn = connInstance.ec2Connection()
#
#print conn

"""
ec2 = EC2Instance()
ec2.list_instances(conn)
"""

#vols= Volumes()
#vols.list_volumes(conn)

#vols.attach_volume(conn, 'vol-0085b88d', 'i-06bb7f04eed0c815f')

#Seg1= Security()
#Seg1.list_security_groups(conn)


#-----------------------
conn = connInstance.s3Connection()
print conn


s3obj1 = S3_Functions()
#s3obj1.create_bucket(conn)
#s3_obj1 = conn.create_bucket('vikibadoni031bucket',location='ap-southeast-2')

#s3obj1.upload_file("2.txt", "vikibucket", conn)

#s3obj1.download_file('2.txt', 'c:/vikas/viki.txt', 'vikibucket', conn)
#s3obj1.move_bw_buckets(conn, 'vikibucket', 'vikidestbucket', '2.txt')

#s3obj1.delete_file(conn, 'vikibucket', '1.txt')

#s3obj1.delete_bucket_func(conn, 'vikidestbucket')

#s3obj1.empty_bucket(conn, 'vikidestbucket')

s3obj1.list_all_buckets(conn)