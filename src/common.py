from os import walk

def get_files(mypath):
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)

    f=list(filter(lambda x: x.endswith(".pdf"), f))

    return f