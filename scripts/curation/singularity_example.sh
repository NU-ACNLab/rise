singularity pull docker://nipy/heudiconv:0.9.0

ingularity shell --writable-tmpfs --cleanenv \
  -B /projects/b1108/data/BIDS_factory/Temple/data_dump/Alloy_RISE:/base \
  /home/erb9722/heudiconv_0.9.0.sif

singularity run --writable-tmpfs --cleanenv \
  -B /projects/b1108/data/BIDS_factory/Temple/data_dump/Alloy_RISE:/base \
  /home/erb9722/heudiconv_0.9.0.sif -d /base/Dicom/sub-{subject}/*/*.dcm \
  -o /base/Nifti/ -f convertall -s 991 -c none --overwrite

#https://reproducibility.stanford.edu/bids-tutorial-series-part-2a/#heuman3

# October 12, 2021: Line 8 isn't working (-d flag)
# October 24, 2021: 0.9.0 works when running from within the container... odd
