# linux_process_monitor
Assuming to use on crontab, process monitoring program.

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
