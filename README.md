
## What the Program Does

This is a **Library Management System** built in Python.  
The user registers one **physical book** and one **digital book (eBook)**, performs actions on them (borrow, return, download), and gets a full summary at the end.

The program demonstrates:
- Correct use of Python data types and input validation
- Object-Oriented Programming with inheritance
- Magic methods (dunder methods)
- Python decorators (`@classmethod`, `@staticmethod`, `@property`)

---

## Classes

### `Book` (Parent class)
Represents a physical book in the library.

| Member | Type | Description |
|---|---|---|
| `title` | `str` | Title of the book |
| `author` | `str` | Author's name |
| `pages` | `int` | Number of pages |
| `price` | `float` | Price in FCFA |
| `available` | `bool` | Whether the book is available |
| `__str__()` | magic method | Human-readable string representation |
| `__eq__()` | magic method | Compare two books by title |
| `__len__()` | magic method | `len(book)` returns number of pages |
| `get_total_books()` | `@classmethod` | Returns total books created |
| `is_valid_price()` | `@staticmethod` | Checks if a price is valid (> 0) |
| `borrow()` | method | Marks the book as borrowed |
| `return_book()` | method | Marks the book as returned |

### `DigitalBook(Book)` (Child class)
Inherits from `Book`. A `DigitalBook` **IS A** `Book`.  
Adds digital-specific features.

| Member | Type | Description |
|---|---|---|
| `file_size_mb` | `float` | File size in megabytes |
| `file_format` | `str` | Format: PDF, EPUB, MOBI… |
| `size_in_kb` | `@property` | Computed size in KB (no parentheses needed) |
| `download()` | method | Simulates downloading the eBook |

---

## How to Run

**Requirements:** Python 3.10 or higher — no external libraries needed.

```bash
# Clone the repository
git clone https://github.com/Ednik75/advanced_programming_group11
cd advanced_programming_group11

# Run the program
python main.py
```

The program will prompt you to enter details for two books interactively.  
All inputs are validated — the program will re-prompt on invalid entries and never crash.

---

## Example Output

```
============================================================
    LIBRARY MANAGEMENT SYSTEM
   PRG1406 — Group Assignment 1
============================================================

── Register a Physical Book ────────────────────────────
  Book title              : The Little Prince
  Author                  : Antoine de Saint-Exupery
  Number of pages         : 96
  Price (FCFA)            : 12.99
  Available? (yes/no)     : yes

── Register a Digital Book (eBook) ─────────────────────
  Book title              : Python Crash Course
  Author                  : Eric Matthes
  Number of pages         : 544
  Price (FCFA)            : 29.99
  Available? (yes/no)     : yes
  File size (MB)          : 12.5
  Format (PDF/EPUB/MOBI)  : PDF

── Book Actions ────────────────────────────────────────
   'The Little Prince' has been borrowed successfully.
    Downloading 'Python Crash Course' (PDF, 12.5 MB)...
   Download complete!
   'The Little Prince' has been returned successfully.

── Magic Methods Demo ──────────────────────────────────
  len(physical book)    = 96 pages
  len(digital book)     = 544 pages
  Are both books the same? False

── Decorators Demo ─────────────────────────────────────
  Total books created  (@classmethod)  : 2
  Is 12.99 FCFA a valid price? (@staticmethod) : True
  eBook size in KB     (@property)     : 12800.0 KB

============================================================
    LIBRARY SUMMARY
============================================================

  Book 1 →  [The Little Prince] by Antoine de Saint-Exupery | 96 pages | 12.99 FCFA | Available
  Book 2 →  [Python Crash Course] by Eric Matthes | 544 pages | 29.99 FCFA | Available |  PDF (12.5 MB)

   Total pages combined  : 640 pages
   Average book price    : 21.49 FCFA
   eBook size            : 12800.0 KB
   Total books in system : 2

============================================================
```

---

## Assignment Coverage

| Requirement | Status | Detail |
|---|---|---|
| 4 data types (`str`, `int`, `float`, `bool`) |  Used in both classes and all inputs |
| Correct boolean |   `get_bool()` uses `answer == "yes"` |
| At least 10 `input()` calls  | 12 inputs collected |
| At least 3 arithmetic expressions |  Total pages, average price, KB conversion |
| Input validation (`while` + `try/except`) | `get_int()`, `get_float()`, `get_bool()` |
| f-strings for all output |  Used throughout, including summary screen |
| Parent class |  `Book` |
| Child class with `super().__init__()` |  `DigitalBook(Book)` |
| New attribute/method in child |  `file_size_mb`, `file_format`, `download()` |
| Magic method `__str__` | Implemented in both `Book` and `DigitalBook` |
| Magic method `__eq__` |  Compares books by title in `Book` |
| Magic method `__len__` |  Returns page count in `Book` |
| `@classmethod` |  `Book.get_total_books()` |
| `@staticmethod` |  `Book.is_valid_price()` |
| `@property` |  `DigitalBook.size_in_kb` |
