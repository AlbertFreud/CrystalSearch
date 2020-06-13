import os
import numpy as np
import copy
from collections import defaultdict
import sys
from multiprocessing import Pool



f_list = os.listdir()
res_list = []
for i in f_list:
	if os.path.splitext(i)[1] == '.res':
		res_list.append(i)
if res_list == []:
	sys.exit(0)
def multi(file_name):
	try:
		vertex_pack =  dict()
		with open(file_name,'r') as f:
			line = f.readline()
			count = 0
			while line != '':

				if line.split()[0] == 'CELL':
					edge_pack = np.mat([float(i) for i in line.split()[2:4]])
					angle = float(line.split()[7])
				if len(line.split()) == 7:

					vertex_pack[count] = np.mat([float(i) for i in line.split()[2:4]])
					count += 1
				line = f.readline()
	except NameError:
		print('Attention!!!!!!\nno file xxxxx.res')
	num_points = len(vertex_pack)
	fina_vertex = dict()
	for i in vertex_pack:
		for ii in [-1,0,1]:
			for iii in [-1,0,1]:
				fina_vertex[(i,(ii,iii))] = np.mat([vertex_pack[i][0,0]+ii,vertex_pack[i][0,1]+iii])



	# for init cystle
	class Graph:
	  
		def __init__(self):
			self.graph = defaultdict(set) # default dictionary to store graph
	  
		# function to add an edge to graph
		def addEdge(self,v,w):
			self.graph[v].add(w) #Add w to v_s list
			self.graph[w].add(v) #Add v to w_s list
	G=Graph()


	init_pack = defaultdict(list)
	#for i in range(1):
	for i in range(num_points):
		#creat an list to compare
		compare_list = dict()
		for ii in fina_vertex:
			a1a2 = (fina_vertex[(i,(0,0))] - fina_vertex[ii])[0,0]
			b1b2 = (fina_vertex[(i,(0,0))] - fina_vertex[ii])[0,1]
			dis = np.sqrt(a1a2**2*edge_pack[0,0]**2+2*a1a2*b1b2*edge_pack[0,0]*edge_pack[0,1]*np.cos(angle* np.pi / 180)+b1b2**2*edge_pack[0,1]**2)
			compare_list[ii] = dis
		min(compare_list,key=compare_list.get)
		del compare_list[min(compare_list,key=compare_list.get)]

		for iii in range(3):
			init_pack[(i,(0,0))].append(min(compare_list,key=compare_list.get))
			G.addEdge((i,(0,0)),min(compare_list,key=compare_list.get))

			del compare_list[min(compare_list,key=compare_list.get)]
	#need increase graph
	if num_points<14:
		for i in range(3):
			add_list=(G.graph.keys()-init_pack.keys()).copy()
			#print(add_list)
			#print(init_pack)
			for i in add_list:
				for ii in range(3):
					G.addEdge(i,(init_pack[(i[0],(0,0))][ii][0],(init_pack[(i[0],(0,0))][ii][1][0]+i[1][0],init_pack[(i[0],(0,0))][ii][1][1]+i[1][1])))
	elif num_points>13 and num_points<16 :
		for i in range(2):
			add_list=(G.graph.keys()-init_pack.keys()).copy()
			#print(add_list)
			#print(init_pack)

			for i in add_list:
				for ii in range(3):
					G.addEdge(i,(init_pack[(i[0],(0,0))][ii][0],(init_pack[(i[0],(0,0))][ii][1][0]+i[1][0],init_pack[(i[0],(0,0))][ii][1][1]+i[1][1])))
	elif num_points>15:
		add_list=(G.graph.keys()-init_pack.keys()).copy()
		#print(add_list)
		#print(init_pack)

		for i in add_list:
			for ii in range(3):
				G.addEdge(i,(init_pack[(i[0],(0,0))][ii][0],(init_pack[(i[0],(0,0))][ii][1][0]+i[1][0],init_pack[(i[0],(0,0))][ii][1][1]+i[1][1])))


	V=G.graph

	def cycle(V):
		result4 = set()
		result5 = set()
		result6 = set()
		result7 = set()
		result8 = set()
		result9 = set()
		result10 = set()
		def search(V, cur, this=None):
			if this is None:
				this = []
			for p in V[cur]:
				if p not in this:
					search(V, p, this+[p])
				else:
					if len(this) >= 4 and this[-4] == p:
						result4.add(tuple(sorted(this[-4:])))
					elif len(this) >= 5 and this[-5] == p:
						result5.add(tuple(sorted(this[-5:])))
					if len(this) >= 6 and this[-6] == p:
						result6.add(tuple(sorted(this[-6:])))
					elif len(this) >= 7 and this[-7] == p:
						result7.add(tuple(sorted(this[-7:])))
					if len(this) >= 8 and this[-8] == p:
						result8.add(tuple(sorted(this[-8:])))
					elif len(this) >= 9 and this[-9] == p:
						result9.add(tuple(sorted(this[-9:])))
					if len(this) >= 10 and this[-10] == p:
						result10.add(tuple(sorted(this[-10:])))
		search(V,list(V.keys())[0],)
		fina_result = [list(result4), 
					   list(result5), 
					   list(result6), 
					   list(result7), 
					   list(result8), 
					   list(result9), 
					   list(result10),
					   ]
		return fina_result 

	def real_cycle():
		new = []
		for i in cycle(V):
			for ii in i:
				new.append(set(ii)) 
		if new == []:
			pass
			return None
		else:
			a = [new[0]]
			c = True
			for ii in new:
				for i in a:
					if len(i&ii)>4:
						c = False
				if c:
					a.append(ii)
				else:
					c = True
			return a
	import math

	#------------------area--------------------
	class Point():
		def __init__(self,x,y):
			self.x = x
			self.y = y
	def GetAreaOfPolyGon(points):
		area = 0
		if(len(points)<3):
			
			 raise Exception("error")
		p1 = points[0]
		for i in range(1,len(points)-1):
			p2 = points[1]
			p3 = points[2]
			#计算向量
			vecp1p2 = Point(p2.x-p1.x,p2.y-p1.y)
			vecp2p3 = Point(p3.x-p2.x,p3.y-p2.y)        
			#判断顺时针还是逆时针，顺时针面积为正，逆时针面积为负
			vecMult = vecp1p2.x*vecp2p3.y - vecp1p2.y*vecp2p3.x   #判断正负方向比较有意思
			sign = 0
			if(vecMult>0):
				sign = 1
			elif(vecMult<0):
				sign = -1
			triArea = GetAreaOfTriangle(p1,p2,p3)*sign
			area += triArea
		return abs(area)
	def GetAreaOfTriangle(p1,p2,p3):
		'''计算三角形面积   海伦公式'''
		area = 0
		p1p2 = GetLineLength(p1,p2)
		p2p3 = GetLineLength(p2,p3)
		p3p1 = GetLineLength(p3,p1)
		s = (p1p2 + p2p3 + p3p1)/2
		area = s*(s-p1p2)*(s-p2p3)*(s-p3p1)   #海伦公式
		area = math.sqrt(area)
		return area
	def GetLineLength(p1,p2):
		'''计算边长'''
		length = math.pow((p1.x-p2.x),2) + math.pow((p1.y-p2.y),2)  #pow  次方
		length = math.sqrt(length)   
		return length    

	#-----------------area---------------------


	for i in range(num_points):
		time_count = 0
		area_count = 0
		print('------------\n',(i,(0,0)),' \n------------')
		for ii in real_cycle():
			if (i,(0,0)) in ii:
				points = []
				for iii in list(ii): 
					points.append(Point(fina_vertex[iii][0,0]*edge_pack[0,0]+fina_vertex[iii][0,1]*edge_pack[0,1]*np.cos(angle* np.pi / 180),fina_vertex[iii][0,1]*edge_pack[0,1]*np.sin(angle* np.pi / 180)))
				area = GetAreaOfPolyGon(points)
				print(area)
				area_count = area_count+area
				time_count +=1 
		print('------------\n',time_count)
		print('S:',area_count-time_count*15.7162826 )

		


if __name__ == '__main__':
	p = Pool(5)
	print(p.map(multi, res_list))





