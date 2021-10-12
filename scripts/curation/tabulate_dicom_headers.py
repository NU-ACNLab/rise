### This script creates a csv of the various key parameters in the dicom headers
### for all of the sequences, subjects and sessions
###
### Ellyn Butler
### October 12, 2021

import dicom as dc
import os

sequences = os.listdir()

for seq in sequences:
    seq = dicoms
