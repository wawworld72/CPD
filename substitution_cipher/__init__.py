import check50
import check50.c

@check50.check()
def exists():
    """substitution_cipher.c exists"""
    check50.exists("substitution_cipher.c")
    
@check50.check(exists)
def compiles():
    """substitution_cipher.c compiles"""
    check50.c.compile("substitution_cipher.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """\n입력 키:** qWeRtYuIoPlKjHgFdSaZxCvBnM\n
    입력 메시지:** Hello World!\n
    예상 출력:** 암호문: Itssg Vgksr!"""
    check50.run("./substitution_cipher").stdin("qWeRtYuIoPlKjHgFdSaZxCvBnM").stdin("Hello World!").stdout("Itssg Vgksr!").exit(0)

