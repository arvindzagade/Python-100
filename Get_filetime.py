from datetime import datetime
from datetime import timedelta

def is_file_older_than (file, delta): 
    cutoff = datetime.utcnow() - delta
    mtime = datetime.utcfromtimestamp(os.path.getmtime(file))
    if mtime < cutoff:
        return True
    return False

 
is_file_older_than(filename, timedelta(seconds=10))

#is_file_older_than(filename, timedelta(days=10))





# print("Last modified: %s" % time.ctime(os.path.getmtime(file)))
    # print("current time:%s" % datetime.utcnow())
    # diff = datetime.utcnow() - datetime.utcfromtimestamp(os.path.getmtime(file))
    # print(diff)
    #filetime = "Last modified: %s" % time.ctime(os.path.getmtime(file))
    # now = datetime.now()
    # now = now.strftime('%Y-%m-%d %H:%M:%S')
    # print(now)
    # FMT = '%Y-%m-%d %H:%M:%S'
    # time_diff = datetime.strptime(now,FMT) - datetime.strptime(file,FMT)
    # print(time_diff)
