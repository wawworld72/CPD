import check50
import check50.c

@check50.check()
def exists():
    """ops.c exists"""
    check50.exists("ops.c")
    
@check50.check(exists)
def compiles():
    """ops.c compiles"""
    check50.c.compile("ops.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """입력 : 5 3 2 3 4 2 3 1 2 3 / 기대 출력 : 3 2 1 3 2 4 3 2 3 5 / 3"""
    check50.run("./ops").stdin("5\n3\n2\n3\n4\n2\n3\n1\n2\n3").stdout("3 2 1 3 2 4 3 2 3 5").stdout("3").exit(0)

