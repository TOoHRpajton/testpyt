import math
print(f"Číslo PI: {math.pi}")
print(f"Sinus 90 stupňů: {math.sin(math.pi/2)}")

def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"Chyba: {zde}")
        return None
    except Exception as e:
        zprava = f"Nelze dělit objekt {a} / {b}: {e}"
        raise Exception(zprava) from e
    finally:
        print("Dělení bylo provedeno.")
        print("tento blok se provede vždy")
    return vysledek

print(bezpecne_deleni(10,2))
print(bezpecne_deleni(10,0))
