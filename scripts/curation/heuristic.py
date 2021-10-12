### This heuristic curates the Rise and Crest projects into BIDS
###
### Ellyn Butler
### October 12, 2021

import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


##### Create Keys
# Structural
t1w = create_key(
   'sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w') #                                   t1_mpg_sag_0.8iso

# Field maps
# Case 4: https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html
mid_dirAP_run1 = create_key(
    'sub-{subject}/{session}/fmap/sub-{subject}_{session}_task-mid_dir-AP_run-1_phasediff') #cmrr_MID_AP_run-1

# fMRI
mid_dirPA_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-mid_dir-PA_run-1_bold') #              cmrr_MID_run-1
mid_dirPA_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-mid_dir-PA_run-2_bold') #              cmrr_MID_run-2
chat_dirPA = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-chat_dir-PA_bold') #              cmrr_chat_run-1

# Build lists of sequences
def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    info = {t1w: [], mid_dirAP_run1: [], mid_dirPA_run1: [], mid_dirPA_run2: [],
        chat_dirPA: []}

    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 320) and (s.dim2 == 320) and ('t1_fl2d_tra' in s.protocol_name):
            info[t1w].append(s.series_id)
    return info

# Specify which niftis will be used for distortion correction (key), and which images
# they are correcting distortion for (value: list)
IntendedFor = {
    mid_dirAP_run1: [
        'sub-{subject}/{session}/func/sub-{subject}_{session}_task-mid_dir-PA_run-1_bold',
        'sub-{subject}/{session}/func/sub-{subject}_{session}_task-mid_dir-PA_run-2_bold',
        'sub-{subject}/{session}/func/sub-{subject}_{session}_task-chat_dir-PA_bold'
    ]
}
