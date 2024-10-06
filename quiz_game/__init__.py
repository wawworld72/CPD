import check50
import check50.c

@check50.check()
def exists():
    """quiz_game.c exists"""
    check50.exists("quiz_game.c")
    
@check50.check(exists)
def compiles():
    """quiz_game.c compiles"""
    check50.c.compile("quiz_game.c", lcs50 = True)

@check50.check(compiles)
def test_input_1():
    """퀴즈 난이도를 선택하세요 (0: 쉬움, 1: 보통, 2: 어려움): 1\n
    보통 난이도를 선택하셨습니다. 기본 점수 5점을 획득했습니다!\n
    \n
    다음 질문들에 답하세요 (1-5 중 선택):\n
    질문 1: 1 질문 2: 3 질문 3: 5 질문 4: 2 질문 5: 4\n
    정답 개수: 1\n
    최종 점수: 8\n

    현재 시간을 입력하세요 (0-23): 8\n
    좋은 아침입니다! 아침 퀴즈로 하루를 시작하셨네요.!"""
    check50.run("./quiz_game").stdin("1\n1\n3\n5\n2\n4\n8\n").stdout("좋은 아침입니다! 아침 퀴즈로 하루를 시작하셨네요.!").exit(0)

