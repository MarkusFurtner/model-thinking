
def sum_of(a,b):
    return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]
def minus(a):
    for i in range(0, len(a)):
        a[i]=-a[i]
    return a    
#a=[[0,1,2],[3,4,5],3,2,67]
#b=[1,2,3]

#print (a[-1])
#x=a.pop()
#print (x)
#print (a)

CUBE_SIZE=4
directions=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
cube=[]
def in_cube(n):
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                cube.append([i,j,k])
    return (cube)
cube= in_cube(CUBE_SIZE) 
#print (len(cube))
#print (cube)
L=[[0,1,0]]
n=0
d=0
D=[]
#J=[0,3,5,7,9,10,11,12,14,16,17,18,20,21,23,24,25]
J=[0,4,5,8,9,10,11,12,14,15,16,17,18,19,21,22,25,26,28,30,33,34,36,37,38,39,40,41,42,43,44,45,48,49,52,53,56,59,62]
def change_direction(Li,Di,direction):
    while (direction+1)%6 == Di[-1]:
        Li.pop()
        direction=Di.pop()
        
        while len(Li) not in J:
            Li.pop()
            direction=Di.pop()
            #if Di==[]:
               # L=[[1,0,0]]
            if len(Li)<10:
                print (Li,Di)
        
    
    else:
        direction = (direction +1)%6 
    
    
    #print ('change') 
    #print (positions,direction, directions[direction])
    return (Li,Di,direction)
 

          
            
def steps(Li,Di,di):
    n=len(Li)
    
    p=sum_of(Li[-1], directions[di])    
    
    if p in cube:
        if p not in Li:
             Li.append(p)
             Di.append(di)
             
             if (n+1) in J:                 
                 di= (di+1)%6
        else:
            if n in J:
                (Li,Di,di)=change_direction(Li,Di,di)        
            else:
                while len(Li) not in J:
                    Li.pop()
                    Di.pop()
                (Li,Di,di)=change_direction(Li,Di,di)     
    else:
        if n in J:
            (Li,Di,di)=change_direction(Li,Di,di) 
        else:
            while len(Li) not in J:
                Li.pop()
                Di.pop() 
            (Li,Di,di)=change_direction(Li,Di,di)    
    
    #print ('steps')    
    #print (Li,Di,di)

    return (Li,Di,di)

#change_direction([[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]],4)

i=0
while n in range(0,CUBE_SIZE**3):
    (L,D,d)= steps(L,D,d)
    n=len(L)
    i +=1
    if i%1000000==0:
        print(i)
    if len(L)> CUBE_SIZE**3-1:
        
        print ('Solution!')
        print (L,len(L),D,i)
        

