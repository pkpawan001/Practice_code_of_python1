S1 = input("First pharase")
S2 = input("Enter second pharase")

S1 = S1.lower()
S2 = S2.lower()

# TODO: Write a for loop to check each letter and compare counts. If any mismatch, print 'not anagrams' and break.
for x in S1:
    if x.isalpha():
        if S1.count(x)!=S2.count(x):
            print("Not Anagrams")
            break

else:
    print('Anagrams')