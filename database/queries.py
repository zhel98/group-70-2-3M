# sql запросы 

products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        price INTEGER,
        description TEXT,
        photo TEXT
    )
"""

select_all_products = """
    SELECT id, name, price, description, photo
    FROM products
    ORDER BY id
"""

insert_product = "INSERT INTO products (name, price, description, photo) VALUES (?, ?, ?, ?)"