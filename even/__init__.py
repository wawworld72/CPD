import check50
import check50.c

@check50.check()
def exists():
    """even.c exists"""
    check50.exists("even.c")
    
@check50.check(exists)
def compiles():
    """even.c compiles"""
    check50.c.compile("even.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 4 7 2 -1 / 기대 출력 : 2"""
    check50.run("./even").stdin("4 7 2 -1").stdout("2").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : 5 11 -5 / 기대 출력 : 0"""
    check50.run("./even").stdin("5 11 -5").stdout("0").exit(0)
