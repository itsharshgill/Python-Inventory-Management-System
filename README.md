# Python Inventory Management System

A command-line inventory management system built with Python for managing product information, including prices and quantities.

## 📌 Overview

This project is a console-based application that allows users to manage an inventory through a simple menu-driven interface.

The system stores product information such as **price** and **quantity** and provides options to add, update, remove, search, and view products.

## 🚀 Features

* Add new products
* Update existing products
* Remove products
* View the complete inventory
* Search for individual products
* Calculate the total value of the inventory
* Sort products alphabetically when displaying inventory
* Track product price and quantity

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* Loops & Conditional Statements
* User Input
* Functions/Operations on Data Structures
* Sorting
* Basic Data Processing

## 💻 Application Menu

```text
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

```text
Apple
Banana
Orange
Mango
```

Each product contains:

* Price
* Quantity

The application can calculate the total inventory value using:

```text
Product Value = Price × Quantity
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/python-inventory-management-system.git
```

### 2. Navigate to the project directory

```bash
cd python-inventory-management-system
```

### 3. Run the program

```bash
python inventory_management.py
```

## 🔐 Security & Code Quality Note

The original version of this project used `eval()` to process numeric user input.

For safer code, user input should be explicitly converted using functions such as:

```python
float()
```

or

```python
int()
```

rather than using `eval()`.

Using explicit type conversion prevents user input from being interpreted as executable Python code.

## 📚 What I Learned

Through this project, I practiced:

* Working with Python dictionaries
* Managing structured data
* Implementing CRUD-style inventory operations
* Handling user input
* Searching and sorting data
* Performing calculations on stored data
* Building a menu-driven command-line application
* Considering secure input handling

## 🔮 Future Improvements

Possible improvements include:

* Add persistent storage using SQLite or MySQL
* Add input validation
* Prevent duplicate product entries
* Add low-stock alerts
* Add product categories
* Add transaction/history tracking
* Add authentication
* Improve error handling
* Separate application logic into reusable functions/classes

## 📁 Project Structure

```text
python-inventory-management-system/
│
├── inventory_management.py
└── README.md
```

## 👤 Author

**Harshdeep Singh**

Cybersecurity Enthusiast | Aspiring Penetration Tester

📧 [itsharshgill@gmail.com](mailto:itsharshgill@gmail.com)

🔗 LinkedIn: [www.linkedin.com/in/itsharshgill](http://www.linkedin.com/in/itsharshgill)
