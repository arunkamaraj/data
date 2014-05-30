import os
getcwd=os.getcwd()
#os.mkdir('/tmp/testing')
os.chdir('/tmp/testing')
cu=os.getcwd()

os.rmdir('/tmp/testing')
print getcwd,cu
