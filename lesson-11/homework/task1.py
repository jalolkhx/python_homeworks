import sqlite3
query = """
    drop table if exists Roster;
    Create table Roster (Name text, Species text, Age int);
    Insert into Roster Values
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29);
"""
with sqlite3.connect('roster.db') as con:
    cursor = con.cursor()
    cursor.executescript(query)
    cursor.execute("UPDATE Roster SET Name='Ezri Dax' WHERE Name='Jadzia Dax'")
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    cursor.execute("ALTER TABLE Roster ADD column Rank text")
    cursor.execute("UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys'")
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    results = cursor.fetchall()
    print(results)