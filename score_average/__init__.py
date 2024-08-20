import check50
import check50.c

@check50.check()
def exists():
    """score_average.c exists"""
    check50.exists("score_average.c")
    
@check50.check(exists)
def compiles():
    """score_average.c compiles"""
    check50.c.compile("score_average.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 1 2 3 4 5 / 기대 출력 : 3.00"""
    check50.run("./score_average").stdin("1\n2\n3\n4\n5").stdout("3.00").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : 1 3 5 7 9 / 기대 출력 : 5.00"""
    check50.run("./score_average").stdin("1\n3\n5\n7\n9").stdout("5.00").exit(0)
