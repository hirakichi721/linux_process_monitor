# linux_process_monitor
Assuming to use on crontab, process monitoring program.

## When to use
- You are assigned as IT system administrator, but the system has no documents, and have no idea what all the server do.
- Then extract processes using monitor.py.
- And if the server has a pair(like, act/sby, act/act), you can compare.py to extract more accurately by comparing server processes.(You may be able to exclude bad and not expected jobs.)

## Usage
```
  python monitor.py OUTPUTFILEPATH
```
- This script read count in OUTPUTFILEPATH
- Check processes now via "ps -ef"
- Save process count to OUTPUTFILEPATH
- Recorded time is created in OUTPUTFILEPATH+".date" file

```
  python compare.py fileA fileB ...
```
- Compare processes output from monitor.py
- Then output as followings
- The first col is the command, and second is the first argument(test.txt), and third is second argument(test2.txt) ...
- o: a process appeared in the file
- x: a process did not appear in the file 
```
% python compare.py test.txt test2.txt test.txt
foo,x,o,x
hage,o,x,o
hoge,o,o,o
var,x,o,x
```
