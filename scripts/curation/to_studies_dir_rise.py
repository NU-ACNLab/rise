# -*- coding: utf-8 -*-
import os
import shutil

'''
    Copies foundations participants from /data/RISE to /studies
            Parameters:
                    none
            Returns:
                    none
'''
def mover():
    work_dir = "/projects/b1108/data/RISE/"
    for partic in os.listdir(work_dir):
        if(partic[0:4] == "sub-"):
            wd = work_dir + partic + "/ses-1/"
            for folder in os.listdir(wd): 
             #checks to make sure it's a participant
                try:
                    source = wd + folder
                    print (source)
                    if(folder == "beh"):
                        print("beh")
                        dest = "/projects/b1108/studies/rise/data/raw/neuroimaging/behavioral/"\
                            + partic + "/ses-1/" + folder
                        print(dest)
                        shutil.copytree(source, dest) 
                        print("Copied " + partic + " " + folder)
                    elif("tsv" in folder):
                        dest = "/projects/b1108/studies/rise/data/raw/neuroimaging/bids/"\
                             + partic + "/ses-1/" + folder
                        shutil.copy(source, dest)
                    else:
                        print("other")
                        dest = "/projects/b1108/studies/rise/data/raw/neuroimaging/bids/"\
                             + partic + "/ses-1/" + folder
                        print(dest)
                        shutil.copytree(source, dest) 
                        print("Copied " + partic + " " + folder)
                except:
                    print("Unable to copy " + partic)


def main():   
    mover()


if __name__ == "__main__":
    main()