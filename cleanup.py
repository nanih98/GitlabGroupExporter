import os
import logging

def clean_files(path):
    logging.info(f"Cleaning files from {path}")
    files = os.listdir(path)
    for file in files:
        os.remove(path+file)