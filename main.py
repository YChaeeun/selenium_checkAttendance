from work import Work
from student import student_dict


def main() :
    w = Work()

    w.login()

    w.moveMainToBoard()
    w.setTodayMonthDayName()
    
    # 출석체크 게시물 작성하기
    w.createCheckPost()

    # 가장 최근에 작성한 출석체크 게시물에서 댓글 크롤링 후 학번 추출하기
    w.moveBoardToNewCheckPost()

    # 정상출석자 35분에 크롤링
    comment_list = w.crawlComments()
    attend = w.returnStudentId(comment_list)

    # 지각자 50분에 크롤링
    comment_list = w.crawlComments()
    late = w.returnStudentId(comment_list)

    # 지각자 결석자 계산
    s_late = late - attend
    s_absent = set(student_dict) - (attend | s_late)

    # 결과
    result_late = w.returnResultString(list(s_late))
    result_absent = w.returnResultString(list(s_absent))
    w.setResultString(result_late, result_absent)

    # 결과 게시물 작성
    w.createCompletePost()


if __name__ == "__main__" :
    main()