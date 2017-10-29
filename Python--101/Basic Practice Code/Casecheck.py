# This program will check the case of the character and change it
character = raw_input ("")
p = ord(character)
if p >= 65 and p <= 90:
	print ("Upper Case")
	print character.lower()
elif p >= 97 and p <= 122:
	print ("Lower Case")
	print character.upper()
else:
	print ("Special Character")