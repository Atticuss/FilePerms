"""
This script processes a given directory and prints the
    percentage of world permissions found.
Re-write of https://github.com/Atticuss/FilePerms
"""
from sys import argv
from os import stat, walk
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
        for (dirpath, _, filenames) in walk(self.indir):
            self.flist.extend(['%s/%s' % (dirpath, filename)
                               for filename in filenames])

    def parse_perms(self):
        """Parses the files in flist for file perms"""
        for permf in self.flist:
            try:
                if stat(permf)[ST_MODE] & 4 != 0:
                    self.rlist.append(permf)
                if stat(permf)[ST_MODE] & 2 != 0:
                    self.wlist.append(permf)
                if stat(permf)[ST_MODE] & 1 != 0:
                    self.elist.append(permf)
            except:
                pass
    @staticmethod
    def _freq(x, y):
        """Returns the frequency of occurence for 2 numbers"""
        return float(x) / float(y) * 100.0

    def stats(self):
        """return %readable, %writable, %executable"""
        return (self._freq(len(self.rlist), len(self.flist)),
                self._freq(len(self.wlist), len(self.flist)),
                self._freq(len(self.elist), len(self.flist)))

    def print_list(self, ltype, pnum=None):
        """Print list based on ltype and pnum
            pnum is the number of items to print"""
        if ltype == "e":
            if not pnum or pnum > len(self.elist):
                pnum = len(self.elist)
            for i in range(0, pnum):
                print(self.elist[i])
        elif ltype == 'w':
            if not pnum or pnum > len(self.wlist):
                pnum = len(self.wlist)
            for i in range(0, pnum):
                print(self.wlist[i])
        elif ltype == 'r':
            if not pnum or pnum > len(self.rlist):
                pnum = len(self.rlist)
            for i in range(0, pnum):
                print(self.rlist[i])

# if copying/pasting into the interpreter set this equal to something!
indir = None

if len(argv) < 2 and not indir:
    print("Oi, you forgot a dir! Set indir or specify a cmd arg")
    exit(-1)
else:
    indir = argv[1]

p = Perms(indir)
p.get_files()
p.parse_perms()
readable, writable, executable = p.stats()

print('\nTotal files: %s' % len(p.flist))
print('%% +R: %s' % readable)
print('%% +W: %s' % writable)
print('%% +E: %s' % executable)
