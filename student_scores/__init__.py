import check50
import check50.c

@check50.check()
def exists():
    """student_scores.c exists"""
    check50.exists("student_scores.c")
    
@check50.check(exists)
def compiles():
    """student_scores.c compiles"""
    check50.c.compile("student_scores.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """기대 출력 : \n학생 1: 총점 = 345, 평균 = 86.25 \n학생 2: 총점 = 343, 평균 = 85.75 \n학생 3: 총점 = 356, 평균 = 89.00"""
    check50.run("./student_scores").stdout("학생 1: 총점 = 345, 평균 = 86.25\n학생 2: 총점 = 343, 평균 = 85.75\n학생 3: 총점 = 356, 평균 = 89.00").exit(0)
