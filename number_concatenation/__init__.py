import check50
import check50.c

@check50.check()
def exists():
    """number_concatenation.c exists"""
    check50.exists("number_concatenation.c")
    
@check50.check(exists)
def compiles():
    """number_concatenation.c compiles"""
    check50.c.compile("number_concatenation.c", lcs50 = True)

@check50.check(compiles)
def test_input_2():
    """입력 : 9 8 7 6 -1 / 기대 출력 : 9876"""
    check50.run("./number_concatenation").stdin("9\n8\n7\n6\n-1").stdout("9876").exit(0)

@check50.check(compiles)
def test_input_3():
    """입력 : 0 1 2 3 -1 / 기대 출력 : 123"""
    check50.run("./number_concatenation").stdin("0\n1\n2\n3\n-1").stdout("123").exit(0)

@check50.check(compiles)
def test_input_4():
    """입력 : 5 4 3 2 1 -1 / 기대 출력 : 54321"""
    check50.run("./number_concatenation").stdin("5\n4\n3\n2\n1\n-1").stdout("54321").exit(0)

@check50.check(compiles)
def test_input_5():
    """입력 : 1 2 3 4 5 -1 / 기대 출력 : 12345"""
    check50.run("./number_concatenation").stdin("1\n2\n3\n4\n5\n-1").stdout("12345").exit(0)
