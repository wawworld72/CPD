import check50
import check50.c

@check50.check()
def exists():
    """time_greeting.c exists"""
    check50.exists("time_greeting.c")
    
@check50.check(exists)
def compiles():
    """time_greeting.c compiles"""
    check50.c.compile("time_greeting.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 13 / 기대 출력 : Good afternoon!"""
    check50.run("./time_greeting").stdin("13").stdout("Good afternoon!").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : 20 / 기대 출력 : Good evening!"""
    check50.run("./time_greeting").stdin("20").stdout("Good evening!").exit(0)
