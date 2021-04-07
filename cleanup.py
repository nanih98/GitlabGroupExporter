import os, glob
import logging

def clean_files(path):
    logging.info(f"Cleaning files from {path}")
    files = glob.glob(path+'*.tar.gz')
    
    for file in files:
        os.remove(file)