from os import walk
from pdfminer.high_level import extract_text

def get_files(mypath):
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)

    f=list(filter(lambda x: x.endswith(".pdf"), f))

    return f


def file_list(path):
    f = get_files(path)
    return f

# reading the text file 0
def read_file(id):
    f = get_files("../data")
    text = extract_text( "../data/" + f[id])
    return text.split()