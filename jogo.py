"""
Ola, eu sou xxxp3dro criado desse programa ainda sou novato em python mais estou aprendo. :) 
"""
import random
import os
import time

lista2 = "(pedra) (papel) ou (tesoura)"

while True:
	os.system("clear")
	jogando = input(f"[Você] Escolher {lista2}: ")
	if True:
		print("--------------------(BOT)--------------------")
		print("")
		
		i = random.choice(("pedra","papel","tesoura"))
		print(f"BOT: {i}")
		print("")
		time.sleep(0.8)