def reverser_1(x):
	return x + (x % 2) + ((x % 2) - 1)


def reverser_2(x):
	return 3-x


print("First method")
print(reverser_1(1))
print(reverser_1(2))
print("Second method")
print(reverser_2(1))
print(reverser_2(2))
