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

cislo_textu = int(input('Choose text to analyze (1 - 3): ')) - 1
print('-' * 40)
print('Selected text: \n')

if cislo_textu == 0:
    print(TEXTS[cislo_textu])
elif cislo_textu == 1:
    print(TEXTS[cislo_textu])
elif cislo_textu == 2:
    print(TEXTS[cislo_textu])
else:
    print('You can only enter a number between 1 - 3. \n'
          'Start again.'
          )
    quit()
print('-' * 40)

########################-ANALYZOVÁNÍ TEXTU-########################

print("The selected text contains: \n")

# == Počet slov == #
for slova in TEXTS[cislo_textu]:
    slova = len(TEXTS[cislo_textu].split())

if slova > 1:
    print(f'There are {slova} words in the selected text.')
else:
    print(f'There is {slova} word in the selected text.')

# == Počet slov začínajících velkým písmenem == #
nazvy_cislo = list()

for nazvy in TEXTS[cislo_textu].split():
    if nazvy.istitle():
        nazvy_cislo.append(nazvy)

nazvy_cislo = len(nazvy_cislo)

if nazvy_cislo > 1:
    print(f'There are {nazvy_cislo} titlecase words.')
elif nazvy_cislo == 0:
    print("There aren't any titlecase words.")
else:
    print(f'There is {nazvy_cislo} titlecase word.')

# == Počet slov psaných VELKÝMI písmeny == #
velka_pismena = list()

for velka in TEXTS[cislo_textu].split():
    if velka.isupper() and velka.isalpha():
        velka_pismena.append(velka)

velka_pismena = len(velka_pismena)

if velka_pismena > 1:
    print(f'There are {velka_pismena} uppercase words.')
elif velka_pismena == 0:
    print("There aren't any uppercase words.")
else:
    print(f'There is {velka_pismena} uppercase word.')

# == Počet slov psaných MALÝMI písmeny == #
mala_pismena = list()

for mala in TEXTS[cislo_textu].split():
    if mala.islower():
        mala_pismena.append(mala)

mala_pismena = len(mala_pismena)

if mala_pismena > 1:
    print(f'There are {mala_pismena} lowercase words.')
elif mala_pismena == 0:
    print("There aren't any lowercase words.")
else:
    print(f'There is {mala_pismena} lowercase word.')

# == Počet čísel v textu == #
cisla = list()

for cislo in TEXTS[cislo_textu].split():
    if cislo.isdigit():
        cisla.append(cislo)

cisla = len(cisla)

if cisla > 1:
    print(f'There are {cisla} numeric strings.')
elif cisla == 0:
    print("There aren't any numeric strings.")
else:
    print(f'There is {cisla} numeric string.')

# == SUMA všech čísel v textu == #
suma = list()

for cislo_1 in TEXTS[cislo_textu].split():
    if cislo_1.isdigit():
        suma.append(cislo_1)

soucet = sum(int(x) for x in suma) 

if soucet != 0:
    print(f'The sum of all the numbers {soucet}.')
else:
    print('There are no numbers to count.')

print('-' * 40)

########################-Graf počtu slov podle znaků-########################

print('LEN|', '\tOCCURENCES', '\t|NR.')
print('-' * 40)

pocet_zn = {'zn_1': [], 'zn_2': [], 'zn_3': [], 'zn_4': [], 
            'zn_5': [], 'zn_6': [], 'zn_7': [], 'zn_8': [], 
            'zn_9': [], 'zn_10': [], 'zn_11': [], 'zn_12': [],
            'zn_13': []
            }

for pocet in TEXTS[cislo_textu].split():
    if pocet.endswith('.') or pocet.endswith(','):
        pocet = pocet[:-1]
    if len(pocet) == 1:
        pocet_zn['zn_1'].append(pocet)
    elif len(pocet) == 2:
        pocet_zn['zn_2'].append(pocet)
    elif len(pocet) == 3:
        pocet_zn['zn_3'].append(pocet)
    elif len(pocet) == 4:
        pocet_zn['zn_4'].append(pocet)
    elif len(pocet) == 5:
        pocet_zn['zn_5'].append(pocet)
    elif len(pocet) == 6:
        pocet_zn['zn_6'].append(pocet)
    elif len(pocet) == 7:
        pocet_zn['zn_7'].append(pocet)
    elif len(pocet) == 8:
        pocet_zn['zn_8'].append(pocet)
    elif len(pocet) == 9:
        pocet_zn['zn_9'].append(pocet)
    elif len(pocet) == 10:
        pocet_zn['zn_10'].append(pocet)
    elif len(pocet) == 11:
        pocet_zn['zn_11'].append(pocet)
    elif len(pocet) == 12:
        pocet_zn['zn_12'].append(pocet)
    elif len(pocet) == 13:
        pocet_zn['zn_13'].append(pocet)



if len(pocet_zn['zn_1']) >= 1:
    if len(pocet_zn['zn_1']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_1']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  1|' + '*' * len(pocet_zn['zn_1']), odsazeni  + '|',
           len(pocet_zn['zn_1']), sep = ''
           )

if len(pocet_zn['zn_2']) >= 1:
    if len(pocet_zn['zn_2']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_2']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  2|' + '*' * len(pocet_zn['zn_2']), odsazeni  + '|',
           len(pocet_zn['zn_2']), sep = ''
           )

if len(pocet_zn['zn_3']) >= 1:
    if len(pocet_zn['zn_3']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_3']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  3|' + '*' * len(pocet_zn['zn_3']), odsazeni  + '|',
           len(pocet_zn['zn_3']), sep = ''
           )

if len(pocet_zn['zn_4']) >= 1:
    if len(pocet_zn['zn_4']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_4']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  4|' + '*' * len(pocet_zn['zn_4']), odsazeni  + '|',
           len(pocet_zn['zn_4']), sep = ''
           )

if len(pocet_zn['zn_5']) >= 1:
    if len(pocet_zn['zn_5']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_5']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  5|' + '*' * len(pocet_zn['zn_5']), odsazeni  + '|',
           len(pocet_zn['zn_5']), sep = ''
           )

if len(pocet_zn['zn_6']) >= 1:
    if len(pocet_zn['zn_6']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_6']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  6|' + '*' * len(pocet_zn['zn_6']), odsazeni  + '|',
           len(pocet_zn['zn_6']), sep = ''
           )

if len(pocet_zn['zn_7']) >= 1:
    if len(pocet_zn['zn_7']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_7']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  7|' + '*' * len(pocet_zn['zn_7']), odsazeni  + '|',
           len(pocet_zn['zn_7']), sep = ''
           )
    
if len(pocet_zn['zn_8']) >= 1:
    if len(pocet_zn['zn_8']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_8']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  8|' + '*' * len(pocet_zn['zn_8']), odsazeni  + '|',
           len(pocet_zn['zn_8']), sep = ''
           )
    
if len(pocet_zn['zn_9']) >= 1:
    if len(pocet_zn['zn_9']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_9']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print('  9|' + '*' * len(pocet_zn['zn_9']), odsazeni  + '|',
           len(pocet_zn['zn_9']), sep = ''
           )
    
if len(pocet_zn['zn_10']) >= 1:
    if len(pocet_zn['zn_10']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_10']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print(' 10|' + '*' * len(pocet_zn['zn_10']), odsazeni  + '|',
           len(pocet_zn['zn_10']), sep = ''
           )
    
if len(pocet_zn['zn_11']) >= 1:
    if len(pocet_zn['zn_11']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_11']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print(' 11|' + '*' * len(pocet_zn['zn_11']), odsazeni  + '|',
           len(pocet_zn['zn_11']), sep = ''
           )
    
if len(pocet_zn['zn_12']) >= 1:
    if len(pocet_zn['zn_12']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_12']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print(' 12|' + '*' * len(pocet_zn['zn_12']), odsazeni  + '|',
           len(pocet_zn['zn_12']), sep = ''
           )
    
if len(pocet_zn['zn_13']) >= 1:
    if len(pocet_zn['zn_13']) < 4:
        odsazeni = '\t' * 3
    elif len(pocet_zn['zn_13']) < 12:
        odsazeni = '\t' * 2
    else:
        odsazeni = '\t'
    print(' 13|' + '*' * len(pocet_zn['zn_13']), odsazeni  + '|',
           len(pocet_zn['zn_13']), sep = ''
           )
    
