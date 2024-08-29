import check50
import check50.c

@check50.check()
def exists():
    """magic_square.c exists"""
    check50.exists("magic_square.c")
    
@check50.check(exists)
def compiles():
    """magic_square.c compiles"""
    check50.c.compile("magic_square.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : \n2 7 6 \n9 5 1 \n4 3 8  \n기대 출력 : 이 배열은 마방진입니다."""
    check50.run("./magic_square").stdin("2\n7\n6\n9\n5\n1\n4\n3\n8\n").stdout("이 배열은 마방진입니다.").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : \n3 1 2\n2 3 1 \n1 2 3  \n기대 출력 : 이 배열은 마방진이 아닙니다."""
    check50.run("./magic_square").stdin("3\n1\n2\n2\n3\n1\n1\n2\n3\n").stdout("이 배열은 마방진이 아닙니다.").exit(0)

@check50.check(compiles)
def test_input_3():
    """입력 : \n8 1 6 \n3 5 7 \n4 9 2  \n기대 출력 : 이 배열은 마방진입니다."""
    check50.run("./magic_square").stdin("8\n1\n6\n3\n5\n7\n4\n9\n2\n").stdout("이 배열은 마방진입니다.").exit(0)
