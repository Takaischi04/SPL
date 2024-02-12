# Zähle die geraden Ziffern zwischen 1 und 1000 zusammen - Tip: Starte den Loop bei 2 und erhöhe den Zählindex jeweils um 2.
for value in range(1, 1001):
    if value %2 == 0:
        print(value)