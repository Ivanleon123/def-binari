def binari_a_enters(binari):
    """Converteix un número binari (cadena) a un enter."""
    try:
        return int(binari, 2)  # Converteix de binari a enter
    except ValueError:
        return "Entrada no vàlida, si us plau, introduïu un número binari."

# Proves de la funció
print(binari_a_enters("101"))      # Retorna 5
print(binari_a_enters("1101"))     # Retorna 13
print(binari_a_enters("10000"))    # Retorna 16
print(binari_a_enters("2"))        # Retorna "Entrada no vàlida, si us plau, introduïu un número binari."
print(binari_a_enters("abc"))      # Retorna "Entrada no vàlida, si us plau, introduïu un número binari."