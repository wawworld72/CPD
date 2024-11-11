import check50
import check50.c

@check50.check()
def exists():
    """fchar_frequency.c exists"""
    check50.exists("char_frequency.c")
    
@check50.check(exists)
def compiles():
    """char_frequency.c compiles"""
    check50.c.compile("char_frequency.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """테스트 케이스 통과는 초록색"""
    check50.run("./char_frequency").stdin("i am a boy").stdout("i 1\n  3\na 2\nm 1\nb 1\no 1\ny 1\n").exit(0)
