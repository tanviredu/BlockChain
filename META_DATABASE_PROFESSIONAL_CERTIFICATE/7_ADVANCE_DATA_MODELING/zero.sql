USE MANGATA_AND_GALLO;
SET SQL_SAFE_UPDATES=0;
DELETE FROM Clients WHERE 1=1;
DELETE FROM Address WHERE 1=1;
DELETE FROM Delivery WHERE 1=1;
DELETE FROM Orders WHERE 1=1;
DELETE FROm Products WHERE 1=1; 
INSERT INTO Clients(FullName,ContactNumber,Email)
VALUES 
('Vanessa McCarthy', 757536378, 'vm@mangatagallo.com'), 
('Marcos Romero', 757536379, 'mr@mangatagallo.com'), 
('Hiroki Yamane', 757536376, 'hy@mangatagallo.com'), 
('Anna Iversen', 757536375, 'ai@mangatagallo.com'), 
('Diana Pinto', 757536374, 'dp@mangatagallo.com');

SELECT * FROM Clients;

INSERT INTO Products (ProductName,BuyPrice,SellPrice,AmountInStock)  
VALUES
('Engagement ring', 2000, 2500, 25), 
('Silver brooch', 300, 400, 100), 
('Earrings', 1000, 1250, 100), 
('Luxury watch', 500, 800, 50), 
('Golden bracelet', 800, 1200, 100);

SELECT * FROM Products;


INSERT INTO Address (Street,ZipCode,State)
VALUES 
('223 Golden Hills, North Austin, TX', '78758', 'Texas'),
('119 Silver Street, Bouldin Creek, TX', '78737', 'Texas'), 
('785 Bronze Lane, East Austin, TX', '78717', 'Texas'), 
('908 Diamond Crescent, South Lamar, TX','76643 ', 'Texas'), 
('345, Golden Hills, North Austin, TX', '78759', 'Texas'), 
('812, Diamond Crescent, North Burnet, TX', '78611', 'Texas');

SELECT * FROM Address;

INSERT INTO Orders(OrderDate,ClientID,ProductID,Quantity,TotalPrice) 
VALUES 
('2022-10-15', 1, 1, 1, 2500), 
('2022-10-16', 2, 2, 2, 800), 
('2022-10-17', 3, 5, 1, 800), 
('2022-10-17', 4, 3, 3, 1050), 
('2022-10-18', 5, 4, 1, 1250);

SELECT * FROM Orders;

INSERT INTO Delivery (DeliveryDate,DeliveryStatus,AddressID,Comment,OrderID)
VALUES 
('2022-10-17', 'Done', 1, 'None', 1), 
('2022-10-20', 'Done', 2, 'None', 2), 
('2022-10-22', 'Done', 3, 'None', 3), 
('2022-10-25', 'Done', 4, 'None', 4), 
('2022-10-27', 'Done', 5, 'None', 5);


SELECT * FROM Delivery;

SELECT * FROM orders_view;
