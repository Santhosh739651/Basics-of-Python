import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("college.db")

# Create cursor
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cur.execute("INSERT INTO student (id, name, marks) VALUES (?, ?, ?)",
            (1, "Santhosh", 90))

# Save changes
conn.commit()

# Fetch data
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()