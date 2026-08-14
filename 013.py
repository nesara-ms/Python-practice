'''WAP to check whether a given word is a palindrome or not.'''
def is_palindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")