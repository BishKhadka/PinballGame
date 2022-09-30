"""Stacy Doore
Fall 2021
CS 152
wordmap.py"""

def main():
	print("Please play  word association game with me!" + "\n" +
              "I will say a word and you will type the first work that comes to your mind.")
	words = ["yes ","no ","ice cream ","phone ","lab ","8 ","tired ","water bottle ","gum ","yesterday "]
	mapping = {}
	for word in words:
		response = input(word)
		mapping[word] = response
	for key in mapping.keys():
		print(key + " = " + mapping.get(key))
main()
