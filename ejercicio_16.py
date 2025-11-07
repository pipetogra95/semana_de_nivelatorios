addition=0
word=input("Enter a word\n")
for w in word:
	if w=="a" or w=="e" or w=="i" or w=="o" or w=="u":
		addition=addition+1
print(f"in you word there are {addition} vowels\n")
