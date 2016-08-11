"""
attempt to create from scratch a simplistic caeser cipher generator
"""
def caeserCipher(input,key):
		alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		print(len(alpha))
		new = []
		for x in input:
			new.append(alpha[(alpha.index(x) + key) % 26])
		new = "".join(new)
		print(new)
caeserCipher("meme",3)
