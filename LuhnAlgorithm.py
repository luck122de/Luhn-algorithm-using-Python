def varify_card_number(card_number):
    reverse_card_number=card_number[::-1]
    Sum_odd_digits=0
    odd_digits=reverse_card_number[::2]
    for digit in odd_digits:
        Sum_odd_digits += int(digit)
    Sum_even_digits=0
    even_digits=reverse_card_number[1::2]
    for digit in even_digits:
        number= int(digit)*2
        if number>=10:
            number= (number//10) + (number%10)
        Sum_even_digits +=number
    total=Sum_odd_digits + Sum_even_digits
    print(total)
    return total%10==0



def main():
    card_number = '4111-1111-4958-1244'
    card_number_translation=str.maketrans({'-':'',' ':''})
    translated_card_number=card_number.translate(card_number_translation)
    if varify_card_number(translated_card_number):
        print('valid!')
    else:
        print('Invalid!')
main()