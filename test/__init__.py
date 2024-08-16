import check50
import check50.c

@check50.check()
def exists():
    """test.c exists"""
    check50.exists("test.c")
    
@check50.check(exists)
def compiles():
    """test.c compiles"""
    check50.c.compile("test.c", lcs50=True)

@check50.check(compiles)
def test_input_1():
    """input of 1 produces correct output"""
    check50.run("./test").stdin("1\n").stdout("output : 1\n").exit(0)

@check50.check(compiles)
def test_input_42():
    """input of 42 produces correct output"""
    check50.run("./test").stdin("42\n").stdout("output : 42\n").exit(0)
