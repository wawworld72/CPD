import check50
import check50.c

@check50.check()
def exists():
    """arrayIndex.c exists"""
    check50.exists("array_index.c")
    
@check50.check(exists)
def compiles():
    """array_index.c compiles"""
    check50.c.compile("array_index.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 3 / 기대 출력 : 40"""
    check50.run("./array_index").stdin("3").stdout("40").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : 0 / 기대 출력 : 10"""
    check50.run("./array_index").stdin("0").stdout("10").exit(0)

@check50.check(compiles)
def test_input_3():
    """입력 : 5 / 기대 출력 : Invalid index"""
    check50.run("./array_index").stdin("5").stdout("Invalid index").exit(0)
