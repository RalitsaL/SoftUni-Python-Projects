grade_data = float(input())


def solve(grade):

    if 2 <= grade_data <= 2.99:
        return "Fail"
    elif 3 <= grade_data <= 3.49:
        return "Poor"
    elif 3.5 <= grade_data <= 4.49:
        return "Good"
    elif 4.5 <= grade_data <= 5.49:
        return "Very Good"
    elif 5.5 <= grade_data <= 6:
        return "Excellent"


print(solve(grade_data))
