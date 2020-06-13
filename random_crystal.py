__aurthor__ = 'yinhengchuang@gmail.com'
from numpy import *
import numpy as np
import random
import os
# pack_mat times pack_position
def multiply(pack_mat, pack_position):
	old_position = []
	for i in pack_position:
		for ii in pack_mat:
			old_position.append((i * ii)%1)
	return old_position

#pop too close site 
def judge(b,limit):
	a = [b[0]]
	c = True
	for ii in b:
		for i in a:
			if sqrt((ii - i)*(ii - i).T) <= limit:
				c = False
		if c:
			a.append(ii)
		else:
			c = True
	return a

# correct a1 a2 b1 b2 angle
def correct(line, a, b, angle):
	#a=b angle=90
	case1 = [
		'GroupID=10',
		'GroupID=11', 'GroupID=12']
	#a!=b angle=90
	case2 = ['GroupID=3',
		'GroupID=4','GroupID=6', 'GroupID=7']
	#a=b andle!=90
	case3 = ['GroupID=5',
		'GroupID=8']
	#a!=b angle!=90
	case4 = ['GroupID=9'
			'GroupID=13', 'GroupID=14', 'GroupID=15', 
		'GroupID=16','GroupID=17']
	#oblique
	case5 = ['GroupID=1', 'GroupID=2']

	if line in case1:
		b = a
		angle = 90 
		pass
	elif line in case2:
		angle = 90
		pass
	elif line in case3:
		b =a 

		pass
	elif line in case4:
		pass
	elif line in case5:
		pass
	return (a, b, angle)

# generate point postion randomly,return site_pack 
def postition(a, b, nums):
	scale = round(b/a, 2)
	if scale > 2:
		bpart =scale//1  
		apart = 10
		bpart = 10 * bpart 
	else:
		apart = bpart = 10
	xx = random.sample(range(1, int(apart)), nums)
	yy = random.sample(range(1, int(bpart)), nums)
	xstep = 1/apart
	ystep = 1/bpart
	site_pack = []
	for i in range(nums):
		c = np.random.uniform((xx[i]-1)*xstep, xx[i]*xstep)
		d = np.random.uniform((yy[i]-1)*ystep, yy[i]*ystep)
		site = mat((c, d,1))
		site_pack.append(site)
	return site_pack
# from Group_ID to get operation matrix
def mat_pack(name):
	GroupID_1=\
	'''
	GroupID=1    Name=p1    OpNum=1    
	op001=x,y
	 1   0   0
	 0   1   0
	'''
	GroupID_2=\
	'''
	GroupID=2    Name=p2    OpNum=2    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,-y
	-1   0   0
	 0  -1   0
	'''
	GroupID_3=\
	'''
	GroupID=3    Name=p1m1   OpNum=2    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,y
	-1   0   0
	 0   1   0
	'''
	GroupID_4=\
	'''
	GroupID=4    Name=p1g1    OpNum=2    
	op001=x,y,
	 1   0   0
	 0   1   0
	op002=-x,y+1/2
	-1   0   0
	 0   1   0.5
	'''
	GroupID_5=\
	'''
	GroupID=5    Name=c1m1    OpNum=4    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,y
	-1   0   0
	 0   1   0
	op003=x+1/2,y+1/2
	 1   0   0.5
	 0   1   0.5
	op004=-x+1/2,y+1/2
	-1   0   0.5
	 0   1   0.5
	'''
	GroupID_6=\
	'''
	GroupID=6    Name=p2mm    OpNum=4    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,-y
	-1   0   0
	 0  -1   0
	op003=-x,y
	-1   0   0
	 0   1   0
	op004=x,-y
	 1   0   0
	 0  -1   0
	'''
	GroupID_7=\
	'''
	GroupID=7    Name=p2mg    OpNum=4   
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,-y
	 1   0   0
	 0  -1   0
	op003=-x+1/2,y
	-1   0   0.5
	 0   1   0
	op004=x+1/2,-y
	 1   0   0.5
	 0  -1   0
	'''
	GroupID_8=\
	'''
	GroupID=8    Name=p2gg    OpNum=4    
	op001=x,y
	 1   0   0
	 0   1   0 
	op002=-x,-y
	-1   0   0
	 0  -1   0
	op003=-x+1/2,y+1/2
	-1   0   0.5
	 0   1   0.5
	op004=x+1/2,-y+1/2
	 1   0   0.5 
	 0  -1   0.5
	'''
	GroupID_9=\
	'''
	GroupID=9    Name=c2mm    OpNum=8   
	op001=x,y
	 1   0   0
	 0   1   0  
	op002=-x,-y
	 1   0   0
	 0  -1   0  
	op003=-x,y
	-1   0   0
	 0   1   0
	op004=x,-y
	 1   0   0 
	 0  -1   0
	op005=x+1/2,y+1/2
	 1   0   0.5
	 0   1   0.5
	op006=-x+1/2,-y+1/2
	-1   0   0.5 
	 0  -1   0.5
	op007=-x+1/2,y+1/2
	-1   0   0.5
	 0   1   0.5
	op008=x+1/2,-y+1/2
	 1   0   0.5 
	 0  -1   0.5
	'''
	GroupID_10=\
	'''
	GroupID=10    Name=p4    OpNum=4    
	op001=x,y 
	 1   0   0
	 0   1   0
	op002=-x,-y
	-1   0   0 
	 0  -1   0
	op003=-y,x
	 0  -1   0
	 1   0   0
	op004=y,-x
	 0   1   0
	-1   0   0
	'''
	GroupID_11=\
	'''
	GroupID=11    Name=p4mm    OpNum=8   
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,-y
	-1   0   0
	 0  -1   0
	op003=-y,x
	 0  -1   0
	 1   0   0
	op004=y,-x
	 0   1   0
	-1   0   0
	op005=-x,y
	-1   0   0
	 0   1   0
	op006=x,-y
	 1   0   0
	 0  -1   0
	op007=y,x
	 0   1   0
	 1   0   0
	op008=-y,-x
	 0  -1   0
	-1   0   0
	'''
	GroupID_12=\
	'''
	GroupID=12    Name=p4gm    OpNum=8    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-x,-y
	-1   0   0
	 0  -1   0
	op003=-y,x
	 0  -1   0
	 1   0   0
	op004=y,-x
	 0   1   0
	-1   0   0
	op005=-x+1/2,y+1/2
	-1   0   0.5
	 0   1   0.5
	op006=x+1/2,-y+1/2
	 1   0   0.5 
	 0  -1   0.5
	op007=y+1/2,x+1/2
	 0   1   0.5
	 1   0   0.5
	op008=-y+1/2,-x+1/2
	 0  -1   0.5 
	-1   0   0.5
	'''
	GroupID_13=\
	'''
	GroupID=13    Name=p3    OpNum=3   
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-y,x-y
	 0  -1   0
	 1  -1   0
	op003=-x+y,-x
	-1   1   0
	-1   0   0
	'''
	GroupID_14=\
	'''
	GroupID=14    Name=p3m1    OpNum=6    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-y,x-y
	 0  -1   0
	 1  -1   0
	op003=-x+y,-x
	-1   1   0
	-1   0   0
	op004=-y,-x
	 0  -1   0
	-1   0   0
	op005=-x+y,y
	-1   1   0
	 0   1   0
	op006=x,x-y
	 1   0   0
	 1  -1   0
	'''
	GroupID_15=\
	'''
	GroupID=15    Name=p31m    OpNum=6    
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-y,x-y
	 0  -1   0
	 1  -1   0
	op003=-x+y,-x
	-1   1   0
	-1   0   0
	op004=y,x
	 0   1   0
	 1   0   0
	op005=x-y,-y
	 1  -1   0
	 0   1   0
	op006=-x,-x+y
	-1   0   0 
	-1   1   0
	'''
	GroupID_16=\
	'''
	GroupID=16    Name=p6    OpNum=6   
	op001=x,y
	 1   0   0
	 0   1   0
	op002=-y,x-y
	 0  -1   0
	 1  -1   0
	op003=-x+y,-x
	-1   1   0
	-1   0   0
	op004=-x,-y
	-1   0   0
	 0  -1   0
	op005=y,-x+y
	 0   1   0
	-1   1   0
	op006=x-y,x
	 1  -1   0 
	 1   0   0
	'''
	GroupID_17=\
	'''
	GroupID=17    Name=p6mm    OpNum=12   
	op001=x,y
	 1   0   0
	 0   1   0
	op002=y,x-y
	 0  -1  0
	 1  -1   0
	op003=-x+y,-x
	-1   1   0
	-1   0   0
	op004=-x,-y
	-1   0   0
	 0  -1   0
	op005=y,-x+y
	 0   1   0
	-1   1   0
	op006=x-y,x
	 1  -1   0 
	 1   0   0
	op007=-y,-x
	 0  -1   0
	-1   0   0
	op008=-x+y,y
	-1   1   0 
	 0   1   0
	op009=x,x-y
	 1   0   0
	 1  -1   0
	op0010=y,x
	 0   1   0
	 1   0   0
	op0011=x-y,y
	 1  -1   0
	 0  -1   0
	op0012=-x,-x+y
	-1   0   0
	-1   1   0
	'''
	mat_pack = []
	for i in range(len(eval(name).split()[3 :])//7):
		pass_m = [float(ii) for ii in eval(name).split()[4 + 7 * i : 10 + 7 * i]]
		mat_pack.append(mat(np.array(pass_m).reshape((2,3))).T)
	return(mat_pack)
# fina - write file
def writepart(filename,a,b,angle,new_postition):
	f1 = open(filename,'w')
	f1.writelines('TITL  C\n')
	str1 = 'CELL'
	str2 = '0.00000'
	str3 = '20.0000'
	str4 = '90.0000'
	ss = '{0:<7}{1}{4}{5:.5f}{4}{6:.5f}{4}{2}{4}{3}{4}{3}{4}{7:.5f}'.format(str1,str2,str3,str4,'    ',a,b,angle)
	f1.writelines(ss)
	f1.writelines('\nLATT  -1\nSFAC   C\n')
	n = 0
	tail = '0.50000    1.00000    0.00000'
	space = 4 * ' '
	for i in new_postition:
		n += 1
		head = 'C'+str(n)
		ii = i.tolist()[0]
		ss = '{0:<6}1{3}{1:.5f}{3}{2:.5f}{3}{4}\n'.format(head,float(ii[0]),float(ii[1]),space,tail)
		f1.writelines(ss)
	f1.writelines('END')
	f1.close()

#eachnums =input('please input eachnums:')
smallfilename = os.getcwd()
iiii = 0
#for GroupID in range(1, 17):
GroupID = 14
for i in range(5000):

	line = 'GroupID='+str(GroupID)
	line = line.strip()
	a = np.random.uniform(2, 8)
	b = np.random.uniform(2, 8)
	angle = np.random.uniform(80, 100)
	(a, b, angle) = correct(line, a, b, angle)
	name = 'GroupID_'+str(GroupID)
	name = name.strip()
	pack_mat = mat_pack(name)
	nums = np.random.randint(2, 4)
	pack_position = postition(a, b, nums)


	old_position = multiply(pack_mat, pack_position)
	new_postition = judge(old_position,0.1)
	eachname = smallfilename+'\\input\\'+str(GroupID)+'_'+'a'+str(a)[0:3]+'b'+str(b)[0:3]+'gama'+str(angle)+str(iiii)+'.res'
	writepart(eachname,a,b,angle,new_postition)
	iiii += 1
