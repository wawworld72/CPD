import check50
import check50.c

@check50.check()
def exists():
    """test.c exists"""
    check50.exists("test.c")

@check50.check(exists)
def compiles():
    """test.c compiles"""
    check50.c.compile("test.c", lcs50=True)

@check50.check(compiles)
def test_add_student():
    """학생 추가 + 짝수 성적 출력 테스트"""
    check50.run("./test").stdin("1\n2024\n51\n60\n50\n60\n50\n1).stdout("학생이 추가되었습니다.")/
    .stdin("1\n2023\n81\n80\n90\n80\n80\n2").stdout("학생이 추가되었습니다.")/
    .stdin("2\n").stdout("짝수 성적의 개수: 8")
