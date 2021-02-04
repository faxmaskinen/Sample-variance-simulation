#import pandas as pd
import numpy as np
#from collections import Counter
import matplotlib.pyplot as plt
import random
# import time

# Based on Khan Academy - simulations:
# https://www.khanacademy.org/math/ap-statistics/summarizing-quantitative-data-ap/more-standard-deviation/v/simulation-showing-bias-in-sample-variance




### POPULATION - compute N, mean, var
N = 600                 #Populaltion size
pop_list = []
pop_average = None      #Population average
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


# Count occurences (number of y-element) for every x-element
x_nr=[]
y_nr=[]
for i in range(1,7):
    x_nr.append(str(i))
    y_nr.append(pop_list.count(i))



# Graph - bar chart - population
fig, axs = plt.subplots(3, 1)
axs[0].bar(x_nr,y_nr)
axs[0].set_title('Population distribution \n N='+str(N)+', mean='+str(pop_average)+', variance='+str(pop_variance))
axs[0].set_ylabel('Counts')
axs[0].set_xlabel('Value of random variable')


# Population probabilities
tot_y = sum(y_nr)
prob_pop=[]
for i in y_nr:
    prob_pop.append(i/tot_y)

sample_var_list=[]
sample_avg_list=[]
sample_size_list=[]


# Sample from the distribution
number_of_samples= 100
max_sample_size=10

for ii in range(number_of_samples):
    sample_size= random.randrange(2,max_sample_size+1) # sample sizes randomized
    sample_list = []

    for i in range(sample_size):
        sample = np.random.choice(np.arange(1, number_of_bars+1), p=prob_pop)
        sample_list.append(sample)

    sample_array = np.array(sample_list)

    sample_var_list.append(np.var(sample_array))    # sample variance
    sample_avg_list.append(np.mean(sample_array))   # sample average
    sample_size_list.append(sample_size)            # sample size


    # Graph - scatter plot - sample variance vs mean
    axs[1].scatter(sample_avg_list, sample_var_list)
    axs[1].set_title('Sample statistics - Lines are Pop. param.')
    axs[1].axhline(y=pop_variance, color='r', linestyle='-') # population variance
    axs[1].axvline(x=pop_average, color='r', linestyle='-')  # population mean
    axs[1].set_ylabel('Biased Sample Variance')  # sum( (x(i) - x_mean)^2) / n
    axs[1].set_xlabel('Sample mean')

    plt.pause(0.01)

    # Compute sample var / pop variance for every sample size
    avg_sample_var_vs_pop_var = []
    size_nr = []
    for s_size in range(2, max_sample_size+1): # sample sizes
        sample_var_nr_renew=[]
        for a_nr,size in enumerate(sample_size_list):
            if size == s_size:
                sample_var_nr_renew.append(sample_var_list[a_nr])
        if len(sample_var_nr_renew)==0: # no samples for one sample size
            avg_sample_var=0
        else:
            avg_sample_var=np.mean(sample_var_nr_renew)
        avg_sample_var_vs_pop_var.append(avg_sample_var/pop_variance)
        size_nr.append(s_size)

    # Graph - Sample size vs variance
    axs[2].bar(size_nr,avg_sample_var_vs_pop_var)
    axs[2].set_title('Sample Size vs. Variance \n'+ str(number_of_samples)+' samples')
    axs[2].set_ylabel('Biased Sample Var/Pop. var (%)')
    axs[2].set_xlabel('Sample mean')

plt.show()
