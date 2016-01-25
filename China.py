#! /usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt

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

print (model.population(), "citizens")
print (model.workers(), "workers")
print (model.nonworkers(), "nonworkers")

growth_data = []
output_data = []
capital_data = []
investment_data = []
ratio_data = []
pop_data = []

#every year the demography shifts and the newborn dependent on workers
print ("Growth rate, Output, Capital, Investment, Ratio workers/nonworkers, Population")
for i in range(0, 200):
    (R, O, M, I, L, N) = model.step()
    pop = model.population()
    ratio = L/N
    print (int(R*1000), int(O), int(M), int(I) , int(ratio*100), int(pop))
    growth_data.append(R)
    output_data.append(O)
    capital_data.append(M)
    investment_data.append(I)
    ratio_data.append(ratio)
    pop_data.append(pop)
print ([int(x) for x in model.demo])

plt.subplot(6,1,1)
plt.plot(growth_data)
plt.ylabel("Growth rate")

plt.subplot(6,1,2)
plt.plot(output_data)
plt.ylabel("Output")

plt.subplot(6,1,3)
plt.plot(capital_data)
plt.ylabel("Capital")

plt.subplot(6,1,4)
plt.plot(investment_data)
plt.ylabel("Investment")

plt.subplot(6,1,5)
plt.plot(ratio_data)
plt.ylabel("Ratio")

plt.subplot(6,1,6)
plt.plot(pop_data)
plt.ylabel("Population")

plt.show()
