import sys
from stat import *
import os

if len(sys.argv) < 2:
	print('Usage: python fileperms.py <target dir>')
	sys.exit(1)

flist=[]
for (dirpath,dirname,filenames) in os.walk(sys.argv[1]):
	flist.extend(['%s/%s'%(dirpath,filename) for filename in filenames])

num = 0
for f in flist:
	if os.stat(f)[ST_MODE] & 4 != 0:
		print('world readable file: %s'%f)
		num+=1

print('\nTotal files: %s -- World readable files: %s'%(len(flist),nume))