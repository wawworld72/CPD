import check50
import check50.c

@check50.check()
def exists():
    """quiz_game.c exists"""
    check50.exists("test.c")
    
@check50.check(exists)
def compiles():
    """quiz_game.c compiles"""
    check50.c.compile("test.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """테스트 케이스1"""
    check50.run("./test").stdin("1\n").stdout("보통 난이도를 선택하셨습니다. 기본 점수 5점을 획득했습니다.")\
    .stdin("1\n3\n5\n2\n4\n").stdout("정답 개수: 1\n").stdout("최종 점수: 8")\
    .stdin("8\n").stdout("좋은 아침입니다! 아침 퀴즈로 하루를 시작하셨네요.").exit(0)

@check50.check(compiles)
def test_input_2():
    """테스트 케이스2"""
    check50.run("./test").stdin("2\n").stdout("어려움 난이도를 선택하셨습니다. 추가 점수는 없지만 정답당 점수가 높습니다.")\
    .stdin("1\n3\n2\n4\n5\n").stdout("정답 개수: 3\n").stdout("최종 점수: 15")\
    .stdin("20\n").stdout("안녕하세요! 저녁 시간의 퀴즈 도전이군요.").exit(0)
