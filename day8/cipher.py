from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_end = False


def caesar(text, shift, direct):
    result = ""
    if direct == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            p = alphabet.index(i)
            np = p+shift
            result += alphabet[np]
        else:
            result += i
    print(f"The result message is {result}")


while not should_end:
    direct = input("Enter whether to encode or decode: \n").lower()
    text = input("Enter the message: \n")
    shift = int(input("Enter the shift number: \n"))
    shift = shift % 26
    caesar(text=text, shift=shift, direct=direct)
    restart = input("Type 'Yes' to continue and 'No' to exit: \n").lower()
    print(restart)
    if restart == "no":
        should_end = True
        print("Thank you.")
