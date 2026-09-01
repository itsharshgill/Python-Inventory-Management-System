import mysql.connector


# Connect to MySQL Server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_Password"
)

cursor = connection.cursor()


# Create Database
cursor.execute(
    "CREATE DATABASE IF NOT EXISTS inventory_management"
)


# Use Database
cursor.execute(
    "USE inventory_management"
)


# Create Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    price DECIMAL(10,2),
    quantity DECIMAL(10,2)
)
""")


# Add Initial Products
cursor.execute("SELECT COUNT(*) FROM products")

Count = cursor.fetchone()[0]


if Count == 0:

    Products = [
        ("Apple", 7.99, 250),
        ("Banana", 2.99, 150),
        ("Orange", 5.95, 75),
        ("Mango", 9.99, 80)
    ]

    cursor.executemany("""
        INSERT INTO products
        (name, price, quantity)
        VALUES (%s, %s, %s)
    """, Products)

    connection.commit()


# Add Product
def add_product(name, price, quantity):

    cursor.execute("""
        INSERT INTO products
        (name, price, quantity)
        VALUES (%s, %s, %s)
    """, (name, price, quantity))

    connection.commit()


# Get Product
def get_product(name):

    cursor.execute("""
        SELECT * FROM products
        WHERE name = %s
    """, (name,))

    return cursor.fetchone()


# Update Product
def update_product(name, price, quantity):

    cursor.execute("""
        UPDATE products
        SET price = %s, quantity = %s
        WHERE name = %s
    """, (price, quantity, name))

    connection.commit()


# Remove Product
def remove_product(name):

    cursor.execute("""
        DELETE FROM products
        WHERE name = %s
    """, (name,))

    connection.commit()


# Get All Products
def get_products():

    cursor.execute("""
        SELECT * FROM products
        ORDER BY name
    """)

    return cursor.fetchall()


# Get Total Inventory Value
def get_total_value():

    cursor.execute("""
        SELECT SUM(price * quantity)
        FROM products
    """)

    Total_Value = cursor.fetchone()[0]

    if Total_Value is None:
        return 0

    return Total_Value