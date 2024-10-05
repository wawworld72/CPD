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
    """입력 키: qWeRtYuIoPlKjHgFdSaZxCvBnM / 입력 메시지: Hello World! / 기대 출력: 암호문: Itssg Vgksr!"""
    check50.run("./substitution_cipher qWeRtYuIoPlKjHgFdSaZxCvBnM").stdin("Hello World!").stdout("암호문: Itssg Vgksr!").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 키: ZYXWVUTSRQPONMLKJIHGFEDCBA / 입력 메시지: ABCDEFGHIJKLMNOPQRSTUVWXYZ / 기대 출력: 암호문: ZYXWVUTSRQPONMLKJIHGFEDCBA"""
    check50.run("./substitution_cipher ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("ABCDEFGHIJKLMNOPQRSTUVWXYZ").stdout("암호문: ZYXWVUTSRQPONMLKJIHGFEDCBA").exit(0)

@check50.check(compiles)
def test_input_3():
    """입력 키: QWERTYUIOPLKJHGFDSAZXCVBQ / 기대 출력: 키에는 중복된 문자가 없어야 합니다."""
    check50.run("./substitution_cipher QWERTYUIOPLKJHGFDSAZXCVBQ").stdin("test").stdout("키에는 중복된 문자가 없어야 합니다.").exit(1)

@check50.check(compiles)
def test_input_4():
    """입력 키: QWERTYUIOPLKJHGFD1AZXCVBNM / 기대 출력: 키는 오직 알파벳 문자만 포함해야 합니다."""
    check50.run("./substitution_cipher QWERTYUIOPLKJHGFD1AZXCVBNM").stdin("test").stdout("키는 오직 알파벳 문자만 포함해야 합니다.").exit(1)

@check50.check(compiles)
def test_input_5():
    """입력 키: QWERTYUIOPLKJHGFDSAZXCVBNML / 기대 출력: 키는 26개의 문자로 구성되어야 합니다."""
    check50.run("./substitution_cipher QWERTYUIOPLKJHGFDSAZXCVBNML").stdin("test").stdout("키는 26개의 문자로 구성되어야 합니다.").exit(1)

@check50.check(compiles)
def test_input_6():
    """입력 키: QWERTYUIOPLKJHGFDSAZXCVBNM / 입력 메시지: 1234!@#$ / 기대 출력: 암호문: 1234!@#$"""
    check50.run("./substitution_cipher QWERTYUIOPLKJHGFDSAZXCVBNM").stdin("1234!@#$").stdout("암호문: 1234!@#$").exit(0)

@check50.check(compiles)
def test_input_7():
    """입력 키: QWERTYUIOPLKJHGFDSAZXCVBNM / 입력 메시지: CS50rocks! / 기대 출력: 암호문: LP50vekyh!"""
    check50.run("./substitution_cipher QWERTYUIOPLKJHGFDSAZXCVBNM").stdin("CS50rocks!").stdout("암호문: LP50vekyh!").exit(0)
