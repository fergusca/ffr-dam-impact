#!/bin/bash

jupyter nbconvert --to notebook --inplace --execute code/blog-final.ipynb
jupyter nbconvert --to html --no-input --output-dir='./outputs' --execute code/blog-final.ipynb 