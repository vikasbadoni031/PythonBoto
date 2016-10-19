import boto
from boto.s3.key import Key

class S3_Functions:

	def __init__(self):
		print "S3 Constructor"

	def create_bucket(self,conn):
		bucket = conn.create_bucket('vikibucket',location='ap-southeast-2')

	def upload_file(self,file_name,bucket_name,conn):
		file=open('c:/vikas/2.txt')
		bucket=conn.get_bucket(bucket_name)
		k = Key(bucket)
		k.key=file_name
		result= k.set_contents_from_file(file)

	def download_file(self,src_file_name,dest_file_name,bucket_name,conn):
		bucket = conn.get_bucket(bucket_name)
		k = Key(bucket,src_file_name)
		k.get_contents_to_filename(dest_file_name)

	def move_bw_buckets(self,conn,src_buck_name,dest_buck_name,file_name):
		print "before"
		srcbucket=conn.get_bucket(src_buck_name)
		print "after first", srcbucket
		destbucket=conn.get_bucket(dest_buck_name)
		print "after second", destbucket
		destbucket.copy_key(file_name,srcbucket.name,file_name)

	def delete_file(self,conn,bucket_name,srcFileName):
		bucket = conn.get_bucket(bucket_name)
		k = Key(bucket,srcFileName)
		k.delete()

	def delete_bucket_func(self,conn,bucket_name):
		bucket = conn.delete_bucket(bucket_name)

	def empty_bucket(self,conn,bucket_name):
		bucket= conn.get_bucket(bucket_name)

		for i in bucket.list():
			print i.key
			i.delete()

	def list_all_buckets(self,conn):
		buckets = conn.get_all_buckets()
		for i in buckets:
			print i.name

			

