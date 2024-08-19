import check50
import check50.c

@check50.check()
def exists():
    """diamond.c exists"""
    check50.exists("diamond.c")
    
@check50.check(exists)
def compiles():
    """diamond.c compiles"""
    check50.c.compile("diamond.c", lcs50 = True)

@check50.check(compiles)
def test_case():
    """....A....
    ...B.B...
    ..C...C..
    .D.....D.
    E.......E
    .D.....D.
    ..C...C..
    ...B.B...
    ....A...."""
    check50.run("./diamond").stdout("....A....\n").stdout("...B.B...\n").stdout("..C...C..\n").stdout(".D.....D.\n").stdout("E.......E\n").stdout(".D.....D.\n").stdout("..C...C..\n").stdout("...B.B...\n").stdout("....A....").exit(0)
