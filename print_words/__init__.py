import check50
import check50.c

@check50.check()
def exists():
    """print_words.c exists"""
    check50.exists("print_words.c")
    
@check50.check(exists)
def compiles():
    """print_words.c compiles"""
    check50.c.compile("print_words.c", lcs50 = True)

@check50.check(compiles)
def test_input_15():
    """Test case 'i am a boy'"""
    check50.run("./print_words").stdin("i am a boy").stdout("i\nam\na\nboy\n").exit(0)

