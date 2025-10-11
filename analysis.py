import pandas as pd
import matplotlib.pyplot as plt
import os
import math
import seaborn as sns


def make_plot(N,M,distribution,mean,method, Tigth_analysis,fixed_release_par,upper_release_par,upper_we, Worst, alpha=(( 1 + math.sqrt(5) ) / 2), Delta_try=10):
    ###############################################################################################################################
    ####################################################INPUT:#####################################################################
    #N                 = list with numbers of jobs 
    #M                 = list with numbers of machines 
    #distribution      = processing time distribution in the simulation 
    #mean              = upper bound on mean of the processing time distribution
    #method            = algorithm considered "DSOS" or "RSOS"
   

    #Tigth_analysis    = TRUE if the upper bound on the release times depends on m
    #fixed_release_par = TRUE if the upper bound on the release times is independent from m and n
    #upper_release_par = parameter influencing upper bound on release time
    #upper_we          = upper bound on jobs' weights
    #Worst             = TRUE if worst-case ratio is considered, FALSE if average ratio is considered
    #Delta_try=10      = parameter influencing the coefficient of variation for the log-normal distribution
    #alpha             = fixed value alpha in the DSOS algorithm, usually golden_ratio-1


    ####################################################OUTPUT:#####################################################################
    # Plots performance ratio vs  number of job for each machine
    ################################################################################################################################
    
    #Find path to data & compute theoretical bound
    fix="n"
    if fixed_release_par: fix="fix"
    if Tigth_analysis:fix="mn_dependent_"
    if Worst: 
         path=os.path.join("Results",f"results_{fix}{upper_release_par}_mean_{mean}_we_{upper_we}","summary","WORST")
         save_folder = os.path.join("Results",f"results_{fix}{upper_release_par}_mean_{mean}_we_{upper_we}","plots","WORST")
    else:
         path=os.path.join("Results",f"results_{fix}{upper_release_par}_mean_{mean}_we_{upper_we}","summary")
         save_folder = os.path.join("Results",f"results_{fix}{upper_release_par}_mean_{mean}_we_{upper_we}","plots")

    if distribution=="d_uniform": 
         CV=1/3
         name_distribution="Uniform"
    if distribution=="exponential":
         CV=1
         name_distribution="Exponential"
    if distribution=="log_normal":
                sigma2=math.log(Delta_try+1)
                CV=math.exp(sigma2)-1
                CV=round(CV)
                name_distribution="Log-normal"
    if distribution=="deterministic":
         CV=0
         name_distribution="Deterministic"

    
    if method=="DSOS":
        predicted=max(1+((2+alpha)*(CV+1)/2),2+alpha)
        if Worst:  name_DSOS=f"{distribution}_DSOS_{round(CV,2)}_Worst.csv"
        else: name_DSOS=f"{distribution}_DSOS_{round(CV,2)}.csv"
        data=pd.read_csv(os.path.join(path,name_DSOS))

    if method=="RSOS":
        predicted=2+CV
        if Worst:  name_RSOS=f"{distribution}_RSOS_{round(CV,2)}_Worst.csv"
        else: name_RSOS=f"{distribution}_RSOS_{round(CV,2)}.csv"
        data=pd.read_csv(os.path.join(path,name_RSOS))
    
    color_palette = sns.color_palette("colorblind")

    #crate plot
    for index, row in data.iterrows():
        selected_columns = [str(n) for n in N if str(n) in row.index]
        plt.plot( pd.to_numeric(selected_columns), row[selected_columns], label=f"m= {round(row.iloc[0])}", marker='o',color=color_palette[index]) #label=f"m={row['m']}"
        #pd.to_numeric(row.index[1:])
    plt.axhline(y=predicted, color='red', linestyle='--', label='Theoretical guarantee')
    plt.legend()
    plt.xlabel('number of jobs')
    plt.ylabel('performance ratio')
    if Worst: 
        if name_distribution=="Deterministic": plt.title(f"Worst case performance {method} for {name_distribution} Setting ")
        else: plt.title(f"Worst case performance {method} for {name_distribution} Distribution ")
    else: 
        if name_distribution=="Deterministic": plt.title(f"Performance {method} for {name_distribution} Setting ")
        else: plt.title(f"Performance {method} for {name_distribution} Distribution ")

    #plt.show()


    # Create the folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Save the plots to the specified folder
    if Worst: plt.savefig(os.path.join(save_folder, f"{distribution}_{method}_{round(CV,2)}_Worst.png"))
    else: plt.savefig(os.path.join(save_folder, f"{distribution}_{method}_{round(CV,2)}.png"))
    plt.close()
