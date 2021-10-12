singularity shell --writable-tmpfs --cleanenv \
  -B /projects/b1108/data/BIDS_factory/Temple/data_dump/Alloy_RISE:/base \
  /home/erb9722/heudiconv_0.9.0.sif

singularity exec --writable-tmpfs --cleanenv \
  -B /projects/b1108/data/BIDS_factory/Temple/data_dump/Alloy_RISE:/base \
  /home/erb9722/heudiconv_0.9.0.sif -d /base/Dicom/sub-{subject}/[0-9]/*.dcm \
  -o /base/Nifti/ -f convertall -s 991 -c none --overwrite

# October 12, 2021: Have to figure out how to get heudiconv to ignore junk directory
#https://reproducibility.stanford.edu/bids-tutorial-series-part-2a/#heuman3

# October 12, 2021: Line 8 isn't working (-d flag)
