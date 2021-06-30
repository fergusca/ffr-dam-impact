#!/bin/bash

jupyter nbconvert --to notebook --inplace --execute code/02_dam_river_flow_analysis_blog.ipynb
jupyter nbconvert --to html --no-input --output-dir='./outputs' --execute code/02_dam_river_flow_analysis_blog.ipynb