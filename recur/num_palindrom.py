num=15351
num_c=num
def reverse_num(num,reversed_num=0):
    if num==0:
        return reversed_num
    else:
        digit=num%10
        reversed_num=digit + reversed_num * 10
        return reverse_num(num//10,reversed_num)

def num_palindrom(num):
    if num<0:
        return False
    rev=reverse_num(num)
    return num == rev
print(num_palindrom(num))