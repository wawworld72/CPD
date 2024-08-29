import check50
import check50.c

@check50.check()
def exists():
    """mode_finder.c exists"""
    check50.exists("mode_finder.c")
    
@check50.check(exists)
def compiles():
    """mode_finder.c compiles"""
    check50.c.compile("mode_finder.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력1 : 6 / 입력2: 1 2 2 3 3 3/ 기대 출력 : 3"""
    check50.run("./mode_finder").stdin("6\n1\n2\n2\n3\n3\n3").stdout("3").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력1 : 5 / 입력2: 4 5 5 4 4/ 기대 출력 : 4"""
    check50.run("./mode_finder").stdin("5\n4\n5\n5\n4\n4").stdout("4").exit(0)

@check50.check(compiles)
def test_input_3():
    """입력1 : 5 / 입력2: -1 -1 -2 -2 -2 / 기대 출력 : -2"""
    check50.run("./mode_finder").stdin("-1\n -1\n -2\n -2\n -2").stdout("-2").exit(0)
