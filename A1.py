pivots=[]
def rref(li):
    for row_num in range(len(li)):
        #interchange
        d={}
        for i in range(len(li)):
            flag=True
            for ele in range(len(li[i])):
                if li[i][ele]!=0:
                    if ele in d.keys():
                        d[ele].append(i)
                    else:
                        d[ele]=list()
                        d[ele].append(i)
                    flag=False
                    break
            if flag:
                if len(li[i]) in d.keys():
                    d[len(li[i])].append(i)
                else:
                    d[len(li[i])]=list()
                    d[len(li[i])].append(i)
        sort_list_keys=sorted(d.keys())
        li2=[]
        for x in sort_list_keys:
            for row in d[x]:
                li2.append(li[row])
        li=li2.copy()
        ##scaling
        safe=0#stores index of pivot point
        for element in range(len(li[row_num])):
            if li[row_num][element]!=0:
                safe=element
                break
        pivots.append(safe)
        safe2=li[row_num][safe]#stores value at index of pivot point
        for element in range(len(li[row_num])):
            if safe2!=0:
                li[row_num][element]/=safe2 
        ##addition
        for row_num_sub in range(len(li)):
            safe3=li[row_num_sub][safe]
            if row_num!=row_num_sub:
                for element in range(len(li[row_num_sub])):
                    li[row_num_sub][element]-=li[row_num][element]*safe3
                    if abs(li[row_num_sub][element])<0.00000000000001:
                        li[row_num_sub][element]=0.0
    return li
#input
li=[]
f=open('./file.txt')
for line in f:
    line=list(map(int,line.split()))
    li.append(line)
#####
li_new=rref(li).copy()
print()
for i in li_new:
    for j in i:
        print(round(j,4),end=' ')
    print()
####
pivo=[]
for i in range(len(li_new)):
    if 1 in li_new[i]:
        pivo.append(li_new[i].index(1))
####
#parametric

free_var=[]
for i in range(len(li_new[0])):
    if i not in pivo:
        free_var.append(i)
triv=[ 0.0 for x in range(len(li_new[0]))]
print(triv,end="+")
for i in range(len(li_new[0])-len(li_new)):
    li_new.append([0.0 for xyz in range(len(li_new[0]))])
for x in range(len(free_var)):
    print(f"x{free_var[x]}*",end="")
    li_temp=[round(-row[free_var[x]],3) for row in li_new]
    #
    for iter in free_var:
        li_temp.insert(iter,0)
        li_temp.pop()
    #
    li_temp[free_var[x]]=1
    if x!=len(free_var)-1:
        print(li_temp,end="+")
    else:
        print(li_temp)