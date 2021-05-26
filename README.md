# linux_process_monitor
Assuming to use on crontab, process monitoring program.

## Usage
```
  python monitor.py OUTPUTFILEPATH
```
- This script read count in OUTPUTFILEPATH
- Check processes now via "ps -ef"
- Save process count to OUTPUTFILEPATH

You can find the processes run on the Linux server for some time.
Use this script if you don't know what processes are running on the server.
