# Dokumentacja API

## Endpointy

### Dodawanie nowego przepisu
- **URL:** `/recipes/`
- **Metoda:** `POST`
- **Opis:** Tworzy nowy przepis na podstawie przesłanych danych.
- **Body:**
  ```json
  {
    "name": "Nazwa przepisu",
    "ingredients": "Lista składników jako string",
    "content": "Treść przepisu"
  }
  ```
- **Odpowiedź:** Zwraca utworzony przepis z przypisanym ID.

### Pobieranie przepisu
- **URL:** `/recipes/{recipe_name}`
- **Metoda:** `GET`
- **Opis:** Pobiera przepis na podstawie jego nazwy.
- **Parametry URL:** `recipe_name `- nazwa przepisu
- **Odpowiedź:** Zwraca szczegóły przepisu, jeśli zostanie znaleziony.

### Usuwanie przepisu
- **URL:** `/recipes/{recipe_name}`
- **Metoda:** `DELETE`
- **Opis:** Usuwa przepis na podstawie jego nazwy.
- **Parametry URL:** `recipe_name` - nazwa przepisu
- **Odpowiedź:** Potwierdzenie usunięcia przepisu.

## Modele

### `RecipeCreate`
**Opis:** Model używany do tworzenia nowego przepisu.
**Pola:**
- `name`: Nazwa przepisu (string)
- `ingredients`: Składniki przepisu jako ciąg znaków (string)
- `content`: Treść przepisu (string)

### `Recipe`
**Opis:** Model używany do prezentacji przepisu.
**Pola:**
- `id`: ID przepisu (integer)
- `name`: Nazwa przepisu (string)
- `ingredients`: Składniki przepisu jako ciąg znaków (string)
- `content`: Treść przepisu (string)
