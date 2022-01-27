### This script tabulates data from the jsons into a csv
###
### Ellyn Butler & Nina Kougan
### January 27, 2022

import pandas as pd
import os
import glob

mriqc_dir = '/projects/b1108/projects/georgia/mriqc_checked/'
mriqc_jsons = os.listdir(glob.glob(mriqc_dir + '*/*/*/*.json'))

# Follow first example here:
# https://towardsdatascience.com/the-python-glob-module-47d82f4cbd2d

# Final csv should contain all key-value pairs in all jsons, and columns
# called "subid" and "sesid"
