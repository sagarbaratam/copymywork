import sys
arglist= sys.argv

class Emp:
    def __init__ (self,arglist):
        self.arglist = arglist

    def fullname(self):
        return '{}'.format(self.arglist[1:])


emp1 = Emp(arglist)
#emp2 = Emp('test','user',100)

print(emp1.fullname())
print(Emp.fullname(emp1))
