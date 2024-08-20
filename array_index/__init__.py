import check50
import check50.c

@check50.check()
def exists():
    """array_index.c exists"""
    check50.exists("array_index.c")
    
@check50.check(exists)
def compiles():
    """array_index.c compiles"""
    check50.c.compile("array_index.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 3 / 기대 출력 : arr[3] = 40"""
    check50.run("./array_index").stdin("3").stdout("arr[3] = 40\n", "arr[3] = 40").exit(0)
