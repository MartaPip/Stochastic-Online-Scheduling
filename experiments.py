import pandas as pd
import numpy as np
import math
import time
from datetime import datetime, timedelta
from bisect import insort_left,insort_right
from tabulate import tabulate
import random
from random import randint
import os
from job_class import Job,Job_b
from run_one import run_one, run_one_both, run_one_both_fast
import pickle
from convert import convert_all 
from analysis import make_plot
from run_experiment import run_experiment


instances=50
realizations_p=50
Distributions=["d_uniform","exponential","log_normal","deterministic"]
NP=[10,20,50,100,200,500,1000]
MP=[1,2,5,10]
N=[10,20,50,100,200,500,1000]
M=[1,2,5,10]
golden_ratio=( 1 + math.sqrt(5) ) / 2

upper_we=30
time_step=1
Printing=False



################################################ adapt parameters for simulations################################################
Distributions=["exponential"]
#simulation parametrs
N=[10,20,50,100,200,500,1000]
M=[1,2,5,10]
alpha_DSOS=golden_ratio-1
Delta_try=10
upper_release_par=5
fixed_release_par=False
#type="asymptotic"
type="standard"
ratio="max"

#plot parameters
MP=M
NP=N
#NP=[10,20,50,100,200,500,1000]
#MP=[1,2,5,10]

################################################################################################################################################
for distribution in Distributions:
    for m in M:
        for n in N:
            run_experiment(m,n,distribution,alpha_DSOS,fixed_release_par,upper_release_par,upper_we,instances,realizations_p,Delta_try)
            print(f"finished for distribution {distribution} withe {m} machines and {n} jobs")
 
convert_all(fixed_release_par,upper_release_par,NP,MP,Distributions,type,ratio,alpha_DSOS,Delta_try)
for distribution in Distributions:
    for method in ["DSOS","RSOS"]:
        make_plot(NP,MP,distribution,method, fixed_release_par,upper_release_par,alpha_DSOS, Delta_try)





''''
#N=[10,20,50,100,200,500,1000,2000]
for distribution in Distributions:
    for method in ["DSOS","RSOS"]:
        if method=="DSOS": N=[10,20,50,100,200,500,1000]
        elif distribution=="log_normal": N=[10,20,50,100,200,500,1000,2000]
        else: N=[10,20,50,100,200,500,1000,2000,5000]
        if type=="asymptotic": make_plot_asymptotic(distribution,method, fixed_release_par,upper_release_par,alpha_DSOS, Delta_try)
        else: make_plot(N,M,distribution,method, fixed_release_par,upper_release_par,alpha_DSOS, Delta_try)

###############################################
'''

'''''
###############################################
N=[10,20,50,100,200,500,1000]
upper_release_par=0
fixed_release_par=False
print("now case:upper_release_par,type:",upper_release_par,fixed_release_par)
for distribution in Distributions:
    for m in M:
        for n in N:
            run_experiment(m,n,distribution,alpha_DSOS,fixed_release_par,upper_release_par,upper_we,instances,realizations_p,Delta_try)
            print(f"finished for distribution {distribution} withe {m} machines and {n} jobs")


convert_all(fixed_release_par,upper_release_par,N,M,Distributions,type,ratio,alpha_DSOS,Delta_try)

for distribution in Distributions:
    for method in ["DSOS","RSOS"]:
        if type=="asymptotic": make_plot_asymptotic(distribution,method, fixed_release_par,upper_release_par,alpha_DSOS, Delta_try)
        else: make_plot(N,M,distribution,method, fixed_release_par,upper_release_par,alpha_DSOS, Delta_try)

#

'''

