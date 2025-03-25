# program to check if the entered word is plaindrome or not

word = input("Enter a word or sentence: ")

palindrome_word = word.replace(" ", "").lower()

reversed_word = palindrome_word[::-1]

if palindrome_word == reversed_word:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")