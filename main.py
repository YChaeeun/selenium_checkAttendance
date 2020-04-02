from work import Work
from notice import Notice
import flag as f

from student import student_dict

def main() :

    # 자동 로그인 여부 설정
    autoUpload = False

    n = Notice()
    w = Work()

    # notice
    n.welcome()
    n.instruction()

    while True : 
        try :
            key = int(input("입력 "))
        except :
            print("잘못된 입력입니다. 프로그램을 종료합니다.")
            break

        if key == 1 :
            if not f.loginFlag :
                w.login()
                w.moveMainToBoard()
                w.setTodayMonthDayName()
                f.loginFlag = True
            else :
                print("이미 로그인 하셨습니다")

        elif key == 2 :
            # 출석체크 게시물 작성하기
            if f.loginFlag :
                w.createCheckPost(autoUpload)
                f.attendancePostFlag = True
            else :
                print("로그인을 먼저 해주세요")
                continue
    
        elif key == 3:
            # 가장 최근 출석체크 게시물 접근
            if f.attendancePostFlag :
                w.moveBoardToNewCheckPost()
                f.accessAttendPostFlag = True
            else :
                print("새로운 출석체크 게시물을 먼저 생성해주세요")
                continue

        elif key == 4 :
            # 정상출석자 크롤링
            if f.accessAttendPostFlag :
                comment_list = w.crawlComments()
                attend = w.returnStudentId(comment_list)

                f.attendanceCrawlFlag = True
                print("출석자 크롤링 완료")
            else :
                print("출석체크 게시글로 접근해주세요")

        elif key == 5 :
            # 지각자 크롤링
            if f.accessAttendPostFlag :
                comment_list = w.crawlComments()
                late = w.returnStudentId(comment_list)

                lateCrawlFalg = True
                print("지각자 크롤링 완료")
            else :
                print("출석체크 게시글로 접근해주세요")
            
        elif key == 6 :
            if f.attendanceCrawlFlag and f.lateCrawlFlag :
                # 지각자 결석자 계산
                s_late = late - attend
                s_absent = set(student_dict) - (attend | s_late)

                # 결과 저장
                result_late = w.returnResultString(list(s_late))
                result_absent = w.returnResultString(list(s_absent))
                w.setResultString(result_late, result_absent)

                f.calculationCompleteFlag = True
                print("완료")
            else :
                print("출석자와 지각자 댓글을 모두 크롤링 해주세요")
                continue

        elif key == 7 :
            # 결과 게시물 작성
            if f.calculationCompleteFlag :
                w.createCompletePost(autoUpload)
                
                end = input("모든 작업을 완료했습니다. 프로그램을 종료하고 웹페이지를 닫을까요? (y/n) ")
                if end in "yYyesYesYES" :
                    break
                else :
                    continue

            else :
                print("지각자와 결석자 계산을 먼저 완료해주세요")
                continue

        elif key == 8 :
            w.back()

        elif key == 9 :
            w.forward()

        else :
            print("1~9 사이의 숫자 명령어를 입력해주세요")
            continue

    w.quit()
    
if __name__ == "__main__" :
    try :
        main()
    except :
        import traceback
        traceback.print_exc()
        input("Program crashed; press Enter to exit")