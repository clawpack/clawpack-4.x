
#
# Fix a set of target files in directory tree rootdir by replacing
# oldpat with newpat. 
#
# Now supports wildcards in list of targetfiles.
#

import os,sys,glob

#rootdir = '..'
clawdir = os.path.expandvars('$CLAW')
rootdir = clawdir
targetfiles = ['*.html','load.js']
oldpat = "http://localhost:50005"
newpat = "http://depts.washington.edu/clawpack/clawpack-4.6.2"

print "Will change ", oldpat
print "  to        ", newpat
print "  in all of ", rootdir
ans = raw_input("Ok? ")
if ans.lower() not in ['y','yes']:
    print "Aborting."
    sys.exit()

for (dirpath, subdirs, files) in os.walk(rootdir):
    currentdir = os.path.abspath(os.getcwd())
    os.chdir(os.path.abspath(dirpath))
    tfiles = []
    for fpat in targetfiles:
        for f in glob.glob(fpat):
            tfiles.append(f)
    for file in tfiles:

        infile = open(file,'r')
        lines = infile.read()
        infile.close()

        if lines.find(oldpat) > -1:
            lines = lines.replace(oldpat, newpat)
            print "Fixed file   ",dirpath + '/' + file
        else:
            print "No change to ",dirpath + '/' + file

        outfile = open(file,'w')
        outfile.write(lines)
        outfile.close()

    os.chdir(currentdir)

