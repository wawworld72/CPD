import check50
import check50.c

@check50.check()
def exists():
    """gamed.c exists"""
    check50.exists("gamed.c")
    
@check50.check(exists)
def compiles():
    """gamed.c compiles"""
    check50.c.compile("gamed.c", lcs50 = True)
