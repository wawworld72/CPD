import check50
import check50.c

@check50.check()
def exists():
    """select_next_number.c exists"""
    check50.exists("select_next_number.c")
    
@check50.check(exists)
def compiles():
    """select_next_number.c compiles"""
    check50.c.compile("select_next_number.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력1 : 1 2 3 4 5 4 3 -1, 입력2 : 1 / 기대 출력 : 2345"""
    check50.run("./select_next_number").stdin("1\n2\n3\n4\n5\n4\n3\n-1\n1").stdout("2345").exit(0)

