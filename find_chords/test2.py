import copy
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
def real_cycle(cycle):
    new = []
    for i in cycle(V):
        for ii in i:
            new.append(set(ii)) 
    a = [new[0]]
    c = True
    for ii in new:
        for i in a:
            if i&ii==i:
                c = False
        if c:
            a.append(ii)
        else:
            c = True
    return c
@real_cycle
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
    fina_result = [list(result4), 
                   list(result5), 
                   list(result6), 
                   list(result7), 
                   list(result8), 
                   list(result9), 
                   list(result10),
                   ]

    return fina_result 

print(cycle(V))
