import check50
import check50.c

@check50.check()
def exists():
    """student_grade_manager.c exists"""
    check50.exists("student_grade_manager.c")
    
@check50.check(exists)
def compiles():
    """student_grade_manager.c compiles"""
    check50.c.compile("student_grade_manager.c", lcs50 = True)

@check50.check(compiles)
def test1():
    """학생 성적 관리 시스템에 오신 것을 환영합니다!\n
    \n
    1. 새 학생 추가\n
    2. 짝수 성적 개수 보기\n
    3. 학생 평균 성적 보기\n
    4. ID의 홀수 자릿수 합 보기\n
    5. 프로그램 종료\n
    원하는 작업을 선택하세요: 학생 ID를 입력하세요: 5개 과목의 성적을 입력하세요:\n
    과목 1 성적: 과목 2 성적: 과목 3 성적: 과목 4 성적: 과목 5 성적: 학년을 입력하세요 (1-4): 학생이 추가되었습니다.\n
    \n
    1. 새 학생 추가\n
    2. 짝수 성적 개수 보기\n
    3. 학생 평균 성적 보기\n
    4. ID의 홀수 자릿수 합 보기\n
    5. 프로그램 종료\n
    원하는 작업을 선택하세요: 학생 ID를 입력하세요: 5개 과목의 성적을 입력하세요:\n
    과목 1 성적: 과목 2 성적: 과목 3 성적: 과목 4 성적: 과목 5 성적: 학년을 입력하세요 (1-4): 학생이 추가되었습니다.\n
    \n
    1. 새 학생 추가\n
    2. 짝수 성적 개수 보기\n
    3. 학생 평균 성적 보기\n
    4. ID의 홀수 자릿수 합 보기\n
    5. 프로그램 종료\n
    원하는 작업을 선택하세요: 짝수 성적의 개수: 8\n
    \n
    1. 새 학생 추가\n
    2. 짝수 성적 개수 보기\n
    3. 학생 평균 성적 보기\n
    4. ID의 홀수 자릿수 합 보기\n
    5. 프로그램 종료\n
    원하는 작업을 선택하세요: 프로그램을 종료합니다. 안녕히 가세요!"""
    check50.run("./student_grade_manager").stdin("1\n2024\n51\n60\n50\n60\n50\n1\n1\n2023\n81\n80\n90\n80\n80\n2\n2\n5").stdout("프로그램을 종료합니다. 안녕히 가세요!\n").exit(0)
