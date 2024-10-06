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
    """1. 새 일정 추가\n"""
    """2. 일정 목록 보기\n"""
    """3. 프로그램 종료\n"""
    """원하는 작업을 선택하세요: 1\n"""
    """일정의 시간을 입력하세요 (0-23): 12\n"""
    """일정이 추가되었습니다."""
    check50.run("./task_manager").stdin("1\n12").stdout("일정이 추가되었습니다.").exit(0)
