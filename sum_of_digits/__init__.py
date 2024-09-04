import check50
import check50.c

@check50.check()
def exists():
    """sum_of_digits.c exists"""
    check50.exists("sum_of_digits.c")
    
@check50.check(exists)
def compiles():
    """sum_of_digits.c compiles"""
    check50.c.compile("sum_of_digits.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 123 456 789 -1 / 기대 출력 : 45"""
    check50.run("./sum_of_digits").stdin("123\n456\n789\n-1").stdout("45").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : 111 222 333 -1 / 기대 출력 : 18"""
    check50.run("./sum_of_digits").stdin("111\n222\n333\n-1").stdout("18").exit(0)
