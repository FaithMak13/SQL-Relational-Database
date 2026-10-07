# Store Inventory Management System – Video Presentation

## Introduction – 30 seconds

Hello, my name is **Faith**, and this video demonstrates my Store Inventory Management System.

I created this project using **Python and SQLite**. The purpose of the program is to manage store inventory and sales transactions using a relational database.

In this demonstration, I will show my program running, demonstrate the main features, and then walk through the important parts of my code, including the database tables, CRUD operations, sales transactions, SQL JOIN, and aggregate functions.

---

## Part 1: Demonstrating the Program – 1 minute 30 seconds

I will start by running my Python program.

The program first connects to a SQLite database called `store_inventory.db`. If the database does not already exist, SQLite creates it automatically.

The program then creates two tables: **products** and **sales**.

The products table stores the product ID, product name, price, and stock quantity.

The sales table stores the sale ID, product ID, quantity sold, and the date and time of the sale.

The program then adds three sample products:

* Wireless Mouse
* Mechanical Keyboard
* 27-inch Monitor

Next, the program retrieves the products from the database and displays the current inventory.

The program then demonstrates an **Update** operation by changing the stock quantity of the Wireless Mouse.

After that, I demonstrate a sales transaction.

When I sell two Wireless Mice, the program first checks whether there is enough stock. If there is enough stock, it records the sale and automatically reduces the inventory.

The program also records the date and time of the transaction.

Next, the program generates a sales report. This report demonstrates how information from the products and sales tables can be combined.

Finally, the program calculates inventory statistics and displays the total number of products and the total value of the inventory.

The program then demonstrates the **Delete** operation by removing the discontinued monitor product and displays the final inventory.

---

## Part 2: Code Walkthrough – 2 minutes

Now I will briefly walk through the important parts of my code.

At the top of my program, I import `sqlite3`, which allows Python to communicate with the SQLite database.

I also import `datetime`, which I use to record the date and time when a sale takes place.

My first function is `connect_db()`.

This function creates a connection to the SQLite database. If the database file does not exist, SQLite creates it automatically.

Next, I have my `create_table()` function.

This function creates two relational tables: `products` and `sales`.

The products table has `product_id` as its primary key.

The sales table has its own primary key, `sale_id`, and uses `product_id` as a foreign key to connect a sale to a product.

This creates a relationship between my two tables.

Next, I have the `insert_product()` function.

This function demonstrates the **Create** part of CRUD because it uses an SQL `INSERT` statement to add products to the database.

I use question marks as placeholders in my SQL statement. This allows me to pass the values separately instead of directly putting them into the SQL command.

My `retrieve_all_products()` function demonstrates the **Read** part of CRUD.

It uses a `SELECT` statement to retrieve all products and then displays them in the terminal.

The `modify_product_stock()` function demonstrates the **Update** part of CRUD.

It uses an SQL `UPDATE` statement to change the stock quantity for a specific product.

The `delete_product()` function demonstrates the **Delete** part of CRUD.

It uses an SQL `DELETE` statement to remove a product using its product ID.

---

## Part 3: Sales, JOIN and Aggregate Functions – 1 minute

One of the most important functions in my program is `record_sale()`.

This function first checks whether the product exists and whether there is enough stock available.

If there is sufficient stock, the program inserts the sale into the sales table and then decreases the product's stock quantity.

This means the program performs multiple related database operations as part of one transaction.

My `get_sales_report()` function demonstrates an SQL **INNER JOIN**.

The JOIN connects the `sales` table to the `products` table using the `product_id`.

This allows me to display information such as the sale ID, product name, quantity sold, and sale date together.

Finally, my `display_financial_metrics()` function demonstrates SQL **aggregate functions**.

I use `COUNT()` to calculate the number of products and `SUM()` to calculate the total value of the inventory currently in stock.

---

## Conclusion – 30 seconds

In conclusion, this project helped me understand how Python can be connected to a relational database.

I demonstrated the four CRUD operations: **Create, Read, Update, and Delete**.

I also implemented related database tables using primary and foreign keys, an SQL INNER JOIN, aggregate functions, and sales transactions that update inventory.

One of the main things I learned is that database programming is not only about storing information. It is also about creating relationships between data and using that information to solve a real-world problem.

Thank you for watching my demonstration.
