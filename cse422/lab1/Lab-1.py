# A* search
from collections import deque
 
class Search:
    def __init__(self, lst):
        self.lst = lst
        self.huristic={}
        
    def Update_huristic(self,hu):
        self.huristic=hu
        
    def Huristic(self,node):        
        return self.huristic[node]   
    
    def Neighbor(self, ver):
        return self.lst[ver]
    
    def A_star_search(self, start, end):
        open_set = set([start])
        closed_set = set([])
        
        pre_dic = {}
        pre_dic[start] = 0
 
        pos_dic = {}
        pos_dic[start] = start
        
        #########################
        while len(open_set) > 0:
            n = None
            for v in open_set:
                if n == None or pre_dic[v] + self.Huristic(v) < pre_dic[n] + self.Huristic(n):
                    n = v;
 
            if n == None:
                return('NO PATH FOUND')
 
            if n == end:
                re_pat = []
 
                while pos_dic[n] != n:
                    re_pat.append(n)
                    n = pos_dic[n]
 
                re_pat.append(start)
 
                re_pat.reverse()
 
                return re_pat
    
            ##################################
            for (m, dis) in self.Neighbor(n):
                if (m not in open_set) and (m not in closed_set):
                    open_set.add(m)
                    pos_dic[m] = n
                    pre_dic[m] = pre_dic[n] + dis

                else:
                    if pre_dic[m] > pre_dic[n] + dis:
                        pre_dic[m] = pre_dic[n] + dis
                        pos_dic[m] = n
 
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
                
            open_set.remove(n)
            closed_set.add(n)
 
        return('NO PATH FOUND')
#############################################################

#file read

input_file=open("input.txt")

name={"Arad":"A","Neamt":"F","Bucharest":"Z","Oradea":"B","Craiova":"S","Pitesti":"P","Eforie":"T","RimnicuVilcea":"R",
      "Fagaras":"O","Timisoara":"C","Dobreta":"V","Urziceni":"D","Hirsova":"N","Vaslui":"H","lasi":"Q","Zerind":"E",
       "Lugoj":"G","Mehadia":"L","Giurgiu":"X","Sibiu":"Y"}

symbol={"A":"Arad","F":"Neamt","Z":"Bucharest","B":"Oradea","S":"Craiova","P":"Pitesti","T":"Eforie","R":"Rimnicu Vilcea",
      "O":"Fagaras","C":"Timisoara","V":"Dobreta","D":"Urziceni","N":"Hirsova","H":"Vaslui","Q":"lasi","E":"Zerind",
       "G":"Lugoj","L":"Mehadia","X":"Giurgiu","Y":"Sibiu"}


l=input_file.readlines()
d={}
h={}
for n in l:
    line=n.strip().split(" ")
    node=name[line[0]] #A,B,C tay cobevert

    #node=line[0]
    #print(name[node])
    h[node]=int(line[1])
    for i in range(2,len(line),2):
        nam=name[line[i]]
        dis=int(line[i+1])
        t=(nam,dis)
        if node in d:
            d[node]=d[node]+[t]
        else:
            d[node]=[t]
        
    
    
#print(h)
#print(d)
obj = Search(d)
obj.Update_huristic(h)
path=obj.A_star_search('A', 'Z')
#print(len(path))

c=0

distance=0
while c<len(path)-1:
    m=path[c]
    l=d[m]
    for tup in l:
        if path[c+1] in tup:
            distance+=tup[1]
    
    c+=1
              
        
#print(distance)
print("Path:",end=" ")
for i in range(len(path)-1):
    print(symbol[path[i]],end=" ->")
    
print(symbol[path[-1]])  
print("Total distance:",distance)
input_file.close()





