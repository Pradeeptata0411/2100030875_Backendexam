import mysql.connector

# Establish connection to the MySQL database
host = "localhost"
port = "3306"
uname = "root"
pwd = "pradeep0411"
db = "saferteckexam"

try:
    db_conn = mysql.connector.connect(host=host, port=port, user=uname, password=pwd, database=db)
    db_cursor = db_conn.cursor(dictionary=True)
    print("Connected to DB Successfully")
except Exception as e:
    print(e)

db_cursor.execute("DROP TABLE IF EXISTS OrderItems")
db_cursor.execute("DROP TABLE IF EXISTS Orders")
db_cursor.execute("DROP TABLE IF EXISTS Products")
db_cursor.execute("DROP TABLE IF EXISTS Customers")

# Create Customers table
create_customers_table = """
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DateOfBirth DATE
)
"""
db_cursor.execute(create_customers_table)

# Create Products table
create_products_table = """
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price INT
)
"""
db_cursor.execute(create_products_table)

# Create Orders table
create_orders_table = """
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
"""
db_cursor.execute(create_orders_table)

# Create OrderItems table
create_orderitems_table = """
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
"""
db_cursor.execute(create_orderitems_table)



# Insert data into Customers table
customers_data = """
INSERT INTO Customers (CustomerID, FirstName, LastName, Email, DateOfBirth) VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '1985-01-15'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '1990-06-20')
"""
db_cursor.execute(customers_data)



# Insert data into Products table
products_data = """
INSERT INTO Products (ProductID, ProductName, Price) VALUES
(1, 'Laptop', 1000),
(2, 'Smartphone', 600),
(3, 'Headphones', 100)
"""
db_cursor.execute(products_data)



# Insert data into Orders table
orders_data = """
INSERT INTO Orders (OrderID, CustomerID, OrderDate) VALUES
(1, 1, '2023-01-10'),
(2, 2, '2023-01-12')
"""
db_cursor.execute(orders_data)



# Insert data into OrderItems table
orderitems_data = """
INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity) VALUES
(1, 1, 1, 1),
(2, 1, 3, 2),
(3, 2, 2, 1),
(4, 2, 3, 1)
"""
db_cursor.execute(orderitems_data)

# Commit the changes to the database
db_conn.commit()



def list_all_customers():
    try:
        sql = "SELECT * FROM Customers"
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

def find_orders_in_january_2023():
    try:
        sql = "SELECT * FROM Orders WHERE OrderDate BETWEEN '2023-01-01' AND '2023-01-31'"
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

def get_order_details_with_customer_info():
    try:
        sql = """SELECT Orders.OrderID, Orders.OrderDate, Customers.FirstName, Customers.LastName, Customers.Email
                 FROM Orders
                 JOIN Customers ON Orders.CustomerID = Customers.CustomerID"""
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)



def list_products_in_order(order_id=1):
    try:
        sql = """SELECT OrderItems.OrderID, Products.ProductName, Products.Price, OrderItems.Quantity
                 FROM OrderItems
                 JOIN Products ON OrderItems.ProductID = Products.ProductID
                 WHERE OrderItems.OrderID = %s"""
        db_cursor.execute(sql, (order_id,))
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

def calculate_total_amount_spent_by_customers():
    try:
        sql = """SELECT 
                    Customers.CustomerID,
                    Customers.FirstName,
                    Customers.LastName,
                    Customers.Email,
                    SUM(Products.Price * OrderItems.Quantity) AS TotalAmountSpent
                 FROM 
                    Customers
                 JOIN 
                    Orders ON Customers.CustomerID = Orders.CustomerID
                 JOIN 
                    OrderItems ON Orders.OrderID = OrderItems.OrderID
                 JOIN 
                    Products ON OrderItems.ProductID = Products.ProductID
                 GROUP BY 
                    Customers.CustomerID,
                    Customers.FirstName,
                    Customers.LastName,
                    Customers.Email"""
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

def find_most_popular_product():
    try:
        sql = """SELECT 
                    Products.ProductID,
                    Products.ProductName,
                    COUNT(OrderItems.OrderItemID) AS TotalOrders
                 FROM 
                    Products
                 JOIN 
                    OrderItems ON Products.ProductID = OrderItems.ProductID
                 GROUP BY 
                    Products.ProductID,
                    Products.ProductName
                 ORDER BY 
                    TotalOrders DESC
                 LIMIT 1"""
        db_cursor.execute(sql)
        row = db_cursor.fetchone()
        print(row)
    except Exception as e:
        print(e)

def get_monthly_orders_and_sales_in_2023():
    try:
        sql = """SELECT 
                    EXTRACT(MONTH FROM Orders.OrderDate) AS Month,
                    COUNT(Orders.OrderID) AS TotalOrders,
                    SUM(Products.Price * OrderItems.Quantity) AS TotalSalesAmount
                 FROM 
                    Orders
                 JOIN 
                    OrderItems ON Orders.OrderID = OrderItems.OrderID
                 JOIN 
                    Products ON OrderItems.ProductID = Products.ProductID
                 WHERE 
                    Orders.OrderDate BETWEEN '2023-01-01' AND '2023-12-31'
                 GROUP BY 
                    EXTRACT(MONTH FROM Orders.OrderDate)
                 ORDER BY 
                    Month"""
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)



def find_customers_who_spent_more_than_1000():
    try:
        sql = """SELECT 
                    Customers.CustomerID,
                    Customers.FirstName,
                    Customers.LastName,
                    SUM(Products.Price * OrderItems.Quantity) AS TotalSpent
                 FROM 
                    Customers
                 JOIN 
                    Orders ON Customers.CustomerID = Orders.CustomerID
                 JOIN 
                    OrderItems ON Orders.OrderID = OrderItems.OrderID
                 JOIN 
                    Products ON OrderItems.ProductID = Products.ProductID
                 GROUP BY 
                    Customers.CustomerID,
                    Customers.FirstName,
                    Customers.LastName
                 HAVING 
                    TotalSpent > 1000"""
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

# Call the functions to execute the queries
list_all_customers()
find_orders_in_january_2023()
get_order_details_with_customer_info()
list_products_in_order(1)
calculate_total_amount_spent_by_customers()
find_most_popular_product()
get_monthly_orders_and_sales_in_2023()
find_customers_who_spent_more_than_1000()

# Close the database connection
db_cursor.close()
db_conn.close()
print("Database connection closed")

