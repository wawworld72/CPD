import check50
import check50.c

@check50.check()
def exists():
    """reversed_array.c exists"""
    check50.exists("reversed_array.c")

@check50.check(exists)
def compiles():
    """reversed_array.c compiles"""
    check50.c.compile("reversed_array.c", lcs50=True)

@check50.check(compiles)
def test_case_1():
    """Test Case 1: Input with mixed integers"""
    check50.run("./reversed_array") \
        .stdin("1\n2\n4\n5\n7\n8\n9\n0\n3\n6") \
        .stdout("6 3 0 9 8 7 5 4 2 1\n").exit(0)

@check50.check(compiles)
def test_case_2():
    """Test Case 2: Input with sequential integers"""
    check50.run("./reversed_array") \
        .stdin("1 2 3 4 5 6 7 8 9 0") \
        .stdout("0 9 8 7 6 5 4 3 2 1\n").exit(0)

@check50.check(compiles)
def test_case_3():
    """Test Case 3: Input with negative and positive numbers"""
    check50.run("./reversed_array") \
        .stdin("-1 -2 -3 -4 -5 6 7 8 9 10") \
        .stdout("10 9 8 7 6 -5 -4 -3 -2 -1\n").exit(0)
