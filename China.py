#! /usr/bin/env python

class Model:
    def __init__(self):
        self.M = 900 #number of machines or capital
        #The value on position n represents the number of people of age n in society 
        self.demo = [
            5,5,5,5,5,5,5,5,5,5,
            5,5,5,5,5,5,5,5,5,5,
            10,10,10,10,10,10,10,10,10,10,
            10,10,10,10,10,10,10,10,10,10,
            10,10,10,10,10,10,10,10,10,10,
            10,10,10,10,10,10,10,10,10,10,
            10,10,10,10,10,10,10,10,10,10,
            5,5,5,5,5,5,5,5,5,5,
            5,5,5,5,5,5,5,5,5,5,
            5,5,5,5,5,5,5,5,5,5
            ]

    def population(self):
        return sum(self.demo)
        
    def workers(self):
        return sum(self.demo[20:70])

    def nonworkers(self):
        return self.population() - self.workers()

    def age_demography(self):
        self.demo = [int(self.workers() / 50)] + self.demo[0:99]
        
    def step(self):
        self.age_demography()
        L = self.workers()
        N = self.nonworkers()
        
        O = ((1+i/30)*L*self.M)**0.5 #workers get more qualified 
        I = O-0.5*N-L*(0.5+i/30) #workers consume increases
        
        self.M = 0.9*self.M+I   #depretiation 10%
        R = (((1+i/30)*L*self.M)**0.5)/O #growth rate
        
        return (R, O, self.M, I, L, N)

model = Model()

print model.population(), "citizens"
print model.workers(), "workers"
print model.nonworkers(), "nonworkers"

#every year the demography shifts and the newborn dependent on workers
print ("growth rate, output, Capital, Investment, Ration Workers/Nonworkers, citzens")
for i in range(0, 50):
    (R, O, M, I, L, N) = model.step()
    print int(R*1000), int(O), int(M), int(I) , int((L/N)*100), int(model.population())
print model.demo
