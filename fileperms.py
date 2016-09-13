"""
This script processes a given directory and prints the
    percentage of world permissions found.
Re-write of https://github.com/Atticuss/FilePerms
"""
import sys
import os
from stat import ST_MODE


class Perms:
    """Contains the methods/function related to parsing and printing
        file perms."""
    def __init__(self, input_dir):
        self.indir = input_dir
        self.flist = []
        self.rlist = []
        self.wlist = []
        self.elist = []

    def get_files(self):
        """Builds a list of files for a give directory"""
        for (dirpath, _, filenames) in os.walk(self.indir):
            self.flist.extend(['%s/%s' % (dirpath, filename)
                               for filename in filenames])

    def parse_perms(self):
        """Parses the files in flist for file perms"""
        for permf in self.flist:
            if os.stat(permf)[ST_MODE] & 4 != 0:
                self.rlist.append(permf)
            if os.stat(permf)[ST_MODE] & 2 != 0:
                self.wlist.append(permf)
            if os.stat(permf)[ST_MODE] & 1 != 0:
                self.elist.append(permf)

    @staticmethod
    def _freq(x, y):
        """Returns the frequency of occurence for 2 numbers"""
        return x / y * 100.0

    def stats(self):
        """return %readable, %writable, %executable"""
        return (self._freq(len(self.rlist), len(self.flist)),
                self._freq(len(self.wlist), len(self.flist)),
                self._freq(len(self.elist), len(self.flist)))

    def print_list(self, ltype, pnum=None):
        """Print list based on ltype and pnum
            pnum is the number of items to print"""
        if ltype == "e":
            if not pnum:
                pnum = len(self.elist)
            for i in xrange(0, pnum):
                print(self.elist[i])
        elif ltype == 'w':
            if not pnum:
                pnum = len(self.wlist)
            for i in xrange(0, pnum):
                print(self.wlist[i])
        elif ltype == 'r':
            if not pnum:
                pnum = len(self.rlist)
            for i in xrange(0, pnum):
                print(self.rlist[i])

if len(sys.argv) < 2:
    indir = input("Enter the directory to parse: ")
else:
    indir = sys.argv[1]

p = Perms(indir)
p.get_files()
p.parse_perms()
readable, writable, executable = p.stats()

print('\nTotal files: %s' % len(p.flist))
print('%% +R: %s' % readable)
print('%% +W: %s' % writable)
print('%% +E: %s' % executable)
