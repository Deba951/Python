# Finding Uncommon Words from Two Sentences Using Python

def words(s1, s2):
    words1 = s1.split()
    words2 = s2.split()

    counts = {}
    for word in words1 + words2:
        counts[word] = counts.get(word, 0) + 1

    uncommon = [word for word in counts if counts[word] == 1]
    return uncommon

s1=str(input("Enter the first sentence: "))
s2=str(input("Enter the second sentence: "))
print(words(s1, s2))