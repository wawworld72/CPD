import check50
import check50.c

@check50.check()
def exists():
    """common_elements.c exists"""
    check50.exists("common_elements.c")
    
@check50.check(exists)
def compiles():
    """common_elements.c compiles"""
    check50.c.compile("common_elements.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """입력 : 1 2 3 4 5 6 7 8 9 / 기대 출력 : 5"""
    check50.run("./common_elements").stdin("1\n2\n3\n4\n5\n6\n7\n8\n9").stdout("5").exit(0)
