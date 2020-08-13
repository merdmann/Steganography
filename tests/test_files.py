import common
from pdfminer.high_level import extract_text

def filecount(path):
    f = common.getfiles(path)
    return len(f)

def test_delivered():
    assert filecount("../data") > 0

# reading the text file 0
def test_read_file():
    f = common.getfiles("../data")
    text = extract_text( "../data/" +f[0])
    print(text.split())   ## creating a list of word might be help full later
    assert len(text.split()) > 1
