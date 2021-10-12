### This script takes the zipped files and puts them into subject/session/sequence
### structure.
###
### Ellyn Butler
### October 12, 2021

projectdir=/projects/b1108/data/BIDS_factory/Temple/data_dump/Alloy_RISE
zips=`find ${projectdir} -name "*.zip"`

for zip in zips; do
  unzip ${zip}
  subid=`find ${projectdir} -maxdepth 1 -name "ALLOY-RISE-*" | cut -d "-" -f 3`
  mv ${projectdir}/ALLOY-RISE-${subid} ${projectdir}/sub-${subid}
  seqdirs=`ls ${projectdir}/sub-${subid}`
  for seqdir in ${seqdirs}; do
    mv ${projectdir}/sub-${subid}/${seqdir}/DICOM/* ${projectdir}/sub-${subid}/${seqdir};
    rm -r ${projectdir}/sub-${subid}/${seqdir}/DICOM
  done
done
