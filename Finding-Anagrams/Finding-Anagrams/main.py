# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if (len(word) == len(anagram)):
        word = word.lower()
        anagram = anagram.lower()

        word_list = sorted(word)
        anagram_list = sorted(anagram)

        if(word_list == anagram_list):
            return True

    else:
        return False


if __name__ == '__main__':
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")
    print(find_anagram(str1, str2))