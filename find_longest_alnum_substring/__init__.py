import check50
import check50.c

@check50.check()
def exists():
    """find_longest_alnum_substring.c exists"""
    check50.exists("find_longest_alnum_substring.c")
    
@check50.check(exists)
def compiles():
    """find_longest_alnum_substring.c compiles"""
    check50.c.compile("find_longest_alnum_substring.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : i am a boy. / 기대 출력 : boy"""
    check50.run("./find_longest_alnum_substring").stdin("i am a boy.").stdout("boy").exit(0)
