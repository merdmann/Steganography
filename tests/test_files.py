import common

def filecount(path):
    f = common.getfiles(path)
    return f.len

def test_delivered():
    assert filecount("../data")==0

