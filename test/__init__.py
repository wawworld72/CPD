import check50
import check50.c

@check50.check()
def exists():
    """student_grade_manager_test exists"""
    check50.exists("test.c")

@check50.check(exists)
def compiles():
    """student_grade_manager_test compiles"""
    check50.c.compile("test.c", lcs50=True)

@check50.check(compiles)
def test_add_student():
    """학생 추가 기능이 정상적으로 작동하는지 테스트합니다."""
    check50.run("./test").stdin("1\n2024\n51\n60\n50\n60\n50\n1\n")\
        .stdout("학생이 추가되었습니다.\n").exit(0)

@check50.check(compiles)
def test_even_grades_count():
    """짝수 성적의 개수를 정확하게 세는지 테스트합니다."""
    check50.run("./test").stdin("1\n2024\n51\n60\n50\n60\n50\n1\n")\
        .stdin("1\n2023\n81\n80\n90\n80\n80\n2\n")\
        .stdin("2\n")\
        .stdout("짝수 성적의 개수: 8\n", regex=False).exit(0)

@check50.check(compiles)
def test_average_grade():
    """학생의 평균 성적을 정확하게 계산하는지 테스트합니다."""
    check50.run("./test").stdin("1\n2023\n81\n80\n90\n80\n80\n2\n")\
        .stdin("3\n0\n")\
        .stdout("학생 ID: 2023, 평균 성적: 82.20\n", regex=False).exit(0)

@check50.check(compiles)
def test_sum_odd_digits():
    """학생의 ID에서 홀수 자릿수의 합을 정확히 계산하는지 테스트합니다."""
    check50.run("./test").stdin("1\n2023\n81\n80\n90\n80\n80\n2\n")\
        .stdin("4\n0\n")\
        .stdout("학생 ID: 2023, ID의 홀수 자릿수 합: 3\n", regex=False).exit(0)

@check50.check(compiles)
def test_program_exit():
    """프로그램 종료 메시지를 정확하게 출력하는지 테스트합니다."""
    check50.run("./test").stdin("5\n")\
        .stdout("프로그램을 종료합니다. 안녕히 가세요!\n", regex=False).exit(0)
