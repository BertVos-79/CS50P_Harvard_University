def main():
    expression = input("Write your arithmetic expression here: ").strip().lower()
    interpreter(expression)


def interpreter(expression):
    expression_list = expression.split()
    match expression_list[1]:
        case "+":
            print(float(int(expression_list[0]) + int(expression_list[2])))
        case "*":
            print(float(int(expression_list[0]) * int(expression_list[2])))
        case "/":
            print(float(int(expression_list[0]) / int(expression_list[2])))
        case "-":
            print(float(int(expression_list[0]) - int(expression_list[2])))


main()
