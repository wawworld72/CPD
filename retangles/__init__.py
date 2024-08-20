import check50
import check50.c

@check50.check()
def exists():
    """retangles.c exists"""
    check50.exists("retangles.c")
    
@check50.check(exists)
def compiles():
    """retangles.c compiles"""
    check50.c.compile("retangles.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 x: 1 1 10 10 \n 입력 y: 5 5 10 10 \n 기대 출력 : 사각형들이 충돌합니다."""
    check50.run("./retangles").stdin("1").stdin("1").stdin("10").stdin("10").stdin("5").stdin("5").stdin("10").stdin("10").stdout("사각형들이 충돌합니다.").exit(0)
