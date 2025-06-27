# online_sales_analysis
analizarea datelor de vanzari
# Aplicație de gestionare a inventarului


## Funcționalități
- Adăugare produse în inventar
- Modificare denumiri și cantități
- Ștergere și filtrare produse
- Adăugare produse în coșul de cumpărături
- Salvare configurații locale (`config.json`)

## Clase utilizate

### `Product`
Reprezintă un produs, are atribute precum nume și cantitate.

### `Inventory`
Gestionează lista de produse și oferă metode de adăugare, modificare și afișare.

### `Cart`
Permite adăugarea produselor selectate într-un coș de cumpărături și calculează totalul.

## Configurare
- Setările aplicației (ex: cheia API sau adresa bazei de date) sunt definite în `config.json`, fișier care este exclus din versionare cu `.gitignore`.

## Lansare
Rulează aplicația cu:
```bash
python main.py

