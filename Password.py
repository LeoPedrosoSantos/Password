import random

L = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
S = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generetor!")
NL = int(input("How many letter woud you like in your password?\n"))
NN = int(input(f"How many numbers would you like?\n"))
NS = int(input(f"How many symbols would you like?\n"))

PL = []

for Char in range(0, NL):
    PL += random.choice(L)

for Char in range(0, NN):
    PL += random.choice(N)

for Char in range(0, NS):
    PL += random.choice(S)

random.shuffle(PL)

Password = ""

for Char in PL:
    Password += Char

print(f"\nSua senha nova é: {Password}\n")

Exit = input("\nClick ENTER to finish the generation!")