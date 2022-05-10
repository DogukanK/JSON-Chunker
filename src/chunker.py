#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Dogukan E. Kurnaz
# Created Date: 04/05/2022
# version ='1.0'
# Description : A little helper tool to split big json files into chunks
# ---------------------------------------------------------------------------
import os
import json
import sys

#check python version
if sys.version_info[0] < 3:
    print("This script requires Python 3.x")
    sys.exit(1)
print("Welcome to the JSON Chunker!")
#get the filename from user
f = str(input("Please enter the filename you want to chunk:"))
fname = f + ".json" 
#get the chunk size from user
chunks = int(input("Please enter the chunk size you want to split the file into:"))
if chunks < 1:
    print("Please enter a valid number of chunk size")
    exit()  
else:
    if os.path.isfile(fname):
        print("File found, splitting into chunks...")
        with open(os.path.join(fname), 'r') as f1:
            lines = [json.loads(line.strip().encode('utf-8'))
                for line in f1.readlines()]
            #this is the number of lines in the file
            print("Total line count: ", len(lines))
            total = len(lines) // chunks
            #this is the number of files to be created
            print("Number of files to be created: ", total+1)
            
            for i in range(total+1):
                json.dump(lines[i * chunks:(i + 1) * chunks], open(
                    f + str(i+1) + ".json", 'w'), ensure_ascii=1, indent=1)
    else:
        print("File not found!")
        exit()
