import check50
import check50.c

@check50.check()
def exists():
    """reversed_array.c 파일이 존재하는지 확인"""
    check50.exists("reversed_array.c")

@check50.check(exists)
def compiles():
    """reversed_array.c가 컴파일 되는지 확인"""
    check50.c.compile("reversed_array.c", lcs50=True)

@check50.check(compiles)
def test_case_1():
    """Test Case 1: 혼합 정수 입력"""
    check50.run("./reversed_array").stdin("1\n2\n4\n5\n7\n8\n9\n0\n3\n6\n").stdout("6 3 0 9 8 7 5 4 2 1\n").exit(0)

@check50.check(compiles)
def test_case_2():
    """Test Case 2: 순차적인 정수 입력"""
    check50.run("./reversed_array").stdin("1\n2\n3\n4\n5\n6\n7\n8\n9\n0\n").stdout("0 9 8 7 6 5 4 3 2 1\n").exit(0)

@check50.check(compiles)
def test_case_3():
    """Test Case 3: 음수 및 양수 혼합 입력"""
    check50.run("./reversed_array").stdin("-1\n-2\n-3\n-4\n-5\n6\n7\n8\n9\n10\n").stdout("10 9 8 7 6 -5 -4 -3 -2 -1\n").exit(0)
