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
def test_input_15():
    """입력 : \n2 7 6 \n9 5 1 \n4 3 8  \n기대 출력 : 이 배열은 마방진입니다."""
    check50.run("./magic_square").stdin("2\n7\n6\n9\n5\n1\n4\n3\n8\n").stdout("이 배열은 마방진입니다.").exit(0)

