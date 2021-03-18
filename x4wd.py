import time
from os import system as oss
oss('clear')
oss('toilet -f mono12 -F gay "X4WD"')
auth = """Author : Mr.C72TR54

Github : https://www.github.com/teamx4ck

Facebook : X4ck cyber army

FB Page : Team X4CK"""
print('\n')
print(auth)
print('\n')
namee = str(input('Enter victim name : '))
def rit(file):
	f.write(file)
def rtn():
	f.write('\n')
path = '/sdcard/'+namee+'.txt'
path2 = '/sdcard/x4wd.txt'
nox = open(path2,'r')
nu = namee.upper()
nl = namee.lower()
f = open(path,'w')
rit(namee)
rtn()
rit(nu)
rtn()
rit(nl)
rtn()
if 'o' in namee:
	rit(namee.replace('o','0'))
elif  'O' in namee:
	rit(namee.replace('O','0'))
line = 0
print('Please wait......')
while True:
	rdd = nox.readline()
	f.write(namee+rdd)
	f.write(nu+rdd)
	if len(rdd) >= 6:
		f.write(rdd)
	line=line+1
	elif line==180:
		break
time.sleep(.2)
print('File saved : '+path)
f.close()