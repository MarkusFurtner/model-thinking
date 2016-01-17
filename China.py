

M=900 #number of mashines or capital
demography=[5,5,5,5,5,5,5,5,5,5,
           5,5,5,5,5,5,5,5,5,5,
           10,10,10,10,10,10,10,10,10,10,
           10,10,10,10,10,10,10,10,10,10,
           10,10,10,10,10,10,10,10,10,10,
           10,10,10,10,10,10,10,10,10,10,
           10,10,10,10,10,10,10,10,10,10,
           5,5,5,5,5,5,5,5,5,5,
           5,5,5,5,5,5,5,5,5,5,
           5,5,5,5,5,5,5,5,5,5]
#The value on position n represents the number of people of age n in society 
print (sum(demography)) 
print ("citizens")
def workers(demo):
    return sum(demo[20:70])
               
L = workers(demography)
print (L)
print ("workers")
def nonworkers(demo):
    N= sum(demo[0:20])+sum(demo[70:100])
    return N

N=nonworkers(demography)
print (N)
print ("nonworkers")

def next_year(demo):
    for j in range(1,100):
        demo[100-j]=demo[99-j]
    demo[0]= int(workers(demo)/50)    
    return demo
#every year the demography shifts and the newborn dependent on workers
print ("growth rate, output, Capital, Investment, Ration Workers/Nonworkers, citzens")
for i in range(0,50):
    demography=next_year(demography)
    L= workers(demography)
    N=nonworkers(demography)
    O=((1+i/30)*L*M)**0.5 #workers get more qualified 
    I=O-0.5*N-L*(0.5+i/30) #workers consume increases
    
    M=0.9*M+I   #depretiation 10%
    R=(((1+i/30)*L*M)**0.5)/O #growth rate
    print (int(R*1000), int(O), int(M), int(I) , int((L/N)*100), int((sum(demography))))
print (demography)   
