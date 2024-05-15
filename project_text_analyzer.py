"""
project_text_analyzer.py: první projekt do Engeto Online Python Akademie

author: Daniel Čudovský
email: daniel.cudovsky@gmail.com
discord: dannyxc12

"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

###############-UVÍTÁNÍ DO PROGRAMU-###############

print('#' * 40)
print('Welcome to a text analyzer app! \n',
      'To continue please login. \n',
       '-' * 40, sep=''
      )

#-----UZIVATELÉ----------#

users = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'
         }

###############-PŘIHLÁŠENÍ UŽIVATELE-###########################

uzivatel = input('Enter your username: ').lower()
heslo = input('Enter your password: ')

print('-' * 40) 

if uzivatel in users.keys() and heslo == users[uzivatel]:
    print(f'\tLogin succesful! \n \tWelcome user {uzivatel.title()}! \n', '-' * 40, sep = '')
else:
    print('Username or password is NOT correct. \n',
          '\tTerminating the app...'
          )
    quit()

######################-VÝBĚR TEXTU-################################

print('Now select a text you want to analyze.')

pocet_textu = len(TEXTS)

cislo_textu = int(input(f'Choose text to analyze (1 - {pocet_textu}): ')) - 1
print('-' * 40)
print('Selected text: \n')


for vybrany_text in TEXTS:
    if cislo_textu < pocet_textu:
        print(TEXTS[cislo_textu])
        break
    else:
        print(f'You can only enter a number between 1 - {pocet_textu}. \n'
          'Start again.'
          )
        quit()
print('-' * 40)

########################-ANALYZOVÁNÍ TEXTU-########################

print("The selected text contains: \n")

slova = 0
nazvy_cislo = 0
velka_pismena = 0
mala_pismena = 0
cisla = 0
suma = []
symboly = (",", ".", ":", "!", "?")

for pocty in TEXTS[cislo_textu].split():
    slova += 1
    if pocty.endswith(symboly):
        pocty = pocty[:-1]
    if pocty.istitle():
        nazvy_cislo += 1
    if pocty.isupper() and pocty.isalpha():
        velka_pismena += 1
    if pocty.islower():
        mala_pismena += 1
    if pocty.isdigit():
        cisla += 1
        suma.append(int(pocty))

if slova > 1:
    print(f'There are {slova} words in the selected text.')
else:
    print(f'There is {slova} word in the selected text.')

if nazvy_cislo > 1:
    print(f'There are {nazvy_cislo} titlecase words.')
elif nazvy_cislo == 0:
    print("There aren't any titlecase words.")
else:
    print(f'There is {nazvy_cislo} titlecase word.')

if velka_pismena > 1:
    print(f'There are {velka_pismena} uppercase words.')
elif velka_pismena == 0:
    print("There aren't any uppercase words.")
else:
    print(f'There is {velka_pismena} uppercase word.')

if mala_pismena > 1:
    print(f'There are {mala_pismena} lowercase words.')
elif mala_pismena == 0:
    print("There aren't any lowercase words.")
else:
    print(f'There is {mala_pismena} lowercase words.')

if cisla > 1:
    print(f'There are {cisla} numeric strings.')
elif cisla == 0:
    print("There aren't any numeric strings.")
else:
    print(f'There is {cisla} numeric string.')

if suma:
    print(f'The sum of all the numbers {sum(suma)}.')
else:
    print('There are no numbers to count.')

print('-' * 40)

########################-Graf počtu slov podle znaků-########################

print('LEN|', '\tOCCURENCES', '\t|NR.')
print('-' * 40)

pocet_zn = {}

for slovo in TEXTS[cislo_textu].split():
    if slovo.endswith(symboly):
        slovo = slovo[:-1]
    delka_slova = len(slovo)
    if delka_slova not in pocet_zn:
        pocet_zn[delka_slova] = []
    pocet_zn[delka_slova].append(slovo)

serazene_delky = sorted(pocet_zn.keys())

for delka in serazene_delky:
    slova = pocet_zn[delka]
    if len(slova) >= 1:
        if len(slova) < 4:
            odsazeni = '\t' * 3
        elif len(slova) < 12:
            odsazeni = '\t' * 2
        else:
            odsazeni = '\t'
        print(f'{delka:3}|{"*" * len(slova)}{odsazeni}|{len(slova)}')

print('-' * 40)
