# 2100030875_Backendexam

These are done in Mysql command line client

creating database and tables 
<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/d7afcae0-fb88-4fef-8f88-91fdae0565b4)

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/b34d53c6-a9f6-4f6d-82b2-bc7c0c389f30)


Sample Queries :
1. List all customers.
   **query :**<br>
   SELECT * FROM Customers;<br>
   <h3>output:</h3>
![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/5490e5e3-2148-4c1b-9334-cd0c0cd5d8c3)
<br>
2. Find all orders placed in January 2023.
    <h4>query:</h4><br>
    SELECT * FROM Orders WHERE OrderDate BETWEEN '2023-01-01' AND '2023-01-31';<br>
    <h3>output:</h3>
![image](https://github.com/Pradeeptata0411/jfsdproject/assets/109360049/fcb04a26-d032-4e10-ade7-b1438036184e)
<br>

3. Get the details of each order, including the customer name and email.
   <h4>query:</h4><br>
   SELECT Orders.OrderID, Orders.OrderDate, Customers.FirstName, Customers.LastName, Customers.Email FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
   <h3>output:</h3>
![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/37456d51-33df-4a23-bc44-3e5c5d5f458a)
<br>

4. List the products purchased in a specific order (e.g., OrderID = 1).
   <h4>query:</h4><br>
   SELECT OrderItems.OrderID, Products.ProductName, Products.Price, OrderItems.Quantity FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE 
   OrderItems.OrderID = 1;
   <h3>output:</h3>
![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/e1de8276-e95e-4b2e-8329-573b5132e1b8)

<br>

5. Calculate the total amount spent by each customer .
   <h4>query:</h4><br>
   SELECT Customers.CustomerID, Customers.FirstName,Customers.LastName,Customers.Email, SUM(Products.Price * OrderItems.Quantity) AS TotalAmountSpent FROM  Customers JOIN  Orders ON     
   Customers.CustomerID = Orders.CustomerID JOIN  OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN  Products ON OrderItems.ProductID = Products.ProductID GROUP BY 
   Customers.CustomerID, Customers.FirstName,Customers.LastName,Customers.Email;
   <h3>output:</h3>
![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/5182afea-272c-461c-8214-bc5c0cecc1fb)

<br>

6. Find the most popular product (the one that has been ordered the most).
   <h4>query:</h4><br>
   SELECT Products.ProductID, Products.ProductName, COUNT(OrderItems.OrderItemID) AS TotalOrders FROM Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY    
   Products.ProductID,Products.ProductName ORDER BY TotalOrders DESC LIMIT 1;
   <h3>output:</h3>
![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/477c2e04-e29e-4844-90e4-6697fe12f371)

<br>

7. Get the total number of orders and the total sales amount for each month in 2023.
   <h4>query:</h4><br>
   SELECT EXTRACT(MONTH FROM Orders.OrderDate) AS Month, COUNT(Orders.OrderID) AS TotalOrders, SUM(Products.Price * OrderItems.Quantity) AS TotalSalesAmount FROM Orders JOIN OrderItems   
   ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE Orders.OrderDate BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY EXTRACT(MONTH 
   FROM Orders.OrderDate) ORDER BY Month;
  <h3>output:</h3>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/a722dfce-76f5-4e6c-a67d-f67acfe3d8a1)

<br>

8.Find customers who have spent more than $1000.
  <h4>query:</h4><br>
  SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalSpent FROM Customers JOIN Orders ON Customers.CustomerID =   
  Orders.CustomerID JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customers.CustomerID, Customers.FirstName, 
  Customers.LastName HAVING TotalSpent > 1000;
  <h3>output:</h3>
  
![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/31abb663-11d5-4422-8aae-3525702367bf)

-------------------------------------------------------------------------------------------------------------------------------

<br>
<br>
<h1>These are Output ScreenShots of the python code 👇👇</h1>
<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/ee428eed-33be-48da-8b36-550ae8b9c130)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/d71644b1-e93c-4e7f-bb75-342bebe39099)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/77f5be63-b6a3-4bd5-ad49-b123fa015302)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/8fdea129-0213-4df3-945e-e391414a71e5)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/ebb88b2c-6e1e-40e1-bdc2-da91d1c08b65)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/f516cc18-14ce-4f0a-bb82-d45138c9263c)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/66d96913-12f5-4ebb-b06e-46e4241de9ef)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/b4d60770-9a15-4ad8-b6f2-c219db18a9e4)

<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/fbdddc71-15c6-4652-8217-ab26e961125c)


<br>

![image](https://github.com/Pradeeptata0411/2100030875_Backendexam/assets/109360049/97116dce-956f-4e3f-9849-f25d6add4241)

<br>
