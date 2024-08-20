import check50
import check50.c

@check50.check()
def exists():
    """sum.c exists"""
    check50.exists("sum.c")
    
@check50.check(exists)
def compiles():
    """sum.c compiles"""
    check50.c.compile("sum.c", lcs50 = True)

@check50.check(compiles)
def test_case_1():
    """입력 : 5 10 / 기대 출력 : 15"""
    check50.run("./sum").stdin("5").stdin("10").stdout("15").exit(0)

@check50.check(compiles)
def test_case_2():
    """입력 : 20 30 / 기대 출력 : 50"""
    check50.run("./sum").stdin("20").stdin("30").stdout("50").exit(0)
