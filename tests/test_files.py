import common
from pdfminer.high_level import extract_text

def file_count(path):
    f = common.get_files(path)
    return len(f)

def file_list(path):
    f = common.get_files(path)
    return f

def test_delivered():
    f = file_list( "../data" )
    assert file_count("../data") == 2
    assert f[0] == 'Bible - German Luther Translation.pdf'
    assert f[1] == 'The Epic of Gilgamesh.pdf'

# reading file 1 and 0. Both are existing and have different number of
# words as contents.
def test_read_file():
    d = read_file(0)
    assert len(d) > 0
    e = read_file(1)
    assert len(e) >  0 and len(d) > 0
    assert len(d) != len(e)

# reading the text file 0
def read_file(id):
    f = common.get_files("../data")
    text = extract_text( "../data/" + f[id])
    assert len(text.split()) > 1
    return text.split()


