# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import copy

count = 0
var1 = sys.stdin.readlines()

var2 = list(map(str.rstrip,var1))
var = []
t1 = [len(var2[j]) for j in range(len(var2)) ]
var4=[]
dict = {var2[i]:t1[i] for i in range(len(var2))}
for i in dict:
    if dict[i]>=16:
        var.append(i)

for i in dict:
    if dict[i]==16:
        var4.append(i)


s = [i  for i in var for j in i if (j.isspace()==True)]
t = [var[j] for j in range(len(var)) if len(var[j])==16 or 19]
u = []
for i in var:
    if '-' in i:
        u.append(i)
        for i in u:
            j=i.split('-')
            for k in j:
                if len(k)==4:
                    try:
                        u.remove(i)
                    except:
                        pass
                else:
                    break

m=[]
var3 = var.copy()
for j in var3:
    if j in t:
        if '-' in j:
            r= "".join(j.split("-"))
            m.append(r)
            for i in range(len(r)):
                try:
                    if (r[i]==r[i+1]):
                        if (r[i+1]==r[i+2]):
                            if (r[i+2] == r[i+3]):
                                var3.remove(j)
                        
                except IndexError:
                     pass
            




for i in var:
    if i.isalpha()==False and i.startswith(('4','5','6')) == True and i not in s and i in t and i not in u and i in var4:
        print ("Valid")
    else:
        print("Invalid")
                
    

    
    
