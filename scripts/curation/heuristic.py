### This heuristic curates the Rise and Crest projects into BIDS
###
### Ellyn Butler
### October 12, 2021

import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


# Create Keys
t1w = create_key(
   'sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
t2w = create_key(
   'sub-{subject}/{session}/anat/sub-{subject}_{session}_T2w')

# Field maps
b0_mag_single_phasediff = create_key(
   'sub-{subject}/{session}/fmap/sub-{subject}_{session}_magnitude{item}')
b0_phase_single = create_key(
   'sub-{subject}/{session}/fmap/sub-{subject}_{session}_phasediff')

b0_mag_multi_phasediff = create_key(
   'sub-{subject}/{session}/fmap/sub-{subject}_{session}_magnitude{item}')
b0_phase_multi = create_key(
   'sub-{subject}/{session}/fmap/sub-{subject}_{session}_phase{item}')


# fmri scans
rest_bold_100 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_acq-100_bold')
rest_bold_124 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_acq-singleband_bold')
rest_bold_204 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_acq-singleband_bold')
dwi_run1 = create_key(
    'sub-{subject}/{session}/dwi/sub-{subject}_{session}_run-01_dwi')
dwi_run2 = create_key(
    'sub-{subject}/{session}/dwi/sub-{subject}_{session}_run-02_dwi')
frac2back = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-frac2back_bold')
go2back = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-go2back_bold')
hero = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-hero_bold')
demo = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_task-idemo_bold')
#
## ASL scans
asl = create_key(
   'sub-{subject}/{session}/asl/sub-{subject}_{session}_asl')
#asl_dicomref = create_key(
#   'sub-{subject}/{session}/asl/sub-{subject}_{session}_acq-ref_asl')
m0 = create_key(
   'sub-{subject}/{session}/asl/sub-{subject}_{session}_m0')
#mean_perf = create_key(
#   'sub-{subject}/{session}/asl/sub-{subject}_{session}_mean-perfusion')


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_run-00{item:01d}_T1w')

    info = {t1w: []}

    for idx, s in enumerate(seqinfo):
        if (s.dim1 == 320) and (s.dim2 == 320) and ('t1_fl2d_tra' in s.protocol_name):
            info[t1w].append(s.series_id)
    return info

# Specify which niftis will be used for distortion correction (key), and which images
# they are correcting distortion for (value: list)
IntendedFor = {

}
