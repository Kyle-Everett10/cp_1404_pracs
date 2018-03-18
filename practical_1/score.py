def main():
    score = float(input("Enter Score: "))
    print(score_checker(score))


def score_checker(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score < 50:
        grade = "Fail"
    else:
        grade = "Pass"
    return grade


main()
