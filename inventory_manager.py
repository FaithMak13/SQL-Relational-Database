import sqlite3
from datetime import datetime

def connect_db(db_name="store_inventory.db"):
    """
    Establishes a connection to the SQLite database.
    Creates the database file if it does not exist.
    Returns the connection object.
    """
    return sqlite3.connect(db_name)

def create_table(conn):
    """
    Creates two relational tables: 'products' and 'sales'.
    Includes foreign key constraints to maintain data integrity.
    """
    cursor = conn.cursor()
    
    # Create the products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL
    )
    """)
    
    # Create the sales table with a Foreign Key relation and a timestamp
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity_sold INTEGER NOT NULL,
        sale_date TEXT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    """)
    conn.commit()
    print("Database tables initialized successfully.")

def insert_product(conn, name, price, stock):
    """
    Inserts a new product record into the products table.
    Demonstrates the 'Insert' capability required by the module.
    """
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO products (name, price, stock_quantity)
    VALUES (?, ?, ?)
    """, (name, price, stock))
    conn.commit()
    print(f"Product '{name}' added successfully.")

def retrieve_all_products(conn):
    """
    Queries the database and retrieves all items in the products table.
    Demonstrates the 'Retrieve/Query' capability.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    print("\n--- Current Inventory List ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Price: ${row[2]:.2f} | Stock: {row[3]}")
    return rows

def modify_product_stock(conn, product_id, new_stock):
    """
    Modifies the stock quantity of an existing product by ID.
    Demonstrates the 'Modify/Update' capability.
    """
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE products
    SET stock_quantity = ?
    WHERE product_id = ?
    """, (new_stock, product_id))
    conn.commit()
    print(f"Product ID {product_id} stock updated to {new_stock}.")

def delete_product(conn, product_id):
    """
    Deletes a product from the database using its unique identifier.
    Demonstrates the 'Delete' capability.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
    conn.commit()
    print(f"Product ID {product_id} removed from database.")

def record_sale(conn, product_id, quantity):
    """
    Records a transaction in the sales table and decrements the product stock.
    Automatically captures the current date and time.
    """
    cursor = conn.cursor()
    
    # Verify stock availability first
    cursor.execute("SELECT stock_quantity, name FROM products WHERE product_id = ?", (product_id,))
    product = cursor.fetchone()
    
    if product and product[0] >= quantity:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
        INSERT INTO sales (product_id, quantity_sold, sale_date)
        VALUES (?, ?, ?)
        """, (product_id, quantity, current_time))
        
        # Deduct from product stock
        new_stock = product[0] - quantity
        cursor.execute("UPDATE products SET stock_quantity = ? WHERE product_id = ?", (new_stock, product_id))
        
        conn.commit()
        print(f"Sold {quantity} units of '{product[1]}'. Inventory updated.")
    else:
        print("Transaction failed: Insufficient stock or invalid Product ID.")

def get_sales_report(conn):
    """
    Performs an INNER JOIN between the products table and sales table.
    Satisfies the unique module requirement of joining two tables.
    """
    cursor = conn.cursor()
    query = """
    SELECT sales.sale_id, products.name, sales.quantity_sold, sales.sale_date
    FROM sales
    INNER JOIN products ON sales.product_id = products.product_id
    """
    cursor.execute(query)
    records = cursor.fetchall()
    
    print("\n--- Sales Transaction Ledger (JOIN Query) ---")
    for record in records:
        print(f"Sale ID: {record[0]} | Item: {record[1]} | Qty: {record[2]} | Date: {record[3]}")

def display_financial_metrics(conn):
    """
    Uses aggregate functions (SUM and COUNT) to compute business metrics.
    Satisfies the additional module requirement for numerical summaries.
    """
    cursor = conn.cursor()
    
    # COUNT aggregate function
    cursor.execute("SELECT COUNT(*) FROM products")
    total_unique_items = cursor.fetchone()[0]
    
    # SUM aggregate function combined with calculations
    cursor.execute("SELECT SUM(price * stock_quantity) FROM products")
    total_value = cursor.fetchone()[0] or 0.0
    
    print("\n--- Inventory Metrics (Aggregate Functions) ---")
    print(f"Total Unique Product SKUs: {total_unique_items}")
    print(f"Total Asset Value of Stock: ${total_value:.2f}\n")

def main():
    """
    The orchestrator function execution path.
    Builds data, runs CRUD queries, executes joins, and aggregates data.
    """
    # 1. Establish connection and setup architecture
    connection = connect_db()
    create_table(connection)
    
    # 2. CRUD Operations: Create (Insert)
    print("\n--- Adding Mock Inventory Records ---")
    insert_product(connection, "Wireless Mouse", 29.99, 50)
    insert_product(connection, "Mechanical Keyboard", 89.99, 20)
    insert_product(connection, "27-inch Monitor", 249.99, 15)
    
    # 3. CRUD Operations: Read (Retrieve)
    retrieve_all_products(connection)
    
    # 4. CRUD Operations: Update (Modify)
    print("\n--- Adjusting Inventory Levels ---")
    modify_product_stock(connection, 1, 48)
    
    # 5. Execute Relational Transactions & Multi-Table Joins
    print("\n--- Recording Real-time Store Transactions ---")
    record_sale(connection, 1, 2)
    record_sale(connection, 2, 1)
    
    # 6. Execute Complex Module Requirement Queries
    get_sales_report(connection)
    display_financial_metrics(connection)
    
    # 7. CRUD Operations: Delete
    print("\n--- Removing Discontinued Lines ---")
    delete_product(connection, 3)
    
    # Final state check
    retrieve_all_products(connection)
    
    # Close resources cleanly
    connection.close()
    print("\nDatabase session closed cleanly.")

if __name__ == "__main__":
    main()