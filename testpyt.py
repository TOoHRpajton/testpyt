cislo_list = [1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5]
unikatni_cisla = set(cislo_list)
print("Unikátní čísla:", unikatni_cisla)
print("Původní seznam:", cislo_list)

prazdna_mnozina = set()
prazdna_mnozina.add(58)
prazdna_mnozina.add(99)
print("Množina po přidání prvků:", prazdna_mnozina)

if 3 in unikatni_cisla:
    print("Číslo 3 je v množině unikátních čísel.") 
else:
    print("Číslo 3 ---NENÍ--- v množiě uikátních čísel.")   