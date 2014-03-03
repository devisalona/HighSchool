from math import *
from copy import *
def lstToNum(l):
    s = ""
    for i in l:
        s += str(i)
    return int(s)
def printQ(l,len):
    print "#"*(2*len+2)
    for col in l:
        s = " -" * (len-1)
        s = s[:2*col] + " Q" + s[2*col:]
        
        print "#" + s + "#"
    print "#"*(2*len+2)
    print
def conflict(state,x):
    L = len(state)
    for i in range(L):
        if state[i] - x == 0 or fabs(float(x-state[i])/(L-i)) == 1:
            return True
    return False
def validSolution(sList):
    t = [sList[0]]
    for i in sList[1:]:
        if conflict(t,i):
            #print t
            return False
        t.extend([i])
    return True
def findSol(L,leng):
    global total
    if len(L) == leng:
        #print L
        if validSolution(L) == True:
            #print L
            co1 = []
            co1.extend(L)
            total.append(co1)
            #return total
    else:
        t = []
        t.extend(L)
        for i in range(0,leng):
            if t.count(i) == 0:
                t.append(i)
                findSol(t,leng)
                t.remove(i)
def findTwelve(L,len):
    unique = []
    for i in L:
        temp = [0]*len
        temp2 = [0]*len
        temp3 = [0]*len
        temp4 = [0]*len
        temp6 = [0]*len

        for ind in range(0,len):
            temp[ind] = len-1-i[ind]
        for ind in range(0,len):
            temp2[i[ind]]=ind
        for ind in range(0,len):
            temp3[len-1-i[ind]]= len-1-ind
        cop = []
        cop = deepcopy(i)
        cop.reverse()
        temp5 = []; temp5= deepcopy(temp); temp5.reverse()
        temp7 = []; temp7= deepcopy(temp2); temp7.reverse()
        temp6 = []; temp6= deepcopy(temp3); temp6.reverse()
        listOfTrans = [temp,temp2,temp3,temp5,temp6,temp7,cop]
        con = 0
        for y in listOfTrans:
            if unique.count(y) != 0:
                con += 1
        if con == 0:
            unique.append(i)
        
##        for y in L:
##            if y == cop or y == temp or y == temp2 or y == temp3 or y == temp4 or y == temp5 or y == temp6 or y ==temp7:
##                L.remove(y)
    return unique
total = []  
lst = [0,1,2,3,4]
#printQ(lst)
#print lstToNum(lst)
#print validSolution(lst)
findSol([],len(lst))
#print total,len(total)
list1 = findTwelve(total,len(lst))
for i in list1:
    printQ(i,len(lst)),
print len(list1)
