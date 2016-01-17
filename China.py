#! /usr/bin/env python

class Model:
    def __init__(self):
        self.M = 900.0 #number of machines or capital
        self.year = 0
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
        self.demo = [self.workers() / 50.0] + self.demo[0:99]
        
    def step(self):
        self.age_demography()
        L = self.workers()
        N = self.nonworkers()
        
        adv = self.year / 30.0
        
        O = ((1+adv)*L*self.M)**0.5 #workers get more qualified 
        I = O*(1-(0.5*N+0.7*L)/(L+N)) #workers consume increases, GDP per capita represented by O/(L+N) 
        
        self.M = 0.9*self.M+I   #depreciation 10%
        R = (((1+adv)*L*self.M)**0.5)/O #growth rate
        
        self.year += 1
        
        return (R, O, self.M, I, L, N)

model = Model()

print model.population(), "citizens"
print model.workers(), "workers"
print model.nonworkers(), "nonworkers"

#every year the demography shifts and the newborn dependent on workers
print ("Growth rate, Output, Capital, Investment, Ratio workers/nonworkers, Population")
for i in range(0, 50):
    (R, O, M, I, L, N) = model.step()
    print int(R*1000), int(O), int(M), int(I) , int((L/N)*100), int(model.population())
print [int(x) for x in model.demo]
