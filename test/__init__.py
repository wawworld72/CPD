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
def test1():
    """테스트 케이스1"""
    check50.run("./test").stdin("1\n2024\n51\n60\n50\n60\n50\n1\n").stdout("학생이 추가되었습니다.")\
    .stdin("1\n2023\n81\n80\n90\n80\n80\n2").stdout("학생이 추가되었습니다.")\
    .stdin("2\n").stdout("짝수 성적의 개수: 8")\
    .stdin("5\n").stdout("프로그램을 종료합니다. 안녕히 가세요!")

@check50.check(compiles)
def test2():
    """테스트 케이스2"""
    check50.run("./test").stdin("1\n2024\n51\n60\n50\n60\n50\n1\n").stdout("학생이 추가되었습니다.")\
    .stdin("1\n2023\n81\n80\n90\n80\n80\n2").stdout("학생이 추가되었습니다.")\
    .stdin("3\n1\n").stdout("학생 ID: 2023, 평균 성적: 82.20")\
    .stdin("5\n").stdout("프로그램을 종료합니다. 안녕히 가세요!")

@check50.check(compiles)
def test3():
    """테스트 케이스3"""
    check50.run("./test").stdin("1\n2024\n51\n60\n50\n60\n50\n1\n").stdout("학생이 추가되었습니다.")\
    .stdin("1\n2023\n81\n80\n90\n80\n80\n2").stdout("학생이 추가되었습니다.")\
    .stdin("4\n1\n").stdout("학생 ID: 2023, ID의 홀수 자릿수 합: 3")\
    .stdin("5\n").stdout("프로그램을 종료합니다. 안녕히 가세요!")
