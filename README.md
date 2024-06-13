# Deploying Mobility-On-Demand for All by Optimizing Paratransit Services

This repository describes the results of the code and the data for the following paper: [https://smarttransit.ai/files/sivagnanam2022offline.pdf](https://scopelab.ai/files/paviaIJCAI24AISG.pdf
### ABSTRACT

*While on-demand ride-sharing services have become popular in recent years, traditional on-demand transit services cannot be used by everyone, e.g., people who use wheelchairs. Paratransit services, operated by public transit agencies, are a critical infrastructure that offers door-to-door transportation assistance for individuals who face challenges in using standard transit routes. However, with declining ridership and mounting financial pressure, public transit agencies in the USA struggle to operate existing services. We collaborate with a public transit agency from the southern USA, highlight the specific nuances of paratransit optimization, and present a vehicle routing problem formulation for optimizing paratransit. We validate our approach using real-world data from the transit agency, present results from an actual pilot deployment of the proposed approach in the city, and show how the proposed approach comprehensively outperforms existing approaches used by the transit agency. To the best of our knowledge, this work presents one of the first examples of using open-source algorithmic approaches for paratransit optimization. *

### ACKNOWLEDGEMENT

This material is based upon work sponsored by the National
Science Foundation under Grant CNS-1952011 and by the
Department of Energy under Award DE-EE0009212.

**Disclaimer**: Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not
necessarily reflect the views of the National Science Foundation or the Department of Energy.

### Directories

[algo](algo):
contains implementation of,
#### Our Algorithms
1. [Online Solver](algo/)
2. [Offline Solver](algo/)


####  Wrapper for other existing baselines
1. [Google or-tools](https://developers.google.com/optimization)

[base](base): contains the custom implementation to solve the para-transit optimization problem.

[common](common): constants and common utilities shared by source files in other folders ([algo](algo), [base](base)).

[data](data): contains the all data to run paratransit sample instances.


#### Data Folder Description:
**Main Input Data**

#### EVALUATION

I) Normal Environment Setup (supports Linux and MacOSX):

Please make sure the following before executing the scripts
1. python 3.8
2. Install all modules listed in "requirements.txt" (using the command pip install -r requirements.txt).
  
Sample Execution:

1. Greedy Algorithm

```bash
python3 run_optimizer.py --algo=greedy --date=0
```

6. Google OR-Tools Routing

```bash
python3 run_optimizer.py --algo=routing --date=0
```
