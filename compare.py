#!/usr/bin/python

import subprocess
import os
import sys

if len(sys.argv)<3:
  print("Usage: fileA fileB")
  sys.exit(0)

data = [] 
# 0. Read Process Count file
# *Each line
#  cmd,count
for fp in sys.argv[1:]:
  dataA = {}
  if os.path.isfile(fp):
    with open(fp) as f:
      for line in f.readlines():
        line = line.strip()
        sps=line.split(",")
        dataA[",".join(sps[0:len(sps)-1])] = int(sps[len(sps)-1])
  data.append(dataA)

allkeys = []
for dic in data:
  allkeys.extend(dic.keys())
uniqkeys = sorted(list(set(allkeys)))

for key in uniqkeys:
  outputline = key
  for i in range(0,len(data)):
    if key in data[i].keys():
      outputline = outputline + "," + "o"
    else:
      outputline = outputline + "," + "x"
  print(outputline)
      
