#You have the numbers 12345, 9845, 178999884662, 7834865
#Write a function to reverse the numbers 
#example 12345 to 54321

num1 = 12345
num2 = 9845
num3 = 178999884662
num4 = 7834865

def reverse_num(num :int):
    '''Function that reverses a number'''
    new_num = 0

    while num > 0:
        digit = num % 10
        num = int(num / 10)
        new_num *= 10
        new_num += digit
        #print(digit, num, new_num, '/n')

    return new_num


if __name__ == "__main__":
    print(reverse_num(num1))
    print(reverse_num(num2))
    print(reverse_num(num3))
    print(reverse_num(num4))
