
# AUFGABE 1

def power(a, b):
	if b == 0:
		return 1
	elif a < 0 or b < 0:
		return -1
	else:
		return a * power(a, b-1)

a = 2
b = 4

print(power(a, b))



# AUFGABE 2

def binary_search(numbers, num, start, end):
	if end >= start:                              # account for end being a lower number than start
		mid_num = start + (end-start) % 2         # set mid point to start binary search
		if numbers[mid_num] == num:
			return mid_num                        # return mid point if already the searched number
		elif numbers[mid_num] < num:
			return binary_search(numbers, num, mid_num + 1, end)       # recursive: loop through the list again with mid point +1
		elif numbers[mid_num] > num:
			return binary_search(numbers, num, start, mid_num - 1)     # same, but accounting for other direction
		else:
			return -1                             # return -1 if number not in list
	else:
		return -1


numbers = [3, 5, 7, 11, 13, 17, 19, 23, 29]
num = 5

final = binary_search(numbers, num, 0, len(numbers)-1)            # set how often we want to loop through the recursive function

if final == -1:
	print("The number is not in the list")
else:
	print("The number " + str(num) + " is at index position " + str(final) + ".")



# AUFGABE 3 bis 7:

class HashTable:
	def __init__(self, size = 10):
		self.size = size
		self.buckets = [[  ] for x in range(self.size)]

	def __my_hash(self, element):
		if type(element) is str:
			return len(element) % self.size
		if type(element) is int:
			return element % self.size

	def insert(self, element):
		self.buckets[self.__my_hash(element)].append(element)
		print(self.buckets)

	def get_element(self, element):
		for liste in self.buckets:
			if element in liste:
				liste.remove(element)
				return element
			else:
				return False

	def get_size(self):
		length = 0
		for liste in self.buckets:
			for element in liste:
				length += 1
		return length + self.size



my_ht = HashTable(size=8)

print(my_ht.buckets)
print(my_ht.insert(32))
print(my_ht.insert("Hallo Servus Grüß Dich"))
print(my_ht.insert("seventeen letters"))
print(my_ht.insert(17))
print(my_ht.get_element(32))
print(my_ht.buckets)
print(my_ht.get_size())