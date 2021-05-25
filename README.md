# Dam Impacts on Global River Connectivity
[![DOI](https://zenodo.org/badge/368339473.svg)](https://zenodo.org/badge/latestdoi/368339473)

This repository is for a research project, in partnership with the WWF (Jeff Opperman, Natalie Sharbol), focused on understanding and examining the impact of dams on the Connectivity Status Index of Free Flowing Rivers on a global scale. 
## Background/ Purpose
Only a third of the world’s large rivers still have their free-flowing status and dams are the primary cause of this loss in river connectivity. However, we have a poor understanding of whether different dam purposes (e.g., hydroelectric, water supply) affect river connectivity differently and whether these relationships vary across regional settings. 
## Goals
For this project, we seek to examine patterns among dam purpose and metrics of river connectivity across the globe. We will compile global datasets on dam infrastructure and river hydro-geometric and connectivity properties to quantify relationships of dam impacts on river connectivity.  We will conduct a pilot study examining relationships in Africa to develop the project methodologies and workflow that can be scaled up to the globe.  
## Unique Contribution
The spatial join of Global Reservoir and Dam dataset (GRanD) and World’s Free-Flowing Rivers datasets (FFR)
## Use
This repository could be used for future projections on how dams might change a river or how dam removal may benefit a river. 
# How to Run
## Tools/ Packages
* numpy
* pandas
* matplotlib
* math
* fiona
* geopandas
* rasterio
* requests
* seaborn
* zipfile
* earthpy
* urllib.request
* warnings
## Data Used
<a href="http://globaldamwatch.org/grand/" target="_blank">GRanD Dataset</a>
* “Global River and Dam Database” (GRanD) Lehner, B., C. R. Liermann, C. Revenga, and others. 2011. High-resolution mapping of the world’s reservoirs and dams for sustainable river-flow management. Frontiers in Ecology and the Environment 9: 494–502. doi:10.1890/100125
*Provides vector point locations for  7320 total recorded dams and reservoirs around the world as point shapefiles.

<a href="https://doi.org/10.6084/m9.figshare.7688801" target="_blank">FFR Dataset</a>
* “Mapping the world's free-flowing rivers Geodatabase” (FFR) Grill, G., B. Lehner, M. Thieme, and others. 2019. Mapping the world’s free-flowing rivers. Nature 569: 215–221. doi:10.1038/s41586-019-1111-9
* The dataset consists of a geometric network of the global river system and associated attributes, such as hydro-geometric properties, as well as connectivity metrics calculated using the methodologies described in the research article.
## Run Workflow
1. Clone the repository https://github.com/krantz23/ffr-dam-impact, or download and decompress the zip file (see the green button for Clone or download).
2. Open a terminal and change directories to this directory (cd ffr-dam-impact).
3. Follow steps in *Required Installations* (below)
3. Launch Jupyter Notebook and open desired exploration or final notebook from the notebooks sub-directory.
4. Make sure you have downloaded and extracted the GRanD dataset manually from <a href="http://globaldamwatch.org/grand/" target="_blank">GRanD Dataset</a>
5. Change the GRanD file path in the desired notebook to your GRand Dataset.
6. In the notebook, Run All Cells.

* In order to run all packages, we used the Earth Data Analytics python environment.
* currently there is only one notebook “fergus-pinke-rantz-to-submit.ipynb”(a midterm blog post).

Or, run Bash script
1. Activate workflow environment

'$ conda activate ffr-dam-env'
2. Make sure you are in the correct directory

'$ cd ffr-dam-impact'
3. Run bash script

'$ .main.sh'

## Required Installations
Install the environment.yml on your Local Computer.
About Conda Environments: https://conda.io/docs/user-guide/tasks/manage-environments.html

To install the environment in your Anaconda installation, run the following in the Terminal:

conda env create -f environment.yml

Note that it takes a bit of time to run this setup Also note that for the code above to work, you need to be in the directory where the environment.yml file lives.

To activate this environment once it has been installed, run the following in the Terminal: On Windows, Mac, and Linux: conda activate environment
## Example Usage
Others can use the commands in this repository to link the GRanD and FFR datasets to look at other relationships among dam attributes (e.g., dam height, dam age) and river connectivity characteristics. The code is specific to the GRanD and FFR geospatial shapefile datasets, however, if these datasets are updated over time or dam and river data are available from other sources it would be possible to adapt the notebooks to perform similar analyses. One could also feasibly use other vector point file dam location datasets along with hydrology datasets to run similar analysis.
