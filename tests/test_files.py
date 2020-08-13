import common

def filecount(path):
    f = common.getfiles(path)
    return len(f)

def test_delivered():
    assert filecount("../data")>0

