import check50
import check50.c

@check50.check()
def exists():
    """oddsum.c exists"""
    check50.exists("oddsum.c")
    
@check50.check(exists)
def compiles():
    """oddsum.c compiles"""
    check50.c.compile("oddsum.c", lcs50 = True)

@check50.check(compiles)
def test_input_123456():
    """입력 : 123456 / 기대 출력 : 9"""
    check50.run("./oddsum").stdin("123456").stdout("9").exit(0)

@check50.check(compiles)
def test_input_24680():
    """입력 : 24680 / 기대 출력 : 0"""
    check50.run("./oddsum").stdin("24680").stdout("0").exit(0)


@check50.check(compiles)
def test_input_13579():
    """입력 : 13579 / 기대 출력 : 25"""
    check50.run("./oddsum").stdin("13579").stdout("25").exit(0)

@check50.check(compiles)
def test_input_-97531():
    """입력 : -97531 / 기대 출력 : 25"""
    check50.run("./oddsum").stdin("-97531").stdout("25").exit(0)
