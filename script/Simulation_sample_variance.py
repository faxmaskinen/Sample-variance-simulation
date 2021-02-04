import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import random
import time

# print('hello')

##### todo ###
# create random creation of distribution calc N, mean, variance of population
# take samples of si


### POPULATION - compute N, mean, var
N = 600
pop_list = []
pop_average = None

number_of_bars =6

prob_pop_distr=[]
for i in range(1,number_of_bars+1):
    n = random.randint(1,30)
    prob_pop_distr.append(n)
prob_pop_distr = [x / sum(prob_pop_distr) for x in prob_pop_distr]

for i in range(N):
    pop = np.random.choice(np.arange(1, number_of_bars+1), p=prob_pop_distr)
    pop_list.append(pop)
pop_array = np.array(pop_list)

pop_variance = np.var(pop_array)
pop_average = np.mean(pop_array)
print("N","pop avg"," pop variance" )
print(N,round(pop_average,2), round(pop_variance,2))

## count occurence, prepare for bar chart
x_nr=[]
y_nr=[]
for i in range(1,7):
    x_nr.append(str(i))
    y_nr.append(pop_list.count(i))

# print(x_nr,y_nr)

### graph - bar chart population
fig, axs = plt.subplots(3, 1)
axs[0].bar(x_nr,y_nr)
axs[0].set_title('population distr')

# fig1 = plt.figure(1)
# ax = fig1.add_axes([0,0,1,1])
# ax.bar(x_nr,y_nr)


#### population probabilities
tot_y = sum(y_nr)
prob_pop=[]
for i in y_nr:
    prob_pop.append(i/tot_y)

# print(prob_pop)
sample_var_list=[]
sample_avg_list=[]
sample_size_list=[]


for ii in range(100):
    sample_size= random.randrange(2,11) # sample sizes
    sample_list = []
    sample_average = None
    for i in range(sample_size):
        sample = np.random.choice(np.arange(1, number_of_bars+1), p=prob_pop)
        sample_list.append(sample)

    sample_array = np.array(sample_list)
    sample_variance = np.var(sample_array)
    sample_average = np.mean(sample_array)

    sample_var_list.append(sample_variance)
    sample_avg_list.append(sample_average)
    sample_size_list.append(sample_size)

# print(sample_var_list)
# print(sample_avg_list)
# print(sample_size_list)


    ### graph - scatter - sample variance
    axs[1].scatter(sample_avg_list, sample_var_list)
    axs[1].set_title('sample variance vs average')
    axs[1].axhline(y=pop_variance, color='r', linestyle='-')
    axs[1].axvline(x=pop_average, color='r', linestyle='-')
    plt.pause(0.1)

    ### compute sample size vs variance

    sample_avg_var = []
    size_nr = []
    for i in range(2, 11):
        sample_var_nr_renew=[]
        for a,size in enumerate(sample_size_list):
            if size == i:
                print(a,size, sample_var_list[a])
                sample_var_nr_renew.append(sample_var_list[a])
        if len(sample_var_nr_renew)==0:
            avg_var=0
        else:
            avg_var=np.mean(sample_var_nr_renew)
        sample_avg_var.append(avg_var/pop_variance)
        size_nr.append(i)
    # print(size_nr)
    # print(sample_avg_var)


    ### graph - sample size vs variance
    axs[2].bar(size_nr,sample_avg_var)
    axs[2].set_title('sample size vs variance')



plt.show()
