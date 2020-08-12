from os import walk

def getfiles(mypath):
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend( filenames )
        return f
