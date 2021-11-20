import os
import sys
import datetime

from unrar import rarfile

def Key(filename):
    bFound = False
    fp = rarfile.RarFile(filename)

    start = 0
    stop = 9999
    for i in range(start, stop):
        pwd = str(i).zfill(4)
        try:
            fp.extractall(path = "./aaa", pwd = pwd)

            print('\nsucceed, key:'+pwd)
            bFound = True
            fp.close()

        except Exception as e:
            print("\rtry",'{:.0%}'.format((i - start)/(stop - start)), end = "")

        if bFound:
            break

if __name__=='__main__':
    starttime = datetime.datetime.now()
    Key(sys.argv[1])
    endtime = datetime.datetime.now()

    print("spend time", (endtime - starttime).seconds, 's')
