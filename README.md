# Python Inventory Management System

A beginner-friendly command-line inventory management system built with **Python and MySQL** for managing product information, including prices and quantities.

## 📌 Overview

This project is a console-based inventory management application that uses a **MySQL database** to store and manage product records.

The system provides a simple menu-driven interface for adding, updating, removing, viewing, and searching products. It can also calculate the total value of the inventory using product prices and quantities.

Python communicates with the MySQL database using the `mysql-connector-python` library.

## 🚀 Features

* Add new products
* Update existing products
* Remove products
* View the complete inventory
* Search for individual products
* Calculate the total value of the inventory
* Sort products alphabetically when displaying inventory
* Track product price and quantity
* Store product records in MySQL
* Insert, update, delete, and retrieve database records
* Command-line based interface

## 🗄️ Database

The application uses a MySQL database named:

```text id="z4xq7m"
inventory_management
```

The database contains a `products` table with the following fields:

| Column     | Description                   |
| ---------- | ----------------------------- |
| `id`       | Unique product ID             |
| `name`     | Product name                  |
| `price`    | Product price                 |
| `quantity` | Product quantity in kilograms |

The application automatically creates the database and `products` table if they do not already exist.

The application also adds the initial sample products when the table is empty.

## 🛠️ Technologies Used

* **Python 3**
* **MySQL**
* **MySQL Connector/Python**
* SQL
* Functions
* Loops
* Conditional Statements
* User Input
* Sorting
* Basic Data Processing
* Basic Calculations

## 💻 Application Menu

```text id="7h3vl5"
---------- Inventory Management System ----------

1. Add Product
2. Update Product
3. Remove Product
4. View Inventory
5. Search Product
6. Total Value Of Inventory
7. Exit
```

## 📊 Example Inventory

The application starts with sample products such as:

```text id="8nbt9j"
Apple
Banana
Orange
Mango
```

Each product contains:

* Price
* Quantity

The total inventory value is calculated using:

```text id="wz9m18"
Product Value = Price × Quantity
```

The application then calculates the combined value of all products stored in the database.

## 🔄 Application Workflow

```text id="6j91j8"
Start Application
       ↓
Display Menu
       ↓
Choose an Option
   ↙   ↓   ↓   ↓   ↓
 Add Update Remove View Search
   ↓    ↓    ↓    ↓    ↓
INSERT UPDATE DELETE SELECT SELECT
   \     |     |     |     /
    \    |     |     |    /
        MySQL
           ↓
    Product Records
```

## ▶️ How to Run

### 1. Clone the repository

```bash id="k20h4n"
git clone https://github.com/itsharshgill/Python-Inventory-Management-System.git
```

### 2. Navigate to the project directory

```bash id="h4q7al"
cd Python-Inventory-Management-System
```

### 3. Install the required Python package

```bash id="p6d7xm"
pip install -r requirements.txt
```

### 4. Make sure MySQL Server is running

MySQL Server must be installed and running before starting the application.

### 5. Configure MySQL

Open `Database.py` and enter your local MySQL password:

```python id="4fs3eg"
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD"
)
```

Replace `YOUR_MYSQL_PASSWORD` with your local MySQL password.

### 6. Run the program

```bash id="j77s9d"
python Main.py
```

The application will automatically create the `inventory_management` database and `products` table if they do not already exist.

## 🔐 Security & Code Quality Note

The original version of this project used Python's `eval()` function to process numeric user input.

The updated version uses explicit type conversion such as:

```python id="6t2ub4"
float()
```

instead of `eval()`.

Using explicit type conversion prevents user input from being interpreted as executable Python code and provides safer input handling.

## 📚 What I Learned

Through this project, I practiced:

* Connecting a Python application to MySQL
* Creating and using a SQL database
* Creating database tables
* Inserting records into MySQL
* Retrieving records using SQL
* Updating database records
* Deleting database records
* Searching database records
* Calculating values from database records
* Using Python functions
* Handling user input
* Building a menu-driven command-line application
* Separating application logic from database operations
* Considering safer input handling

## 🔮 Future Improvements

Possible improvements include:

* Add input validation
* Prevent duplicate product entries
* Add low-stock alerts
* Add product categories
* Add inventory transaction/history tracking
* Add user authentication
* Add administrator functionality
* Improve database error handling
* Move database credentials to environment variables
* Separate the application into additional modules as the project grows

## 📁 Project Structure

```text id="z2byxq"
Python-Inventory-Management-System/
│
├── Main.py
├── Database.py
├── requirements.txt
└── README.md
```

### `Main.py`

Contains the main application workflow and handles:

* Menu options
* User interaction
* Product operations
* Inventory display
* Search
* Inventory value calculation

### `Database.py`

Handles the MySQL database operations, including:

* Connecting to MySQL
* Creating the database
* Creating the `products` table
* Adding initial products
* Adding products
* Updating products
* Removing products
* Retrieving products
* Calculating inventory value

### `requirements.txt`

Contains the Python package required for MySQL connectivity.

## 👤 Author

**Harshdeep Singh**

Cybersecurity Enthusiast | Aspiring Penetration Tester

📧 [itsharshgill@gmail.com](mailto:itsharshgill@gmail.com)

🔗 LinkedIn: [www.linkedin.com/in/itsharshgill](http://www.linkedin.com/in/itsharshgill)
