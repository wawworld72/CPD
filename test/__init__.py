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
def test_input_15():
    """input of 15 produces correct output"""
    check50.run("./test").stdin("15\n").stdout("1 2 4 5 7 8 10\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test_input_9():
    """input of 9 produces correct output"""
    check50.run("./test").stdin("9\n").stdout("1 2 4 5 7 8\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test_input_x():
    """input of x produces correct output"""
    check50.run("./test").stdin("12").stdout("AMEX\n").stdout(check50.EOF).exit(0)