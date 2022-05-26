# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # checks if the lengths of words are the same and sorts them
    if(len(word) == len(anagram)):
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)
        # checks if the sorted words are the same
        if(sorted_anagram == sorted_word):
            return True
        else:
            return False
    else:
        return False
print(find_anagram('sweat', 'weats'))


    

