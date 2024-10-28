import check50
import check50.c

@check50.check()
def exists():
    """substitution_cipher.c exists"""
    check50.exists("substitution_cipher.c")
    
@check50.check(exists)
def compiles():
    """substitution_cipher.c compiles"""
    check50.c.compile("substitution_cipher.c", lcs50=True)

@check50.check(compiles)
def test_input_1():
    """\n입력 키: ZYXWVUTSRQPONMLKJIHGFEDCBA\n
    입력 메시지: ABCDEFGHIJKLMNOPQRSTUVWXYZ\n
    예상 출력: ZYXWVUTSRQPONMLKJIHGFEDCBA"""
    check50.run("./substitution_cipher") \
           .stdin("ZYXWVUTSRQPONMLKJIHGFEDCBA") \
           .stdin("ABCDEFGHIJKLMNOPQRSTUVWXYZ") \
           .stdout("ZYXWVUTSRQPONMLKJIHGFEDCBA") \
           .exit(0)

@check50.check(compiles)
def test_input_2():
    """\n입력 키: QWERTYUIOPLKJHGFDSAZXCVBNM\n
    입력 메시지: ABCDEFGHIJKLMNOPQRSTUVWXYZ\n
    예상 출력: ZYXWVUTSRQPONMLKJIHGFEDCBA"""
    check50.run("./substitution_cipher") \
           .stdin("ZYXWVUTSRQPONMLKJIHGFEDCBA") \
           .stdin("I am a boy") \
           .stdout("R zn z ylb") \
           .exit(0)


@check50.check(compiles)
def test_input_3():
    """\n입력 키: qWeRtYuIoPlKjHgFdSaZxCvBnM\n
    입력 메시지: Hello World!\n
    예상 출력: Itkkg Vgksr!"""
    check50.run("./substitution_cipher") \
           .stdin("qWeRtYuIoPlKjHgFdSaZxCvBnM") \
           .stdin("Hello World!") \
           .stdout("Itkkg Vgksr!\n") \
           .exit(0)
