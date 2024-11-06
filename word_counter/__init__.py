import check50
import check50.c

@check50.check()
def exists():
    """word_counter.c exists"""
    check50.exists("word_counter.c")
    
@check50.check(exists)
def compiles():
    """word_counter.c compiles"""
    check50.c.compile("word_counter.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : i am a boy / 기대 출력 : 4"""
    check50.run("./word_counter").stdin("i am a boy").stdout("4").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : hello    world    w h a t / 기대 출력 : 6"""
    check50.run("./word_counter").stdin("hello    world    w h a t").stdout("6").exit(0)
