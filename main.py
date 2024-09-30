'''takes the input from the user and stores it in the variable S'''
S = input('Enter a string: ')

'''The methods will check the variable S for certain criteria
and display true or false depending on the method provided'''
print('The input had all alphanumeric characters:', S.isalnum())
print('The input had all alphabetical characters:', S.isalpha())
print('The input had all digits:', S.isdigit())
print('The input had lowercase letters:', S.islower())
print('The input had uppercase letters:', S.isupper())
