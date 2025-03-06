import sqlite3
query = """
    drop table if exists Books;
    Create table Books (Title text, Author text, Year_Published int, Genre text);
    Insert into Books Values
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');
"""

with sqlite3.connect('library.db') as con:
    cursor = con.cursor()
    cursor.executescript(query)
    cursor.execute("UPDATE Books SET Year_Published=1950 WHERE Title='1984'")
    for i in cursor.execute("SELECT Title, Author FROM Books WHERE Genre='Dystopian'"):
        print(i)
    cursor.execute("DELETE FROM Books WHERE Year_Published<1950")
    
    