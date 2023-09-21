def letterFrequency(x):
    letters = sorted("".join((x.split())))
    cnt = dict.fromkeys(letters)
    for i in cnt.keys():
        count = 0
        for j in letters:
            if j == i:
                count +=1
            cnt[i] = count
    print(f"The count of each letter in the sentence is {cnt}.")

letterFrequency(input("Enter a sentence: ")) 
