import check50
import check50.c

@check50.check()
def exists():
    """cap_words.c exists"""
    check50.exists("cap_words.c")
    
@check50.check(exists)
def compiles():
    """cap_words.c compiles"""
    check50.c.compile("cap_words.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """입력 : hello WORLD 123 cOmPuTeR / 기대 출력 : Hello World 123 Computer"""
    check50.run("./cap_words").stdin("hello WORLD 123 cOmPuTeR").stdout("Hello World 123 Computer").exit(0)

@check50.check(compiles)
def test_input_2():
    """입력 : i aM a bOY. / 기대 출력 : I Am A Boy."""
    check50.run("./cap_words").stdin("i aM a bOY.").stdout("I Am A Boy.").exit(0)
