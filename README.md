# Store Inventory Management System

## Project Overview

The **Store Inventory Management System** is a Python application that uses **SQLite** to manage products, inventory quantities, and sales transactions.

The project demonstrates how a Python program can connect to a relational database and perform common database operations, including **Create, Read, Update, and Delete (CRUD)** operations. It also demonstrates relationships between tables, SQL `JOIN` queries, aggregate functions, and transaction processing.

This project was created as part of a programming/database learning module to demonstrate practical database skills.

## Features

The application provides the following features:

* Create and initialize a SQLite database.
* Create `products` and `sales` relational tables.
* Add new products to inventory.
* Retrieve and display all products.
* Update product stock quantities.
* Delete products from the database.
* Record sales transactions.
* Automatically reduce inventory after a sale.
* Check whether sufficient stock is available before recording a sale.
* Store the date and time of each sale.
* Generate a sales report using an SQL `INNER JOIN`.
* Calculate inventory statistics using SQL aggregate functions.
* Close the database connection properly when the program finishes.

## Technologies Used

* **Python 3**
* **SQLite**
* **sqlite3** Python standard library
* **datetime** Python standard library
* SQL

No external Python packages are required.

## Database Structure

The application uses two related tables.

### Products Table

The `products` table stores information about items available in the store.

| Column           | Type    | Description                 |
| ---------------- | ------- | --------------------------- |
| `product_id`     | INTEGER | Unique product identifier   |
| `name`           | TEXT    | Product name                |
| `price`          | REAL    | Product price               |
| `stock_quantity` | INTEGER | Quantity currently in stock |

### Sales Table

The `sales` table stores information about completed sales.

| Column          | Type    | Description               |
| --------------- | ------- | ------------------------- |
| `sale_id`       | INTEGER | Unique sale identifier    |
| `product_id`    | INTEGER | ID of the product sold    |
| `quantity_sold` | INTEGER | Number of units sold      |
| `sale_date`     | TEXT    | Date and time of the sale |

The `product_id` column in the `sales` table is a **foreign key** that connects each sale to a product in the `products` table.

## CRUD Operations

The project demonstrates all four basic CRUD operations.

### Create

New products are inserted into the database using SQL `INSERT`.

Example:

```python
insert_product(connection, "Wireless Mouse", 29.99, 50)
```

### Read

Products are retrieved using a SQL `SELECT` query.

```python
retrieve_all_products(connection)
```

### Update

Inventory quantities can be modified using SQL `UPDATE`.

```python
modify_product_stock(connection, 1, 48)
```

### Delete

Products can be removed using SQL `DELETE`.

```python
delete_product(connection, 3)
```

## Sales Transactions

The `record_sale()` function performs several operations:

1. Finds the selected product.
2. Checks whether enough stock is available.
3. Records the sale in the `sales` table.
4. Records the current date and time.
5. Deducts the quantity sold from the product's inventory.
6. Saves the changes to the database.

For example:

```python
record_sale(connection, 1, 2)
```

This records the sale of two units and reduces the product's stock accordingly.

## SQL JOIN

The project demonstrates how two related database tables can be combined using an `INNER JOIN`.

The sales report connects the `sales` table with the `products` table:

```sql
SELECT sales.sale_id,
       products.name,
       sales.quantity_sold,
       sales.sale_date
FROM sales
INNER JOIN products
ON sales.product_id = products.product_id;
```

This allows the program to display the product name together with the corresponding sales information.

## Aggregate Functions

The project also demonstrates SQL aggregate functions.

### COUNT

The program uses `COUNT()` to determine the number of unique product records:

```sql
SELECT COUNT(*) FROM products;
```

### SUM

The program uses `SUM()` to calculate the total value of inventory currently in stock:

```sql
SELECT SUM(price * stock_quantity)
FROM products;
```

These calculations provide useful business information from the database.

## How to Run the Program

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python installation by running:

```bash
python --version
```

### 2. Save the Program

Save the Python code as:

```text
inventory_manager.py
```

### 3. Run the Program

Open a terminal in the project folder and run:

```bash
python inventory_manager.py
```

The program will automatically create the SQLite database:

```text
inventory_manager.db
```

The database does not need to be created manually.

## Example Products

The program initially adds three sample products:

| Product             |   Price | Initial Stock |
| ------------------- | ------: | ------------: |
| Wireless Mouse      |  $29.99 |            50 |
| Mechanical Keyboard |  $89.99 |            20 |
| 27-inch Monitor     | $249.99 |            15 |

The program then performs inventory updates and records sales transactions.

## Example Output

```text
Database tables initialized successfully.

--- Adding Mock Inventory Records ---
Product 'Wireless Mouse' added successfully.
Product 'Mechanical Keyboard' added successfully.
Product '27-inch Monitor' added successfully.

--- Current Inventory List ---
ID: 1 | Name: Wireless Mouse | Price: $29.99 | Stock: 50
ID: 2 | Name: Mechanical Keyboard | Price: $89.99 | Stock: 20
ID: 3 | Name: 27-inch Monitor | Price: $249.99 | Stock: 15

--- Adjusting Inventory Levels ---
Product ID 1 stock updated to 48.

--- Recording Real-time Store Transactions ---
Sold 2 units of 'Wireless Mouse'. Inventory updated.
Sold 1 unit of 'Mechanical Keyboard'. Inventory updated.

--- Sales Transaction Ledger (JOIN Query) ---

--- Inventory Metrics (Aggregate Functions) ---
Total Unique Product SKUs: 3
Total Asset Value of Stock: $...
```

*What I Learned*

Through this project, I practiced using Python to work with a relational database.

I learned how to:

* Create and connect to a SQLite database.
* Create database tables using SQL.
* Design relationships between tables.
* Use primary keys and foreign keys.
* Insert records into a database.
* Retrieve information using `SELECT`.
* Modify existing records using `UPDATE`.
* Delete records using `DELETE`.
* Use parameterized SQL queries.
* Record and process transactions.
* Use `INNER JOIN` to combine information from multiple tables.
* Use aggregate functions such as `COUNT()` and `SUM()`.
* Connect Python logic with SQL database operations.

*Challenges*

One of the challenges was understanding how the different database operations work together.

For example, recording a sale requires more than simply inserting a record. The program must first check the available stock, record the sale, and then update the inventory quantity.

Another important learning experience was understanding the relationship between the `products` and `sales` tables. The foreign key allows sales transactions to be associated with the correct product.

*Future Improvements*

If I continue developing this project, I would like to add:

* A graphical user interface.
* User input instead of hard-coded products.
* Product search functionality.
* Automatic low-stock alerts.
* Better error handling and input validation.
* A product editing menu.
* Sales totals and revenue calculations.
* A daily, weekly, and monthly sales report.
* A database reset/setup option for demonstrations.
* Improved protection of database transactions.

*Conclusion*

The Store Inventory Management System demonstrates how Python and SQLite can be used together to build a simple relational database application.

The project successfully demonstrates CRUD operations, relational tables, foreign keys, SQL joins, transactions, and aggregate functions while solving a practical inventory management problem.
