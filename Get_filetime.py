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
