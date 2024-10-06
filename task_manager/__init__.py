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
def add_tesk_1():
    """일정 관리 프로그램에 오신 것을 환영합니다!\n
    \n
    1. 새 일정 추가\n
    2. 일정 목록 보기\n
    3. 프로그램 종료\n
    원하는 작업을 선택하세요: 1\n
    일정의 시간을 입력하세요 (0-23): 12\n
    일정이 추가되었습니다."""
    check50.run("./task_manager").stdin("1\n12\n3\n").stdout("일정이 추가되었습니다.\n").exit(0)

@check50.check(compiles)
def add_tesk_2():
    """일정 관리 프로그램에 오신 것을 환영합니다!\n
    \n
    1. 새 일정 추가\n
    2. 일정 목록 보기\n
    3. 프로그램 종료\n
    원하는 작업을 선택하세요: 1\n
    일정의 시간을 입력하세요 (0-23): 20\n
    일정이 추가되었습니다."""
    check50.run("./task_manager").stdin("1\n20\n3\n").stdout("일정이 추가되었습니다.\n").exit(0)

@check50.check(compiles)
def view_tesk():
    """일정 관리 프로그램에 오신 것을 환영합니다!\n
    \n
    1. 새 일정 추가\n
    2. 일정 목록 보기\n
    3. 프로그램 종료\n
    원하는 작업을 선택하세요: 2\n
    일정 목록:\n
    일정 1: 12시 - 오후\n
    일정 2: 20시 - 저녁"""
    check50.run("./task_manager").stdin("1\n12\n1\20\n2\n3\n").stdout("일정 1: 12시 - 오후\n일정 2: 20시 - 저녁").exit(0)
