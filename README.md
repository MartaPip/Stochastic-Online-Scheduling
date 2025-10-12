# *Stochastic Online Scheduling on Identical Parallel Machines* 


## Description
This repository contains the code written for the master thesis "Stochastic Online Scheduling on Parallel Machines: Theoretical Analysis and Computational Study on the Performance Guarantees of Deterministic and Randomized Algorithms"

In this work, we address the stochastic online scheduling problem of minimizing the expected total weighted completion time on identical parallel machines. Building on Schulz’s previous work, we finalize the proofs of the performance guarantees of the algorithms developed in the paper "Stochastic Online Scheduling Revisited”[1] and we refine the guarantee for the deterministic algorithm when considering a fixed number of machines. We demonstrate that the randomized algorithm (RSOS) and the deterministic algorithms (DSOS) have performance ratios of $2+\Delta$ and $\max\left\\{2.618, 2.309+1.309\Delta -\frac{0.691}{m}\right\\}$, respectively, where $\Delta$ is an upper bound on the squared coefficient of variation of the processing times. Notably, these guarantees are the tightest ones for the problem with generic processing time distributions. 

To evaluate the performance of the RSOS and DSOS algorithms in practise, we conduct a computational study on simulated data. The implementation was partially inspired by the work of M. Buchem and T. Vredeveld[2]. For the DSOS algorithm, we consider $\max\left\\{2.618, 2.309+1.309\Delta\right\\}$ as the theoretical gurantee since it holds for any number of machines.

Additional details on the theoretical analysys and on the implementation can be found in the thesis.


## Setup

```bash

git clone git@github.com:MartaPip/Stochastic-Online-Scheduling.git

cd Stochastic-Online-Scheduling

conda env create -f environment.yml

conda activate Tesi_env

```

## Running the experiments

To run the experiments, adjust the following parameters in the *experiments.py* file and execute it:

### Usually fixed parameters:

- **N=[10,20,50,100,200,500,1000]** Array specifying the number of jobs to consider in the simulations.

- **M=[1,2,5,10]** Array specifying the number of machines to consider in the simulations.

- **Distributions=["d_uniform","exponential","log_normal","deterministic"]** List specifying the distributions of the jobs' processing times to consider in the simulations.

- **Delta_try** Upper bound on the coefficient of variation that is considered when running simulations with the log-normal distribution. The default value is 10.

- **upper_mean** Upper bound on the expected value of the jobs' processing times. 

- **upper_we** Upper bound on the weights of the jobs.

- **instances** Number of instances simulated for each scenario. 

- **realizations_p** Number of realizations of the processing times simulated for each instance.

- **alpha_DSOS** Value of $\alpha$ considered in the $DSOS$ algorithm, by default it is *golden ratio* $-1$.



### Parameters to select release time conditions:

- **fixed_release_par** A Boolean parameter (True or False) indicating whether the upper bound of the job's release time depends on the number of jobs considered.

- **Tigth_analysis**  A Boolean parameter (True or False) indicating whether the upper bound of the release time of the jobs depends on the number of machines considered.

- **upper_release_par**  If *Tigth_analysis* is True, the upper bound on the release time is calculated as upper_release_par $\times$ upper_we $\times \frac{n}{2m}$.  If *Tigth_analysis* is Fasle and *fixed_release_par* is True, *upper_release_par* specifies the upper bound on the release time. Otherwise, the upper bound is calculated as $n \times$ upper_release_par.

### Summary tables and plot characteristics parameters:

- **Summary $\in$ {"Worst", "Average", "Both"}** A string indicating if the summary table of the scenario contains the worst results among the instances, the average one, or both.

- **Plot_Worst** A Boolean parameter (True or False) indicating whether the plot illustrates the highest ratio among the instances. When it is False, the average ratio across the instances is considered.


## Outputs

- **run_experiment**: Runs a simulation for a combination of input parameters. Creates a table containing the objective values of the DSOS and RSOS algorithms, as well as two lower bounds on the optimal solutions for each instance and realization of the processing times. The table's dimensions are (*instances* , *realizations_p* ).
  
- **convert_all_both**: Takes the tables created by *run_experiment* and outputs a summary table for each distribution and algorithm. In every summary-table cell, corresponding to different combinations of the values in N and M, the average or the worst-case ratios among the instances are represented.
  
- **make_plot**: Takes a summary table created by convert_all_both to generate plots of the worts-case or the average ratio against the number of jobs for each number of machines setting.



## Source
[1] A. S. Schulz. “Stochastic Online Scheduling Revisited”. In: Combinatorial Optimization and Applications. Ed. by B. Yang, D.-Z. Du, and C. A. Wang. Berlin, Heidelberg: Springer Berlin Heidelberg, 2008, pp. 448–457. 

[2] M. Buchem and T. Vredeveld. “Performance analysis of fixed assignment policies for stochastic online scheduling on uniform parallel machines”. In: Computers & Operations Research 125 (2021), p. 105093



