# -*- coding: utf-8 -*-
import os
import json
import csv

def find_dates():
    csv_file = "/projects/b1108/studies/rise/scripts/rise-crest-qc-log.csv"
    partic_list = {}
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #skip header
        next(reader, None) 
        for row in reader:
            partic_id = row[0]
            if(not partic_id in partic_list.keys()):
                partic_list[partic_id] = row[1]   
    return partic_list


def scans_to_file(partic, date, log_file):
    #set working dir
    work_dir = "/projects/b1108/data/RISE/sub-" + partic \
                + "/ses-1/"
    #open file:
    log_file_path = work_dir + log_file
    with open(log_file_path, 'w') as logfile: 
        file.write("filname\tacq_time\n")
        #iterate through scans and add line to .tsv file
        for scan in os.listdir(work_dir):
            for file in (work_dir + scan):   
                #check to make sure it's a .json
                if(file.split(".")[1] == "json"):      
                    print(work_dir + scan + '/' + file)
                    # Opening JSON file
                    f = open(work_dir + scan + '/' + file)
                    # returns JSON object as dict
                    data = json.load(f)
                    # Get aquisition time
                    time = data['AcquisitionTime']
                    # Closing file
                    f.close()
                    #FORMAT
                    #filname tab acq_time
                    # scan/filename tab YYYY-MM-DDTHH:mm:SS
                    # need to create this file at ses-1 folder level
                    #write to output file
                    datetime = date + "T" + time.split(".")[0]
                    line = scan + "/" + file + "\t" + datetime + "\n"
                    file.write(line)
        file.close()

def main(): 
    pd_dict = find_dates()
    for partic, date in pd_dict.items():
        #format = sub-####_ses-1_scans.tsv
        file = "sub-" + partic + "_ses-1_scans.tsv"
        scans_to_file(partic, date, file)



if __name__ == "__main__":
    main()