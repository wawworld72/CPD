import check50
import check50.c

@check50.check()
def exists():
    """filter.c exists"""
    check50.exists("filter.c")
    
@check50.check(exists)
def compiles():
    """test.c compiles"""
    check50.c.compile("filter.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """입력 : 15 / 기대 출력 : 1 2 4 5 7 8 10"""
    check50.run("./filter").stdin("15").stdout("1 2 4 5 7 8 10").exit(0)

@check50.check(compiles)
def test_input_9():
    """입력 : 9 / 기대 출력 : 1 2 4 5 7 8"""
    check50.run("./filter").stdin("9").stdout("1 2 4 5 7 8").exit(0)
