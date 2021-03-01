import re
import subprocess
import os
import sys


# output = open("/Users/a1455121/Desktop/test/python/output1.txt", "w")
# bad_words = [' [',':[','migrate','Warning','Extensions','Version','fingerprints','SHA']
# with open("/Users/a1455121/Desktop/test/python/output.txt") as input:
#     for line in input:
#         #if not (re.match('\r?\n', line)) and not line.startswith(('#','*',' ',']','[',',')) and not line.lstrip()[0].isdigit() not any(bad_word in line for bad_word in bad_words):
#         if not any(bad_word in line for bad_word in bad_words) and not (re.match('\r?\n', line)) and not line.startswith(('#','*',' ',']','[',',')) and not line.lstrip()[0].isdigit():
#             output.write(line)
#             print(line)
        
# input.close()
# output.close()

# with open("/Users/a1455121/Desktop/test/python/output1.txt","r") as input:
#     res = dict(item.split(":") for item in input.split("\n"))
#     print ("Resultant dictionary", str(res))


# output = open("/Users/a1455121/Desktop/test/python/output1.txt", "w")
# bad_words = [' [',':[','migrate','Warning','Extensions','Version','fingerprints','SHA']
# cmd = '/usr/bin/keytool -list -v -keystore /Users/a1455121/dccerts/test/toolshed/keystore.jks -storepass ds28agj'
# k  = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
# # def bytetostring():
# #         l= []
# #         for each in k:
# #                l.append(each.decode("utf-8"))
# #         print(l)

# # f = bytetostring(k)

# stdout, stderr = k.communicate()       
        

# lines =  stdout.decode("utf-8")
# names_list = lines.split("\n")

# test_list = list(filter(None, names_list))
# print(test_list)
# # for line in names_list:
# # #      #if not (re.match('\r?\n', line)) and not line.startswith(('#','*',' ',']','[',',')) and not line.lstrip()[0].isdigit() not any(bad_word in line for bad_word in bad_words):
# #       #if not any(bad_word in line for bad_word in bad_words) and not (re.match('\r?\n', line)) and not line.startswith(('#','*',' ',']','[',',')) and not line.lstrip()[0].isdigit():
# #       #if not line[0] == '#' or '*' or ' ' or ']'or '['or ','
# #         print(names_list)


# # #output.close()












# # f = open("/Users/a1455121/Desktop/test/python/output1.txt","r")
# # lines = f.readlines()

# # print (lines)




        
# ###Things to add
# #automate the command locate keytool and keytool complete command
# #automate the heart beat state 




cmd = '/usr/bin/keytool -list -v -keystore /Users/a1455121/dccerts/test/toolshed/keystore.jks -storepass ds28agj'
output = open("/Users/a1455121/Desktop/test/python/output1.txt", "w")
bad_words = ['Warning',' [',':[','Extensions','Version','fingerprints','SHA','MD5','   ']

with subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) as k:
    stdout, stderr = k.communicate()
    lines =  stdout.decode("utf-8")
    names_list = lines.split("\n")
    for line in names_list:
        #if re.search(r'^[^#,   *00\[ExtensionsVersionAuthorit\]]',line) and re.search(r'[^keyRSA\[ ]$',line):
            print (line)






output.close()
