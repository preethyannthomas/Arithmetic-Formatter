def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first = []
    second = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        first.append(pieces[0])
        operator.append(pieces[1])
        second.append(pieces[2])

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    for i in range(len(first)):
        if not (first[i].isdigit() and second[i].isdigit()):
            return "Error: Numbers must only contain digits."

    for i in range(len(first)):
        if len(first[i]) > 4 or len(second[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(first)):
        if len(first[i]) > len(second[i]):
            first_line.append(" "*2 + first[i])
        else:
            first_line.append(" "*(len(second[i]) - len(first[i]) + 2) + first[i])

    for i in range(len(second)):
        if len(second[i]) > len(first[i]):
            second_line.append(operator[i] + " " + second[i])
        else:
            second_line.append(operator[i] + " "*(len(first[i]) - len(second[i]) + 1) + second[i])

    for i in range(len(first)):
        third_line.append("-"*(max(len(first[i]), len(second[i])) + 2))

    if answer:
        for i in range(len(first)):
            if operator[i] == "+":
                ans = str(int(first[i]) + int(second[i]))
            else:
                ans = str(int(first[i]) - int(second[i]))

            if len(ans) > max(len(first[i]), len(second[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(first[i]), len(second[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems
