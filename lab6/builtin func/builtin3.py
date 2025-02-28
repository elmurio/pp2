input_str = input("Enter a string: ")

cleaned_str= input_str.replace(" ", "").lower()

reversed_str = ''.join(reversed(cleaned_str))

is_palindrome = cleaned_str == reversed_str

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
