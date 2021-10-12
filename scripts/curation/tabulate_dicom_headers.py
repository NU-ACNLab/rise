### This script creates a csv of the various key parameters in the dicom headers
### for all of the sequences, subjects and sessions
###
### Ellyn Butler
### October 12, 2021

import pydicom #https://github.com/pydicom/pydicom
import os
#import subprocess
import pandas as pd

project_dir = '/projects/b1108/data/BIDS_factory/Temple/data_dump/Alloy_RISE'
subject_dirs = os.popen('find '+project_dir+' -name "sub-*"').read().split("\n")[:-1]
#subject_dirs = [sub.replace('\n', '') for sub in subject_dirs]

param_dict = {
    'subject':[],
    'session':[],
    'scandate':[],
    'EchoNumbers':[],
    'EchoTime':[],
    'FlipAngle':[],
    'InPlanePhaseEncodingDirection':[],
    'Modality':[],
    'ProtocolName':[],
    'RepetitionTime':[],
    'SequenceName':[],
    'SliceThickness':[]
}

for sub_dir in subject_dirs:
    sequences = os.popen('ls '+sub_dir).read().split("\n")[:-1]
    # Skip 99, not a real sequence?
    sequences = [seq for seq in sequences if '99' not in seq]
    for seq in sequences:
        dcm_path = os.popen('find '+sub_dir+'/'+seq+'/ -name "*.dcm"').read().split("\n")[1]
        dcm = pydicom.dcmread(dcm_path)
        sub = sub_dir.split('/')[-1]
        param_dict['subject'].append(sub)
        param_dict['session'].append('NA') #Will have to be changed once we have a session naming convention
        param_dict['scandate'].append(dcm.AcquisitionDate)
        param_dict['EchoNumbers'].append(dcm.EchoNumbers)
        param_dict['EchoTime'].append(dcm.EchoTime)
        param_dict['FlipAngle'].append(dcm.FlipAngle)
        #param_dict['ImageType'].append(dcm.ImageType)
        if hasattr(dcm, 'InPlanePhaseEncodingDirection'):
            param_dict['InPlanePhaseEncodingDirection'].append(dcm.InPlanePhaseEncodingDirection)
        else:
            param_dict['InPlanePhaseEncodingDirection'].append('NA')
        param_dict['Modality'].append(dcm.Modality)
        param_dict['ProtocolName'].append(dcm.ProtocolName)
        param_dict['RepetitionTime'].append(dcm.RepetitionTime)
        param_dict['SequenceName'].append(dcm.SequenceName)
        param_dict['SliceThickness'].append(dcm.SliceThickness)

param_df = pd.DataFrame.from_dict(param_dict)
param_df.to_csv('', index=False)

unique_param_df = param_df.drop('subject', 1).drop('session', 1).drop('scandate', 1).drop_duplicates()
unique_param_df.to_csv('',index=False)
