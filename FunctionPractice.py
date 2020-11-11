#WAP to check whether the given number is palindrome or not
# def reverseNumber(number):
#     global reverse
#     reverse=0
#     while(number>0):
#         remainder = number % 10
#         reverse = (reverse*10) + remainder
#         number = number // 10
#     return reverse
#
# num= int(input('Enter a number: '))
# reverseNumber(num)
# if(reverse==num):
#     print('{} is a palindrome'.format(num))
# else:
#     print('{} is not a palindrome'.format(num))



#WAP to read first,middle and last name fo a person and print it's initials
# def initials(fname,mname,lname):
#     print('The initials are {}.{}.{}'.format(fname[0],mname[0],lname[0]))
#
# fname= input('Enter first name: ')
# mname= input('Enter middle name: ')
# lname= input('Enter last name: ')
# initials(fname,mname,lname)


#WAP to pass a list of numbers and print the sum of numbers which are multiple of 5
# def inputNumbers(n):
#     global numbers
#     numbers = []
#     for i in range(n):
#         user_input = int(input('Enter number: '))
#         numbers.append(user_input)
#     return numbers
#
# def sum(n,numbers):
#     global total
#     total = 0
#     for i in range(n):
#         if(numbers[i]%5==0):
#             total = total + numbers[i]
#     return total
#
# n = int(input('How many numbers?'))
# inputNumbers(n)
# sum(n,numbers)
# print('The sum of numbers divisible by 5 is {}'.format(total))


#WAP to input a number and find the sum of digits
# def sumOfDigits(number):
#     global sum
#     sum = 0
#     while (number > 0):
#          remainder = number % 10
#          sum = sum + remainder
#          number= number//10
#     return sum
#
# num = int(input('Enter a number: '))
# sumOfDigits(num)
# print('The sum of digits of the number {} is {}'.format(num,sum))




#WAP to pass a list of names and print the names whose starting and ending characters are vowels. eg:Apoorba

def inputNames(n):
    global names
    names = []
    for i in range(n):
        user_name = input('Enter name: ')
        names.append(user_name)
    return names

def vowelFilter(n,names):
    global vowel_list
    vowel_list = []
    for i in range(n):
        name = names[i].lower()
        add_name = names[i]
        if(name[0]=='a' or name[0]=='e' or name[0]=='i' or name[0]=='o' or name[0]=='u'):
            if(name[-1]=='a' or name[-1]=='e' or name[-1]=='i' or name[-1]=='o' or name[-1]=='u'):
                vowel_list.append(add_name)
    return vowel_list

n = int(input('How many names? '))
inputNames(n)
vowelFilter(n,names)
print('the list of names starting and ending with vowel are {}'.format(vowel_list))

