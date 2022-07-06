# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value 
# for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?


lst = []
alpha = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
fopen = open("file.txt","r")
fopen = fopen.read()
words = fopen.split(",")
words.sort()
lst.append(words)
scores = 0

for word in lst:
    for i in range(0,len(word)):
        num = i+1
        wrd = word[i]
        sum_Index = 0
        for letter in wrd:
            if letter != '"':
                ind = alpha.index(letter)
                sum_Index += ind
        scores += sum_Index * num

print(scores)
