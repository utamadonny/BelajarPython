# print(2*2)

#%% function
def func1():
	print("func1")

func1()

#%% function with parameter
def func2(a, b):
	print(a, " ", b)

func2(1, 2)

# function with default parameter
def power(x, y=2):
	return x**y

print(power(2)) 
print(power(2, 3))

# %% function with variable number of parameter
def add(*args):
	sum = 0
	for n in args:
		sum += n
	return sum

add(1, 2, 3, 4, 5)
#%% conditional 
def max_num(a, b):
	if a > b:
		return a
	else:
		return b

#%% Polindrome

def is_palindrome(s):
	if s == s[::-1]:
		return True
	return False

run = True
while (run):
	s = input("Enter a string: ")
	
	if s == "exit":
		run = False
		break

	s = s.lower()
	s = s.replace(" ", "")
	s = s.replace(".", "")
	s = s.replace(",", "")
	s = s.replace("!", "")
	s = s.replace("?", "")
	s = s.replace(";", "")
	s = s.replace(":", "")
	s = s.replace("(", "")
	s = s.replace(")", "")
	s = s.replace("[", "")
	s = s.replace("]", "")
	s = s.replace("{", "")

	print("Result : ", is_palindrome(s))

# %%
