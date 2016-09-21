"""
Banner maker
From http://usingpython.com/python-programming-challenges/
"""

userName = input("What's your name?")
bannerName = ("* " + userName + " *")
print("-" * len(bannerName) + "\n\n")
print(bannerName + "\n\n")
print("-" * len(bannerName))

