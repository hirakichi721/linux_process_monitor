#!/usr/bin/python

import subprocess
import os
import sys

if len(sys.argv)!=2:
  print("Usage: outputFilePath")
  sys.exit(0)
#PROCESS_COUNT_FILE = "process_count.csv"
PROCESS_COUNT_FILE = sys.argv[1]
# Proceess includes below are summerized as one process.(To exclude too many output.)
SPECIAL_PROCESSES = ["/usr/sbin/zabbix_proxy","/usr/sbin/zabbix_agentd"]

cmd = "ps -ef"

proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
result = proc.communicate()
stdout = result[0]
stdout = stdout.strip()


data = {}
# 0. Read Process Count file
# *Each line
#  cmd,count
if os.path.isfile(PROCESS_COUNT_FILE):
  with open(PROCESS_COUNT_FILE) as f:
    for line in f.readlines():
      line = line.strip()
      sps=line.split(",")
      data[",".join(sps[0:len(sps)-1])] = int(sps[len(sps)-1])

# 1. Read and merge processes
lineno=0
for line in stdout.split("\n"):
  lineno=lineno+1
  if lineno==1:
    continue
  sps = line.split()
  process_name = " ".join(sps[7:])
  process_name = process_name.strip()

  for i in range(0,len(SPECIAL_PROCESSES)):
    if process_name.find(SPECIAL_PROCESSES[i])!=-1:
      process_name = SPECIAL_PROCESSES[i]
      break

  if not process_name.startswith("["):
    process_name=process_name.rstrip(":")
    if process_name not in data.keys():
      data[process_name]=0
    data[process_name] = data[process_name]+1

# 2. Record
with open(PROCESS_COUNT_FILE,"w") as f:
  for key in sorted(data.keys()):
    f.write(",".join([key,str(data[key])]))
    f.write("\n")
