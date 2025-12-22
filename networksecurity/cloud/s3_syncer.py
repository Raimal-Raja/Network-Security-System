import os 




# class S3Sync:
#     def sync_folder_to_s3(self,folder,aws_bucket_url):
#         command = f"aws s3 sync {folder} {aws_bucket_url}"
#         os.system(command)
        
#     def sync_folder_from_s3(self,folder,aws_bucket_url):
#         command = f"aws s3 sync {aws_bucket_url} {folder}"
#         os.system(command)


import subprocess

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        try:
            command = ["aws", "s3", "sync", folder, aws_bucket_url]
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"S3 sync failed: {e}")

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        try:
            command = ["aws", "s3", "sync", aws_bucket_url, folder]
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"S3 sync failed: {e}")
