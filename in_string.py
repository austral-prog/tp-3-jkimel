def check_vowels():
    name = input("Ingrese un nombre: ")
    name_lower = name.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for vowel in vowels:
        print(f"Contiene {vowel}: {vowel in name_lower}")
check_vowels()
