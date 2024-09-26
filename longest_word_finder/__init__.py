import check50
import check50.c

@check50.check()
def exists():
    """longest_word_finder.c exists"""
    check50.exists("longest_word_finder.c")
    
@check50.check(exists)
def compiles():
    """longest_word_finder.c compiles"""
    check50.c.compile("longest_word_finder.c")

@check50.check(compiles)
def test_input_1():
    """입력 : hello world programming / 기대 출력 : programming"""
    check50.run("./longest_word_finder").stdin("hello world programming").stdout("programming").exit(0)

