from check50 import *

@check()
def exists():
    """substitution.c exists"""
    return exists("substitution.c")

@check("exists")
def compiles():
    """substitution.c compiles"""
    return run("clang -o substitution substitution.c -lcs50").exit(0)

@check("compiles")
def test_case_1():
    """Test case 1: Valid key and message"""
    key = "qWeRtYuIoPlKjHgFdSaZxCvBnM"
    plaintext = "Hello World!"
    expected_output = "암호문: Itssg Vgksr!"

    output = run("./substitution " + key).stdin(plaintext).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output

@check("compiles")
def test_case_2():
    """Test case 2: Valid key and message"""
    key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    expected_output = "암호문: ZYXWVUTSRQPONMLKJIHGFEDCBA"

    output = run("./substitution " + key).stdin(plaintext).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output

@check("compiles")
def test_case_3():
    """Test case 3: Duplicate characters in key"""
    key = "QWERTYUIOPLKJHGFDSAZXCVBQ"
    expected_output = "키에는 중복된 문자가 없어야 합니다."

    output = run("./substitution " + key).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output

@check("compiles")
def test_case_4():
    """Test case 4: Non-alphabetic characters in key"""
    key = "QWERTYUIOPLKJHGFD1AZXCVBNM"
    expected_output = "키는 오직 알파벳 문자만 포함해야 합니다."

    output = run("./substitution " + key).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output

@check("compiles")
def test_case_5():
    """Test case 5: Key length not equal to 26"""
    key = "QWERTYUIOPLKJHGFDSAZXCVBNML"
    expected_output = "키는 26개의 문자로 구성되어야 합니다."

    output = run("./substitution " + key).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output

@check("compiles")
def test_case_6():
    """Test case 6: Valid key with no change in non-alpha characters"""
    key = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    plaintext = "1234!@#$"
    expected_output = "암호문: 1234!@#$"

    output = run("./substitution " + key).stdin(plaintext).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output

@check("compiles")
def test_case_7():
    """Test case 7: Valid key with mixed input"""
    key = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    plaintext = "CS50rocks!"
    expected_output = "암호문: LP50vekyh!"

    output = run("./substitution " + key).stdin(plaintext).stdout().strip()
    print(output)  # For debugging
    assert expected_output in output
