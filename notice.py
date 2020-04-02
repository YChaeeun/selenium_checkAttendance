
import os

class Notice :
    def __init__(self) :
        pass

    def welcome(self) :
        print("\n#################################################")

        print(" 게시물 댓글로 출석체크 하기 \n\n")

        print("제작 : 유채은 (github.com/YChaeeun/selenium_checkAttendance)")
        print("에러 신고 및 기타 건의 사항은 ychae.leah@gmail.com 으로 연락주세요!")

        print("시작하려면 아무 키나 눌러주세요")

        print("#################################################")

        key = input("")

        return

    def instruction(self) :
        os.system("clear")
        print("\n\n#################################################")

        print("1 로그인 & 게시판 이동 \n2 출석 게시물 작성\n3 최근 출석 게시물 보기\n4 크롤링 (출석)\n5 크롤링 (지각)\n6 계산\n7 결과 게시물 작성\n8 뒤로\n9 앞으로\n")
        print("\n** 숫자 이외의 값 입력 시 종료합니다.")

        print("#################################################")


