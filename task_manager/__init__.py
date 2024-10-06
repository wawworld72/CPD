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
    """일정 관리 프로그램에 오신 것을 환영합니다!"""
    """1. 새 일정 추가"""
    """2. 일정 목록 보기"""
    """3. 프로그램 종료"""
    """원하는 작업을 선택하세요: 1"""
    """일정의 시간을 입력하세요 (0-23): 12"""
    """일정이 추가되었습니다."""
    check50.run("./task_manager").stdin("1\n12\n3\n").stdout("일정이 추가되었습니다.\n").exit(0)
