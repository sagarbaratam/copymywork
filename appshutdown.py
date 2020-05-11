
import subprocess
import re


cmd = ""
bad_words = ['Warning',' [',':[','Extensions','Version','fingerprints','SHA','MD5','   ','recommended']

with subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) as k:
    stdout, stderr = k.communicate()
    lines =  stdout.decode("utf-8")
    names_list = lines.split("\n")
    for line in names_list:
        if not line.startswith((' ','#','*',']','[',',')) and not any(bad_word in line for bad_word in bad_words) and "".join([s for s in line.strip().splitlines(True) if s.strip("\r\n").strip()]):
            print(line)


        


#not any(bad_word in line for bad_word in bad_words) and not (re.match('\r?\n', line)) 






