import sys
from subprocess import call
def createfqdn():
    str = sys.argv[1]
    name = str.lower()
    if name.endswith("-m.bby"):
	    call("/usr/local/bin/ssh "+name, shell=True)
    else:
        FQDN = name+"-m.bby"
        print("Adding -m.bby since its not there")
        call("/usr/local/bin/ssh "+FQDN, shell=True)

createfqdn()
