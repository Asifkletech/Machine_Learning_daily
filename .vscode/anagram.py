str1="listen"
str2="silent"

if (sorted(str1))==(sorted(str2)):
    print("it is Anagram")

else:
    print("it is not a Anagram")
    
    

from collections import defaultdict

def group_anagrams(words: list) -> dict:
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return dict(anagrams)

# Example usage:
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

