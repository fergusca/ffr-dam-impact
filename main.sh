#!/bin/bash

jupyter nbconvert --to notebook --inplace --execute code/fergus-pinke-rantz-to-submit.ipynb
jupyter nbconvert --to html --no-input --output-dir='./outputs' --execute code/fergus-pinke-rantz-to-submit.ipynb 