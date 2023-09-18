DESIGN THE DATABASE ACCRODING TO THIS 

BOOKING
	BOOKING_ID(PK)			(INT)
	BOOKING_DATE			(DATETIME)
	BOOKING_TABLE_NUMBER	(INT)
	CUSTOMER_ID(FK)			(INT)
	STAFF_ID(FK)			(INT) 		(NULLABLE VALUE)

ORDERS
	ORDER_ID(PK)			(INT)
	ORDER_DATE				(DATE)
	ORDER_QUANTITY			(INT)
	ORDER_TOTAL_COST		(DECIMAL) (10,2)
	MENU_ID(FK)				(INT)
	CUSTOMER_ID(FK)			(INT)
	STAFF_ID(FK)			(INT) 


DELIVERY
	DELIVERY_ID(PK)			(INT)
	DELIVERY_DATE			(DATE)
	DELIVERY_STATUS			(VARCHAR)
	ORDER_ID(FK)			(INT)


MENU
	MENU_ID(PK)				(INT)
	MENU_NAME				(VRACHAR)
	MENU_CUISINE			(VARHCAR)
	MENU_ITEMS_ID(FK)		(INT)

MENU_ITEMS
	MENU_ITEMS_ID(PK)		(INT)
	MENU_ITEMS_STARTER		(VARCHAR)
	MENU_ITEMS_COURSES		(VARCHAR)
	MENU_ITEMS_DRINKS		(VARCHAR)
	MENU_ITEMS_DESSERTS		(VARCHAR)




CUSTOMER
	CUSTOMER_ID(PK)			(INT)
	CUSTOMER_NAME			(VARCHAR)
	CUSTOMER_MOBILE_NUMBER  (VARCHAR)
	CUSTOMER_EMAIL      	(VARCHAR)

STAFF
	STAFF_ID(PK)			(INT)
	STAFF_NAME				(VARCHAR)
	STAFF_MOBILE_NUMBER		(VARHCAR)
	STAFF_EMAIL				(VARCHAR)
	STAFF_ROLE				(VARCHAR)
	STAFF_SALARY			(INT)




SUBQUERY (NESTED QUERY) 
Subqueries, also called nested queries, can be placed in the SELECT, FROM or WHERE clause to return relevant data.

IN A SUBQUERY YOU CAN USE SEVEREAL TYPES OF OPERATOR LIKE ANY,ALL,EXISTS NOT EXISTS

ANY -> IF THERE ANY VALUE MEET THE CRITERIA THEN POSITIVE
ALL -> IF ALL THE VALUE MEET THE CRITERIA THEN POSITIVE OTHER THAN NEGATIVE
EXISTS -> IF VALUE EXISTS ON THAT CRITERIA
NOT EXISTS -< IF VALUE NOT EXISTS BASED ON THE CRITERIA









--INSERT VALUE FOR THE STAFF

USE LittleLemonDB;
INSERT INTO Staff 
(
	Name,
	MobileNumber,
	Email,
    Role,
    Salary
)
VALUES
    ('John Doe', '+1234567890', 'john.doe@example.com', 'Manager', 50000),
    ('Jane Smith', '+9876543210', 'jane.smith@example.com', 'Staff', 60000),
    ('Bob Johnson', '+5555555555', 'bob.johnson@example.com', 'Staff', 45000),
    ('Alice Brown', '+1111111111', 'alice.brown@example.com', 'Staff', 55000),
     ('Sarah Johnson', '+7778889991', 'sarah.johnson@example.com', 'CEO', 52000),
    ('Michael Wilson', '+1231231234', 'michael.wilson@example.com', 'Staff', 62000),
    ('Emily Davis', '+5554443332', 'emily.davis@example.com', 'Staff', 48000);



-- INSERT VALUE FOR THE CUSTOMER

INSERT INTO Customer (CustomerName, MobileNumber, Email)
VALUES
    ('Megan Adams', '+1112223334', 'megan.adams@example.com'),
    ('Jacob Brown', '+5556667778', 'jacob.brown@example.com'),
    ('Olivia Davis', '+9998887777', 'olivia.davis@example.com'),
    ('Elijah Evans', '+7778889999', 'elijah.evans@example.com'),
    ('Liam Garcia', '+1234567892', 'liam.garcia@example.com'),
    ('Sophia Green', '+4445556665', 'sophia.green@example.com'),
    ('Ava Harris', '+5554443334', 'ava.harris@example.com'),
    ('Ethan Jackson', '+7779998883', 'ethan.jackson@example.com'),
    ('Noah Johnson', '+1231231236', 'noah.johnson@example.com'),
    ('Emma Martinez', '+9876543211', 'emma.martinez@example.com');

-- INSERT VALUES MENU ITEMS

INSERT INTO MenuItems (Starter, Course, Drinks, Desserts)
VALUES
    ('Caesar Salad', 'Grilled Salmon', 'Soda', 'Cheesecake'),
    ('Mozzarella Sticks', 'Chicken Alfredo', 'Iced Tea', 'Tiramisu'),
    ('Spinach Dip', 'Beef Tacos', 'Lemonade', 'Chocolate Cake'),
    ('Tomato Soup', 'Vegetable Stir-Fry', 'Coffee', 'Fruit Salad'),
    ('Bruschetta', 'Spaghetti Carbonara', 'Water', 'Panna Cotta'),
    ('Onion Rings', 'Pork Chop', 'Red Wine', 'Key Lime Pie'),
    ('Caprese Salad', 'Shrimp Scampi', 'Orange Juice', 'Brownie Sundae'),
    ('Garlic Bread', 'Lamb Curry', 'Coca-Cola', 'Apple Pie'),
    ('Potato Skins', 'Vegetarian Lasagna', 'Mojito', 'Cherry Cheesecake'),
    ('Nachos', 'BBQ Ribs', 'Sprite', 'Strawberry Shortcake'),
    ('Crispy Calamari', 'Steak Fajitas', 'Margarita', 'Creme Brulee'),
    ('French Onion Soup', 'Teriyaki Chicken', 'Limeade', 'Ice Cream'),
    ('Spring Rolls', 'Seafood Paella', 'Root Beer', 'Banana Split'),
    ('Cobb Salad', 'Beef Burger', 'Iced Coffee', 'Peach Cobbler'),
    ('Garlic Parmesan Wings', 'Tofu Stir-Fry', 'Ginger Ale', 'Red Velvet Cake'),
    ('Clam Chowder', 'Salmon Teriyaki', 'Chai Tea', 'Carrot Cake'),
    ('Avocado Toast', 'Vegetable Curry', 'Arnold Palmer', 'Pistachio Ice Cream'),
    ('Fried Pickles', 'Lobster Bisque', 'Sparkling Water', 'Lemon Sorbet'),
    ('Shrimp Cocktail', 'Pasta Primavera', 'Grape Juice', 'Fudge Brownie'),
    ('Greek Salad', 'Filet Mignon', 'Mint Julep', 'Tropical Fruit Tart');


-- insert value in MENU

INSERT INTO Menu (MenuName,Cuisine, MenuItemsID)
VALUES
    ('Breakfast Menu','Italian', 1),
    ('Lunctarian Menu','Indian', 6),
    ('Branch Menu','French', 7),
    ('Happy Meal Menu','Mediterranean', 8),
    ('Late Night Menu','Thai', 9),
    ('Drinks Menu','Greek', 10);h Menu','Mexican', 2),
    ('Special Menu','American', 3),
    ('Brunch Menu','Japanese', 4),
    ('Dinner Menu','Chinese', 5),
    ('Vegitarian Menu','Indian', 6),
    ('Branch Menu','French', 7),
    ('Happy Meal Menu','Mediterranean', 8),
    ('Late Night Menu','Thai', 9),
    ('Drinks Menu','Greek', 10);
    
SELECT * FROM Menu;

--INSERT VALUE INTO ORDER

INSERT INTO Orders (OrderDate, Quantity, TotalCost, MenuID, CustomerID, StaffID)
VALUES
    ('2023-09-17', 3, 45.99, 1, 1, 2),
    ('2023-09-18', 2, 32.50, 3, 2, 3),
    ('2023-09-19', 4, 65.75, 2, 3, 1),
    ('2023-09-20', 1, 15.25, 4, 4, 2),
    ('2023-09-21', 3, 50.00, 5, 5, 3),
    ('2023-09-22', 2, 35.99, 1, 6, 1),
    ('2023-09-23', 3, 49.50, 3, 7, 2),
    ('2023-09-24', 2, 29.75, 2, 8, 3),
    ('2023-09-25', 4, 70.25, 4, 9, 1),
    ('2023-09-26', 1, 14.99, 5, 10, 2),

    ('2023-09-30', 2, 300.75, 2, 8, 3),
    ('2023-10-25', 4, 320.25, 4, 9, 1),
    ('2023-11-26', 1, 250.99, 5, 10, 2); 



-- CREATE VIEW FOR THE OrdersView

CREATE VIEW `OrdersView`
AS
	SELECT 
		OrderID,
		Quantity,
		TotalCost AS "Cost" 
	FROM Orders;   

Select * from OrdersView;

-- For your second task, Little Lemon need information from four tables on all customers with orders that cost more than $150.
	Customers table: The customer id and full name.
	Orders table: The order id and cost.
	Menus table: The menus name.
	MenusItems table: course name and starter name.


SELECT C.CustomerID,C.CustomerName as "FullName",O.OrderID,O.TotalCost as "Cost",M.MenuName as "MenuName",MI.Course FROM Customer C
JOIN Orders O
ON O.CustomerID = C.CustomerID
JOIN Menu M
ON O.MenuID = M.MenuID
JOIN MenuItems MI
ON M.MenuItemsID = MI.MenuItemsID
WHERE O.TotalCost > 150.00 order by Cost ASC;


-- Task 3

USE LittleLemonDB;
SELECT MenuName FROM Menu WHERE MenuID=ANY(SELECT MenuID FROM Orders WHERE Quantity >2);

-- any shows any key is matched. in the nested query we list MenuId whose quantity is greater than 2
-- outer query is searching  MenuName whose MenuID is matched ANY of the  element of the list and 
-- if its matched with any element then print the MenuName  






Creating a prepared statement

=> PREPARE statement_Name 'INSERT INTO table1 VALUES (?, ?, ?, ?)';





Task 1:
In this first task, Little Lemon need you to create a procedure that displays the maximum ordered quantity in the Orders table. 

Creating this procedure will allow Little Lemon to reuse the logic implemented in the procedure easily without retyping the same code over again and again to check the maximum quantity. 

You can call the procedure GetMaxQuantity and invoke it as follows:


ANS:

USE LittleLemonDB;
DROP PROCEDURE IF EXISTS GetMaxQuantity;

DELIMITER //
CREATE PROCEDURE GetMaxQuantity()
BEGIN
SELECT MAX(Quantity) AS "Max Quantity in Order" FROM Orders;
END //
DELIMITER ;

CALl GetMaxQuantity();


TASK 2:
In the second task, Little Lemon need you to help them to create a prepared statement called GetOrderDetail. This prepared statement will help to reduce the parsing time of queries. It will also help to secure the database from SQL injections.

The prepared statement should accept one input argument, the CustomerID value, from a variable. 

The statement should return the order id, the quantity and the order cost from the Orders table. 

Once you create the prepared statement, you can create a variable called id and assign it value of 1. 

Then execute the GetOrderDetail prepared statement using the following syntax:


ANS: 


USE LittleLemonDB;
PREPARE GetOrderDetail
FROM
"SELECT OrderID,Quantity,TotalCost AS 'Cost' FROM Orders WHERE CustomerID = ?";

SET @CustomerID = 1;
EXECUTE GetOrderDetail USING @CustomerID;
deallocate prepare GetOrderDetail;



TASK 3:

Your third and final task is to create a stored procedure called CancelOrder. Little Lemon want to use this stored procedure to delete an order record based on the user input of the order id.

Creating this procedure will allow Little Lemon to cancel any order by specifying the order id value in the procedure parameter without typing the entire SQL delete statement.   

If you invoke the CancelOrder procedure, the output result should be similar to the output of the following screenshot:


ANS:

DELIMITER //

CREATE PROCEDURE CancelOrder(order_id INT)
BEGIN
	DELETE FROM Orders WHERE OrderID = order_id;
	SELECT CONCAT("Order ", OrderID, " is cancelled") as Confirmation;
END //

DELIMITER ;

CALL CancelOrder(50);

TASK-1:

-- INSERT BOOKING

USE LittleLemonDB;
INSERT INTO Bookings(BookingDate,BookingTableNumber,CustomerID,StaffID)
VALUES
('2022-10-10',5,1,1),
('2022-11-12',3,3,2),
('2022-10-11',2,2,3),
('2022-10-13',2,1,4);


TASK-2
-- CheckBooking


DROP PROCEDURE IF EXISTS CheckBooking;
DELIMITER //
CREATE PROCEDURE CheckBooking(booking_date DATETIME,booking_table_number INT)
BEGIN 
	DECLARE booking_exists INT DEFAULT 0;
    SELECT COUNT(*) INTO booking_exists FROM Bookings WHERE BookingDate = booking_date AND BookingTableNumber = booking_table_number;
    IF booking_exists > 0 THEN
		SELECT CONCAT("Table ",booking_table_number," already booked") AS "Booking status";
    ELSE
		SELECT "Table Is Open For booking" AS "Booking status";
    END IF;
END //
DELIMITER ; 

SELECT * FROM Bookings;
CALL CheckBooking('2022-12-30',5);


-- TASK 3

USE LittleLemonDB;

DROP PROCEDURE IF EXISTS AddValidBooking;
DELIMITER //
CREATE PROCEDURE AddValidBooking(booking_date DATE,booking_table_number INT,customer_id INT,staff_id INT)
BEGIN
	DECLARE booking_status INT DEFAULT 0;
    START TRANSACTION;
    SELECT COUNT(*) INTO booking_status FROM Bookings WHERE BookingDate = booking_date AND BookingTableNumber = booking_table_number;
    IF booking_status > 0 THEN
		-- booking already exists
        SELECT CONCAT("Table ",booking_table_number," already booked - booking calcelled" ) AS "Booking status";
        ROLLBACK;
	ELSE
		INSERT INTO Bookings(BookingDate,BookingTableNumber,CustomerID,StaffID)
        VALUES
        (booking_date,booking_table_number,customer_id,staff_id);
        COMMIT;
        SELECT "Booking Added" AS "Booking status";
    END IF;
END //
DELIMITER ;
CALL AddValidBooking("2022-10-10",7,1,2);



TASK -1 : AddBooking

USE LittleLemonDB;

DROP PROCEDURE IF EXISTS AddBooking;
DELIMITER //
CREATE PROCEDURE AddBooking(
	customer_id INT,
    booking_date DATETIME,
    table_number INT,
    staff_id INT
)
BEGIN
	INSERT INTO Bookings(CustomerID,BookingDate,BookingTableNumber,StaffID)
    VALUES
    (customer_id,booking_date,table_number,staff_id);
    SELECT "Booking added successfully" AS "Message";
END //
DELIMITER ;

CALL AddBooking(3,"2022-12-30",3,3);


Task-2 :  UPDATE Booking

USE LittleLemonDB;

DROP PROCEDURE IF EXISTS UpdateBooking;
DELIMITER //
CREATE PROCEDURE UpdateBooking(
    booking_id INT,
    booking_date DATETIME
)
BEGIN
    UPDATE Bookings SET BookingDate = booking_date
    WHERE BookingID = booking_id;
    SELECT CONCAT("Booking ",booking_id," ipdated");

END //
DELIMITER ;
CALL UpdateBooking(1,"2022-10-20");

TASK-3 : Cancel booking

USE LittleLemonDB;

DROP PROCEDURE IF EXISTS CancelBooking;
DELIMITER //
CREATE PROCEDURE CancelBooking(
	booking_id INT
)
BEGIN
	DELETE FROM Bookings 
    WHERE BookingID = booking_id;
	SELECT CONCAT("Booking ",booking_id," canceled");

END //
DELIMITER ;
CALL CancelBooking(1);
