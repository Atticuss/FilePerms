import sys
from stat import *
import os

if len(sys.argv) < 2:
	print('Usage: python fileperms.py <target dir>')
	sys.exit(1)

flist=[]
for (dirpath,dirname,filenames) in os.walk(sys.argv[1]):
	flist.extend(['%s/%s'%(dirpath,filename) for filename in filenames])

readable = 0
writeable = 0
executable = 0
for f in flist:
	if os.stat(f)[ST_MODE] & 4 != 0:
		print('world readable file: %s'%f)
		readable+=1
	if os.stat(f)[ST_MODE] & 2 != 0:
		print('world writable file: %s'%f)
		writable+=1
	if os.stat(f)[ST_MODE] & 1 != 0:
		print('world executable file: %s'%f)
		executable+=1

print('\nTotal files: %s'%len(flist))
print('World readable: %s'%readable)
print('World writable: %s'%writeable)
print('World executable: %s'%executable)