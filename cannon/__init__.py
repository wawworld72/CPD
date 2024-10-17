import check50
import check50.c

@check50.check()
def exists():
    """arrayIndex.c exists"""
    check50.exists("cannon.c")
    
@check50.check(exists)
def compiles():
    """array_index.c compiles"""
    check50.c.compile("cannon.c", lcs50 = True)
