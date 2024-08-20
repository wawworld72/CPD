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
def test_input_1():
    """입력 : 123456 / 기대 출력 : 9"""
    check50.run("./oddsum").stdin("123456").stdout("9").exit(0)
