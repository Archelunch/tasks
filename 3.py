exclude = list("aeiou")
result = []
phrase = "The quick onyx goblin jumps over the lazy dwarf"
for i in phrase:
	if not i in exclude and not i in result:
		result.append(i)
print(result)
