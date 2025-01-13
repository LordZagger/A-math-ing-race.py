#this program is for the WEO "The A-math-ing" race activity
mode = input('Enter the first number: ')
if mode == '71':
    int1 = int(input("Reenter the first number: "))
    int2 = int(input("Enter the second number: "))
    int3 = int(input("Enter the third number: "))
    int4 = int(input("Enter the fourth number: "))
    int5 = int(input("Enter the fifth number: "))
    int6 = int(input("Enter the sixth number: "))
    int7 = int(input("Enter the seventh number: "))
    int8 = int(input("Enter the eigth number: "))
    int9 = int(input("Enter the last number: "))
    list_answer = [int1,int2,int3,int4,int5,int6,int7,int8,int9]
else:
    int1 = int(input("Renter the first number: "))
    int2 = int(input("Enter the second number: "))
    int3 = int(input("Enter the third number: "))
    int4 = int(input("Enter the fourth number: "))
    int5 = int(input("Enter the fifth number: "))
    int6 = int(input("Enter the sixth number: "))
    int7 = int(input("Enter the seventh number: "))
    int8 = int(input("Enter the eigth number: "))
    int9 = int(input("Enter the ninth number: "))
    int10 = int(input("Enter the tenth number: "))
    int11 = int(input("Enter the eleventh number: "))
    int12 = int(input("Enter the twelvth number: "))
    int13 = int(input("Enter the last number: "))
    list_answer = [int1,int2,int3,int4,int5,int6,int7,int8,int9,int10,int11,int12,int13]
print()

correct_answer_easy = [71,111,111,100,32,74,111,98,33]
                       #G  o   o   d      J  o  b  !
correct_answer_hard = [87,111,119,33,32,65,109,97,122,105,110,103,33]
                       #W  o   w  !     A   m  a   z  i   n    g   !
if list_answer == correct_answer_easy or list_answer == correct_answer_hard:
    list_letters = []
    for number in list_answer:
        list_letters += [chr(number)]
    message = ''.join(list_letters)
    print('Unicode code points:',list_answer)
    print(f"This displays: '{message}'")
else:
    print(list_answer)
    print("Review your inputs!")