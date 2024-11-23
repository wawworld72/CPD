import check50
import check50.c

@check50.check()
def exists():
    """del_alpha.c exists"""
    check50.exists("del_alpha.c")
    
@check50.check(exists)
def compiles():
    """del_alpha.c compiles"""
    check50.c.compile("del_alpha.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """입력 : Hello, World! 123 / 기대 출력 : HelloWorld"""
    check50.run("./del_alpha").stdin("Hello, World! 123").stdout("HelloWorld").exit(0)

@check50.check(compiles)
def test_input_9():
    """입력 : ###Hello@@@World### / 기대 출력 : HelloWorld"""
    check50.run("./del_alpha").stdin("###Hello@@@World###").stdout("HelloWorld").exit(0)

@check50.check(compiles)
def test_input_58():
    """입력 : The quick brown fox / 기대 출력 : HelloWorld"""
    check50.run("./del_alpha").stdin("The quick brown fox").stdout("Thequickbrownfox").exit(0)

@check50.check(compiles)
def test_input_24():
    """입력 : Word1    Word2     Word3 / 기대 출력 : WordWordWord"""
    check50.run("./del_alpha").stdin("Word1    Word2     Word3").stdout("WordWordWord").exit(0)
