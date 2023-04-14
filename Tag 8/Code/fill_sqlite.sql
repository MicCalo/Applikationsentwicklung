DELETE FROM Shipments;
DELETE FROM Orders;
DELETE FROM Customers;


INSERT INTO Customers (Id, FirstName, LastName, Address, City) VALUES 
(1,'Anna','Bedecs','123 1st Street','Seattle'),
(2,'Antonio','Gratacos Solsona','123 2nd Street','Boston'),
(3,'Thomas','Axen','123 3rd Street','Los Angelas'),
(4,'Christina','Lee','123 4th Street','New York'),
(5,'Martin','O’Donnell','123 5th Street','Minneapolis'),
(6,'Francisco','Pérez-Olaeta','123 6th Street','Milwaukee'),
(7,'Ming-Yang','Xie','123 7th Street','Boise'),
(8,'Elizabeth','Andersen','123 8th Street','Portland'),
(9,'Sven','Mortensen','123 9th Street','Salt Lake City'),
(10,'Roland','Wacker','123 10th Street','Chicago'),
(11,'Peter','Krschne','123 11th Street','Miami'),
(12,'John','Edwards','123 12th Street','Las Vegas'),
(13,'Andre','Ludick','456 13th Street','Memphis'),
(14,'Carlos','Grilo','456 14th Street','Denver'),
(15,'Helena','Kupkova','456 15th Street','Honolulu'),
(16,'Daniel','Goldschmidt','456 16th Street','San Francisco'),
(17,'Jean Philippe','Bagel','456 17th Street','Seattle'),
(18,'Catherine','Autier Miconi','456 18th Street','Boston'),
(19,'Alexander','Eggerer','789 19th Street','Los Angelas'),
(20,'George','Li','789 20th Street','New York'),
(21,'Bernard','Tham','789 21th Street','Minneapolis'),
(22,'Luciana','Ramos','789 22th Street','Milwaukee'),
(23,'Michael','Entin','789 23th Street','Portland'),
(24,'Jonas','Hasselberg','789 24th Street','Salt Lake City'),
(25,'John','Rodman','789 25th Street','Chicago'),
(26,'Run','Liu','789 26th Street','Miami'),
(27,'Karen','Toh','789 27th Street','Las Vegas'),
(28,'Amritansh','Raghav','789 28th Street','Memphis'),
(29,'Soo Jung','Lee','789 29th Street','Denver');

/* Add some orders */
INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id, Id, ('2022-01-' || SUBSTR('00' || CAST(((50 - Id) % 31)+1  as text), -2, 2) ||' ' || SUBSTR('00' ||CAST((Id + 4) % 24  as text), -2, 2) || ':' || SUBSTR('00' ||CAST((Id * ID + 23) % 60  as text), -2, 2) || ':00') FROM Customers;

INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id+100, Id, ('2022-02-' || SUBSTR('00' || CAST((Id % 28)+1 as text), -2, 2) ||' ' || SUBSTR('00' || CAST(Id % 24  as text), -2, 2) || ':' || SUBSTR('00' || CAST((Id * ID + 45) % 60  as text), -2, 2) || ':00') FROM Customers;

INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id+200, Id, ('2022-03-' || SUBSTR('00' || CAST((Id % 31)+1  as text), -2, 2) ||' ' || SUBSTR('00' || CAST(Id % 24  as text), -2, 2) || ':' || SUBSTR('00' || CAST((Id * ID + 45) % 60  as text), -2, 2) || ':00') FROM Customers LIMIT 15;

INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id+250, Id, ('2022-03-' || SUBSTR('00' || CAST((Id % 31)+1  as text), -2, 2) ||' ' || SUBSTR('00' || CAST(Id % 24  as text), -2, 2) || ':' || SUBSTR('00' || CAST((Id * ID + 45) % 60  as text), -2, 2) || ':00') FROM Customers LIMIT 7;

/* Add shipments [same day delivery :-)] */
INSERT INTO Shipments (Id, OrderId, ShipmentDate)
SELECT Id, Id, OrderDate FROM Orders WHERE  (Id % 3) = 0;