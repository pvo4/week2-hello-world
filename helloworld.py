# Phillip Vo

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

print('What is your name?')		
myName = input()
print()
print('It is a pleasure to meet you, ' + myName +'!')
print()
print('Choose a language and I will greet you in that language!')
print('1. Russian')
print('2. Japanese')
print('3. Vietnamese')
print()
number = input()			#Ask the user to input one of the three choices
print()
if number == '1':			#I used an if, elif and else statement to get the desire response
	print('Zdravstvuyte')	#If the user inputs 1, the greeting will be in Russian
elif number == '2':			#If the user inputs 2, greeting will be in Japanese and 3 for Vietnamese
	print('Konnichiwa')
elif number == '3':
	print('Chao ban')
else:
	print('You did not input the correct number, try again.')	#If the user inputs any response other than 1,2, or 3 the program will tell them to try again