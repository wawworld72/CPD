import check50
import check50.c

@check50.check()
def exists():
    """palidrome_check.c exists"""
    check50.exists("palidrome_check.c")
    
@check50.check(exists)
def compiles():
    """palidrome_check.c compiles"""
    check50.c.compile("palidrome_check.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 1991 / 기대 출력 : 1991는 참"""
    check50.run("./palidrome_check").stdin("1991").stdout("1991는 참").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : 12321 / 기대 출력 : 12321는 참"""
    check50.run("./palidrome_check").stdin("12321").stdout("12321는 참").exit(0)

@check50.check(compiles)
def test_input_3():
    """입력 : 1234 / 기대 출력 : 1234는 거짓"""
    check50.run("./palidrome_check").stdin("1234").stdout("1991는 거짓").exit(0)

@check50.check(compiles)
def test_input_4():
    """입력 : -1 / 기대 출력 : 잘못된 입력"""
    check50.run("./palidrome_check").stdin("-1").stdout("잘못된 입력").exit(0)
