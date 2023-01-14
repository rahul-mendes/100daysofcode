def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


oper = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculate():
    cont = True
    n1 = int(input("Enter number: "))
    while cont:
        n2 = int(input("Enter number: "))
        operate = input("Enter an operator: ")
        calc = oper[operate]
        answer = calc(n1, n2)
        print(answer)
        if input(f"Enter y to use {answer} as n1 and any letter to continue: ") == "y":
            n1 = answer
        else:
            cont = False
            calculate()


calculate()
