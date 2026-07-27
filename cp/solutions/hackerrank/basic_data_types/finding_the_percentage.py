if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # My code
    # if query_name in student_marks[name]: # --> wrong here because the key should be query_name – not name
    #     print(sum(student_marks[query_name]) / len(student_marks[query_name]))

    # Corrected code
    scores_list = student_marks[query_name] # get the score of the queried student
    avg = sum(scores_list) / len(scores_list)
    print(f"{avg:.2f}")
