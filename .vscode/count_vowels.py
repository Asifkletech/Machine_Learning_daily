vowel=['a',"e","i","o","u"]
count=0
word="programming"

for character in word:
    if character in vowel:
        
        count+=1

print(count)