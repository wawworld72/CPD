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
    """\n  입력 x: 1 1 10 10 \n  입력 y: 5 5 10 10 \n  기대 출력 : 사각형들이 충돌합니다."""
    check50.run("./retangles").stdin("1").stdin("1").stdin("10").stdin("10").stdin("5").stdin("5").stdin("10").stdin("10").stdout("사각형들이 충돌합니다.").exit(0)

@check50.check(compiles)
def test_input_2():
    """\n  입력 x: 5 5 10 10 \n  입력 y: 1 1 10 10 \n  기대 출력 : 사각형들이 충돌합니다."""
    check50.run("./retangles").stdin("5").stdin("5").stdin("10").stdin("10").stdin("1").stdin("1").stdin("10").stdin("10").stdout("사각형들이 충돌합니다.").exit(0)

@check50.check(compiles)
def test_input_3():
    """\n  입력 x: 1 1 10 10 \n  입력 y: 15 15 10 10 \n  기대 출력 : 사각형들이 충돌하지 않습니다."""
    check50.run("./retangles").stdin("1").stdin("1").stdin("10").stdin("10").stdin("15").stdin("15").stdin("10").stdin("10").stdout("사각형들이 충돌하지 않습니다.").exit(0)


@check50.check(compiles)
def test_input_4():
    """\n  입력 x: -1 1 10 10 \n  입력 y: \n  기대 출력 : 잘못된 입력"""
    check50.run("./retangles").stdin("-1").stdin("1").stdin("10").stdin("10").stdout("잘못된 입력").exit(0)

