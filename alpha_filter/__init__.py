import check50
import check50.c

@check50.check()
def exists():
    """alpha_filter.c exists"""
    check50.exists("alpha_filter.c")
    
@check50.check(exists)
def compiles():
    """alpha_filter.c compiles"""
    check50.c.compile("alpha_filter.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """입력 : i am a boy / 기대 출력 : iamaboy"""
    check50.run("./alpha_filter").stdin("i am a boy").stdout("iamaboy").exit(0)

@check50.check(compiles)
def test_input_9():
    """입력 : hello   world   w h a t / 기대 출력 : helloworldwhat"""
    check50.run("./alpha_filter").stdin("hello   world   w h a t").stdout("helloworldwhat").exit(0)
