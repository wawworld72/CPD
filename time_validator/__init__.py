import check50
import check50.c

@check50.check()
def exists():
    """time_validator.c exists"""
    check50.exists("time_validator.c")
    
@check50.check(exists)
def compiles():
    """time_validator.c compiles"""
    check50.c.compile("time_validator.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : 3 / 기대 출력 : Invalid hour."""
    check50.run("./time_validator").stdin("3").stdout("Invalid hour.").exit(0)
