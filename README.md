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

[notebooks](notebooks):
contains implementation of:
#### Our Solvers
1. [Online Solver](notebooks/online.ipynb)
2. [Offline Solver](notebooks/offline.ipynb)


####  Other Directories and files
1. [Google or-tools](https://developers.google.com/optimization)

[data](data): contains the all data to run paratransit sample instances. Please note this is synthetic data, and not the real-world data used in the paper for privacy purposes. 

[core](core): contains the functionality related to working with the OSRM server

[bin](bin): contains script to start osrm server

[config](config.py) : contains the configuration parameter for the solvers and OSRM server


#### Set Up

I) Normal Environment Setup (supports Linux and MacOSX):

Please make sure the following before executing the scripts and notebooks
1. python 3.11.9
2. Install all modules listed in "requirements.txt" (using the command pip install -r requirements.txt).
3. Generate .env with OSRM_HOST and OSRM_PORT
4. Set up OSRM Server

Currently, we are running a single OSRM server. The optimizers rely on an OSRM server. Server should have about 16GB of RAM.

If you want to build and push a new image the process and code is located at 
[smarttransit-osrm-backend](https://github.com/smarttransit-ai/smarttransit-osrm-backend/tree/paratransit_software)
which is the `smarttransit-osrm-backend` repository under the `paratransit_software` branch. README.md at that 
location details that process.

Start OSRM Server:

```bash
source .env
bash bin/osrmserverrun.sh
# test the OSRM server
curl "http://$OSRM_HOST:$OSRM_PORT/table/v1/driving/-86.79426670074463,36.12473806954196;-86.7641830444336,36.13808266878191"
```
  
