#import re, sys

#map(sys.stdout.write,(l for l in sys.stdin if re.search(sys.argv[1],l)))

import subprocess
import re
import sys

#search_term = sys.argv[1]
l = subprocess.Popen('ls -lrt',shell=True,stdout=subprocess.PIPE)
out=l.stdout.read()

for line in out:
    if re.search(b'(\d).(\d)',line):
        print (line)
        if line == None:
            print ('no matches found')