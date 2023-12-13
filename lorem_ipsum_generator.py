import random
import time


# Seznam obsahující kombinace všech písmen abecedy a k nim jsou postupně přiřazeny všechny jednotlivé samohlásky. Kombinace slabik o dvou písmenech.
slabiky = ['aa', 'ae', 'ai', 'ao', 'au',
           'ba', 'be', 'bi', 'bo', 'bu',
           'ca', 'ce', 'ci', 'co', 'cu',
           'da', 'de', 'di', 'do', 'du',
           'ea', 'ee', 'ei', 'eo', 'eu',
           'fa', 'fe', 'fi', 'fo', 'fu',
           'ga', 'ge', 'gi', 'go', 'gu',
           'ha', 'he', 'hi', 'ho', 'hu',
           'ia', 'ie', 'ii', 'io', 'iu',
           'ja', 'je', 'ji', 'jo', 'ju',
           'ka', 'ke', 'ki', 'ko', 'ku',
           'la', 'le', 'li', 'lo', 'lu',
           'ma', 'me', 'mi', 'mo', 'mu',
           'na', 'ne', 'ni', 'no', 'nu',
           'oa', 'oe', 'oi', 'oo', 'ou',
           'pa', 'pe', 'pi', 'po', 'pu',
           'qa', 'qe', 'qi', 'qo', 'qu',
           'ra', 're', 'ri', 'ro', 'ru',
           'sa', 'se', 'si', 'so', 'su',
           'ta', 'te', 'ti', 'to', 'tu',
           'ua', 'ue', 'ui', 'uo', 'uu',
           'va', 've', 'vi', 'vo', 'vu',
           'wa', 'we', 'wi', 'wo', 'wu',
           'xa', 'xe', 'xi', 'xo', 'xu',
           'ya', 'ye', 'yi', 'yo', 'yu',
           'za', 'ze', 'zi', 'zo', 'zu']


# Uživatel zadává počet vět, maximální a minimální délku vět.
while True:
    try:
        print()
        pocet_vet = int(input("Zadejte počet vět: "))
        time.sleep(0.2)
        print()
        
        max_delka_vety = int(input("Zadejte maximální počet slov ve větě: "))
        time.sleep(0.2)
        print()
        
        min_delka_vety = int(input("Zadejte minimální počet slov ve větě: "))
        time.sleep(0.2)
        print()


# Kontrola, zda je maximální délka věty větší nebo rovna minimální délce věty a jestli není zadaný znak jiný než číslice.     
        if max_delka_vety >= min_delka_vety:
            break
        
        else:
            print("Maximální počet slov ve větě nemůže být menší než minimální počet slov ve větě.")
            time.sleep(0.2)

    except ValueError:
        print("Zadaná hodnota nemůže být nic jiného než číslo. Zadejte kladné celé číslo.")
        time.sleep(0.2)       


# Uživatel zadává maximální a minimální délku slova.
while True:
    try:
        max_delka_slova = int(input("Zadejte maximální délku slova. (Vámi zadané číslo je maximální počet slabik ve slově): "))
        time.sleep(0.2)
        print()
        
        min_delka_slova = int(input("Zadejte minimální délku slova. (Vámi zadané číslo je minimální počet slabik ve slově): "))
        time.sleep(0.2)
        print()


# Kontrola, zda je maximální délka slova větší nebo rovna minimální délce slova a jestli není zadaný znak jiný než číslice.        
        if max_delka_slova >= min_delka_slova:
            break
        
        else:
            print("Maximální délka slova nemůže být menší než minimální délka slova.")
            time.sleep(0.2)
            
    except ValueError:
        print("Zadaná hodnota nemůže být nic jiného než číslo. Zadejte kladné celé číslo.")
        time.sleep(0.2)


# Seznam pro uchování vytvořených slov, který se používá v generování náhodných vět.     
vytvorena_slova = []


# Generování náhodných slov.
for slova in range(len(slabiky)):

    delka_jednoho_slova = random.randint(min_delka_slova, max_delka_slova)

    nahodne_slovo = random.sample(slabiky, delka_jednoho_slova)

    slovo = ''.join(nahodne_slovo)

    vytvorena_slova.append(slovo)


# Generování náhodných vět.
for vety in range(pocet_vet):
    
    pocet_vytvorenych_slov = len(vytvorena_slova)

    max_pocet_slov = min(max_delka_vety, pocet_vytvorenych_slov)

    nahodny_pocet_slov = random.randint(min_delka_vety, max_pocet_slov)

    nahodne_vety = random.sample(vytvorena_slova, nahodny_pocet_slov)

    veta = ' '.join(nahodne_vety)

    veta = veta.capitalize()

    print(f"{veta}.")

    

