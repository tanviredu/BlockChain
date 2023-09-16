CREATE VIEW `orders_view`
AS
SELECT 
	o.OrderID,
    
    c.ClientID,
    c.FullName,
    
    p.ProductName,
    
    o.Quantity,
    o.TotalPrice AS "TotalCost",
    
    d.DeliveryStatus,
    d.DeliveryDate,
    a.Street 
FROM 
	Clients c
JOIN Orders   o   ON o.ClientID  = c.ClientID
JOIN Delivery d   ON d.OrderID   = o.OrderID
JOIN Products p   ON p.ProductID = o.ProductID
JOIN Address  a   ON a.AddressID = d.AddressID;