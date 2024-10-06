import check50
import check50.c

@check50.check()
def exists():
    """task_manager.c exists"""
    check50.exists("task_manager.c")
    
@check50.check(exists)
def compiles():
    """task_manager.c compiles"""
    check50.c.compile("task_manager.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """일정 추가 테스트"""
    check50.run("./task_manager").stdin("1\n12\n").stdout("일정이 추가되었습니다.").exit(0)
