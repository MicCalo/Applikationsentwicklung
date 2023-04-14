SELECT Orders.*, Customers.FirstName, Customers.LastName, customers.City, Shipments.ShipmentDate, Shipments.Id AS ShipmentId
FROM Orders
INNER JOIN Customers ON Orders.CustomerId = Customers.Id /* Join with Customers so we also have first- and last name of customer */
LEFT JOIN Shipments ON Orders.Id = Shipments.OrderId /* Optionally, join with shipments. If it was already shipped, add date and id */
ORDER BY Customers.LastName