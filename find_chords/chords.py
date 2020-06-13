import os
import numpy as np
from collections import defaultdict
f_list = os.listdir()
for i in f_list:
    if os.path.splitext(i)[1] == '.res':
        file = i
try:
	vertex_pack = defaultdict(list)
	with open(file,'r') as f:
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

V={
    1:{2,6},
    2:{1,3},
    3:{2,4,8},
    4:{3,5,9},
    5:{4,10},
    6:{1,7},
    7:{6,8},
    8:{3,7,9},
    9:{4,8,10},
    10:{5,9},
}
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
    search(V,1,)
    fina_result = [result4, 
                   result5, 
                   result6, 
                   result7, 
                   result8, 
                   result9, 
                   result10,]

    return fina_result 
print(cycle(V))


print(angle)
print(edge_pack)
print(vertex_pack)

