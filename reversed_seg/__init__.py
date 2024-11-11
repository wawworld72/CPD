import check50
import check50.c

@check50.check()
def exists():
    """reversed_seg.c exists"""
    check50.exists("reversed_seg.c")
    
@check50.check(exists)
def compiles():
    """reversed_seg.c compiles"""
    check50.c.compile("reversed_seg.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """입력 : hello. / 기대 출력 : olleh."""
    check50.run("./reversed_seg").stdin("hello.").stdout("olleh.").exit(0)

@check50.check(compiles)
def test_input_9():
    """입력 : I am a boy / 기대 출력 : i ma a yob"""
    check50.run("./reversed_seg").stdin("I am a boy").stdout("i ma a yob").exit(0)
