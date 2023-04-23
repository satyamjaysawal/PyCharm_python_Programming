def is_Palindrome(string):
    return string[::-1] == string
word = input("enter a word gor check is palindrome or not :")
if is_Palindrome(word):
    print("{} is palindrome".format(word))
else:
    print("{} is not palindrome".format(word))
