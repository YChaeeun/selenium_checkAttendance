from work import Work
from student import student_dict

def main() :
    
    w = Work()
    print("1 로그인 & 게시판 이동 / 2 출석 게시물 작성 / 3 최근 출석 게시물 보기 / 4 크롤링 (출석) / 5 크롤링 (지각) / 6 계산 / 7 결과 게시물 작성/ 8 뒤로 / 9 앞으로")
    print("숫자 이외의 값 입력 시 종료합니다.")

    while True : 

        try :
            key = int(input("입력 "))
        except :
            print("잘못된 입력입니다. 프로그램을 종료합니다.")
            break

        if key == 1 :
            w.login()
            w.moveMainToBoard()
            w.setTodayMonthDayName()

        elif key == 2 :
            # 출석체크 게시물 작성하기
            w.createCheckPost()
    
        elif key == 3:
            # 가장 최근 출석체크 게시물 접근
            w.moveBoardToNewCheckPost()

        elif key == 4 :
            # 정상출석자 크롤링
            comment_list = w.crawlComments()
            attend = w.returnStudentId(comment_list)
            print("출석자 크롤링 완료")

        elif key == 5 :
            # 지각자 크롤링
            comment_list = w.crawlComments()
            late = w.returnStudentId(comment_list)
            print("지각자 크롤링 완료")
            
        elif key == 6 :
            # 지각자 결석자 계산
            s_late = late - attend
            s_absent = set(student_dict) - (attend | s_late)

            # 결과 저장
            result_late = w.returnResultString(list(s_late))
            result_absent = w.returnResultString(list(s_absent))
            w.setResultString(result_late, result_absent)
            print("완료")

        elif key == 7 :
            # 결과 게시물 작성
            w.createCompletePost()

        elif key == 8 :
            w.back()

        elif key == 9 :
            w.forward()

        else :
            print("1~9 사이의 숫자 명령어를 입력해주세요")
            continue
    
if __name__ == "__main__" :
    main()