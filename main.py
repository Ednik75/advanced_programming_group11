
class Book:
    
    
    total_books = 0

    def __init__(self, title: str, author: str, pages: int, price: float, available: bool):
        self.title     = title
        self.author    = author
        self.pages     = pages
        self.price     = price
        self.available = available
        Book.total_books += 1

    
    def __str__(self) -> str:
        status = "Available" if self.available else "Borrowed"
        return (
            f" [{self.title}] by {self.author} | "
            f"{self.pages} pages | {self.price:.2f} FCFA | {status}"
        )

    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title.lower() == other.title.lower()

    
    def __len__(self) -> int:
        return self.pages

    
    @classmethod
    def get_total_books(cls) -> int:
        return cls.total_books

    
    @staticmethod
    def is_valid_price(price: float) -> bool:
        return price > 0
        
    @staticmethod
    def is_long_book(pages: int) -> bool:
        """Returns True if the book has more than 300 pages."""
        return pages > 300

    def borrow(self):
        
        if self.available:
            self.available = False
            print(f"  '{self.title}' has been borrowed successfully.")
        else:
            print(f"    '{self.title}' is already borrowed.")

    def return_book(self):
        
        if not self.available:
            self.available = True
            print(f"  '{self.title}' has been returned successfully.")
        else:
            print(f"    '{self.title}' is already available.")


class DigitalBook(Book):
    

    def __init__(self, title: str, author: str, pages: int, price: float,
                 available: bool, file_size_mb: float, file_format: str):
        
        super().__init__(title, author, pages, price, available)
        
        self.file_size_mb = file_size_mb
        self.file_format  = file_format

   
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} |  {self.file_format} ({self.file_size_mb:.1f} MB)"

    
    def download(self):
        """Simulate downloading the digital book."""
        if self.available:
            print(f"    Downloading '{self.title}' ({self.file_format}, {self.file_size_mb} MB)...")
            print(f"  Download complete!")
        else:
            print(f"    '{self.title}' is not available for download.")

    
    @property
    def size_in_kb(self) -> float:
        """Converts file size from MB to KB automatically."""
        return self.file_size_mb * 1024




def get_int(prompt: str) -> int:
    """Ask for an integer, re-prompt on bad input. (Part 1 — validation)"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("    Please enter a valid whole number.")

def get_float(prompt: str) -> float:
    """Ask for a float, re-prompt on bad input. (Part 1 — validation)"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("    The value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("   Please enter a valid decimal number (e.g. 12.5).")

def get_bool(prompt: str) -> bool:
    """Ask yes/no, return bool. (Part 1 — correct boolean)"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        print("   Please answer 'yes' or 'no'.")




def main():
    print("=" * 60)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("   PRG1406 — Group Assignment 1")
    print("=" * 60)

    library: list[Book] = []

    
    print("\n── Register a Physical Book ────────────────────────────")

    title1   = input("  Book title              : ").strip()          
    author1  = input("  Author                  : ").strip()          
    pages1   = get_int("  Number of pages         : ")                
    price1   = get_float("  Price (FCFA)            : ")              
    avail1   = get_bool("  Available? (yes/no)     : ")               

    book1 = Book(title1, author1, pages1, price1, avail1)
    library.append(book1)

    
    print("\n── Register a Digital Book (eBook) ─────────────────────")

    title2   = input("  Book title              : ").strip()          
    author2  = input("  Author                  : ").strip()          
    pages2   = get_int("  Number of pages         : ")                
    price2   = get_float("  Price (FCFA)            : ")              
    avail2   = get_bool("  Available? (yes/no)     : ")               
    size2    = get_float("  File size (MB)          : ")              
    format2  = input("  Format (PDF/EPUB/MOBI)  : ").strip().upper()  

    book2 = DigitalBook(title2, author2, pages2, price2, avail2, size2, format2)
    library.append(book2)
    book3_name = input("Enter third book name: ")
    book3_price = float(input("Enter third book price: "))
    book3_quantity = int(input("Enter quantity: "))
    
    book3_total = book3_price * book3_quantity
    
    print(f"\nBook Name: {book3_name}")
    print(f"Book Price: {book3_price}")
    print(f"Quantity: {book3_quantity}")
    print(f"Total Price: {book3_total}")

    
    print("\n── Book Actions ────────────────────────────────────────")
    book1.borrow()
    book2.download()
    book1.return_book()

   
    total_pages      = pages1 + pages2                        
    avg_price        = (price1 + price2) / 2                  
    ebook_size_in_kb = book2.size_in_kb                       

    
    print("\n── Magic Methods Demo ──────────────────────────────────")
    print(f"  len(physical book)    = {len(book1)} pages")
    print(f"  len(digital book)     = {len(book2)} pages")
    same = book1 == book2
    print(f"  Are both books the same? {same}")

    
    print("\n── Decorators Demo ─────────────────────────────────────")
    print(f"  Total books created  (@classmethod)  : {Book.get_total_books()}")
    print(f"  Is {price1:.2f} FCFA a valid price? (@staticmethod) : {Book.is_valid_price(price1)}")
    print(f"  eBook size in KB     (@property)     : {ebook_size_in_kb:.1f} KB")

    
    print("\n" + "=" * 60)
    print("   LIBRARY SUMMARY")
    print("=" * 60)

    for i, book in enumerate(library, 1):
        print(f"\n  Book {i} → {book}")    

    print(f"\n   Total pages combined  : {total_pages} pages")
    print(f"   Average book price    : {avg_price:.2f} FCFA")
    print(f"  eBook size            : {ebook_size_in_kb:.1f} KB")
    print(f"   Total books in system : {Book.get_total_books()}")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
