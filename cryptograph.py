from random import *
import random
import random2
from tqdm import tqdm
import time

#Text_1
print("""
Easy Crypto Algorithm"
----------------------------
Es werden nur ganze Zahlen Akzeptiert
""")

#Password input

passwd_user = input("Gib dein Passwort ein: ")
lenght = input("Wie Lange soll dein Passwort sein?: ")

length_passwd = len(passwd_user)

passwd_user = int(passwd_user)
lenght = int(lenght)




zahl_1 = (int(str(passwd_user)[:1]))
zahl_2 = (int(str(passwd_user)[:2]))
zahl_3 = (int(str(passwd_user)[:3]))
zahl_4 = (int(str(passwd_user)[:4]))
zahl_5 = (int(str(passwd_user)[:5]))
zahl_6 = (int(str(passwd_user)[:6]))

random2.seed(62500)
generate_random_key = random2.randint(1, 512)


number_nfol = zahl_1 * zahl_2 * zahl_3 * zahl_4 * zahl_5 * zahl_6

calcs = [number_nfol ** generate_random_key, number_nfol ** length_passwd, generate_random_key ** length_passwd]

for i in tqdm(calcs):
    time.sleep(2)
#key_phrase = number_nfol ** generate_random_key ** length_passwd 

n_0 = calcs[0]
n_1 = calcs[1]
n_2 = calcs[2]  

calcs_2 = [n_0 * n_1, n_0 * n_2, n_1 * n_2]

for i in tqdm(calcs_2):
    time.sleep(2)
    
k_0 = calcs_2[0]
k_1 = calcs_2[1]
k_2 = calcs_2[2]

#Kürzen

calc_f = k_0 + k_1 + k_2
l_calc = len(str(calc_f))
l_calc = int(l_calc)
plus_calc = l_calc - int(lenght)
#print(plus_calc)

neg_int = plus_calc * -1
#print(neg_int)
calc_f = int(str(calc_f)[:neg_int])

print("Dein Verschlüsseltes Passwort ist: ", calc_f)

