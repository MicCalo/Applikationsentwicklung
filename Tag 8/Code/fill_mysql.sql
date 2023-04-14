USE small_shop_demo;

DELETE FROM Shipments;
DELETE FROM Orders;
DELETE FROM Customers;

INSERT INTO Customers (FirstName, LastName, Address, City) VALUES 
('Anna','Bedecs','123 1st Street','Seattle'),
('Antonio','Gratacos Solsona','123 2nd Street','Boston'),
('Thomas','Axen','123 3rd Street','Los Angelas'),
('Christina','Lee','123 4th Street','New York'),
('Martin','O’Donnell','123 5th Street','Minneapolis'),
('Francisco','Pérez-Olaeta','123 6th Street','Milwaukee'),
('Ming-Yang','Xie','123 7th Street','Boise'),
('Elizabeth','Andersen','123 8th Street','Portland'),
('Sven','Mortensen','123 9th Street','Salt Lake City'),
('Roland','Wacker','123 10th Street','Chicago'),
('Peter','Krschne','123 11th Street','Miami'),
('John','Edwards','123 12th Street','Las Vegas'),
('Andre','Ludick','456 13th Street','Memphis'),
('Carlos','Grilo','456 14th Street','Denver'),
('Helena','Kupkova','456 15th Street','Honolulu'),
('Daniel','Goldschmidt','456 16th Street','San Francisco'),
('Jean Philippe','Bagel','456 17th Street','Seattle'),
('Catherine','Autier Miconi','456 18th Street','Boston'),
('Alexander','Eggerer','789 19th Street','Los Angelas'),
('George','Li','789 20th Street','New York'),
('Bernard','Tham','789 21th Street','Minneapolis'),
('Luciana','Ramos','789 22th Street','Milwaukee'),
('Michael','Entin','789 23th Street','Portland'),
('Jonas','Hasselberg','789 24th Street','Salt Lake City'),
('John','Rodman','789 25th Street','Chicago'),
('Run','Liu','789 26th Street','Miami'),
('Karen','Toh','789 27th Street','Las Vegas'),
('Amritansh','Raghav','789 28th Street','Memphis'),
('Soo Jung','Lee','789 29th Street','Denver');

/* Add some orders */
INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id, Id, CONCAT('2022-01-', ((50 - Id) MOD 31)+1,' ', (Id + 4) MOD 24, ':', (Id * ID + 23) MOD 60,':00') FROM Customers;

INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id+100, Id, CONCAT('2022-02-',(Id MOD 28)+1,' ', Id MOD 24, ':', (Id * ID + 45) MOD 60,':00') FROM Customers;

INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id+200, Id, CONCAT('2022-03-', (Id MOD 31)+1,' ', Id MOD 24, ':', (Id * ID + 45) MOD 60,':00') FROM Customers LIMIT 15;

INSERT INTO Orders (Id, CustomerId, OrderDate) 
SELECT Id+250, Id, CONCAT('2022-03-',(Id MOD 31)+1,' ', Id MOD 24, ':', (Id * ID + 45) MOD 60,':00') FROM Customers LIMIT 7;

/* Add shipments [same day delivery :-)] */
INSERT INTO Shipments (Id, OrderId, ShipmentDate)
SELECT Id, Id, OrderDate FROM Orders WHERE  (Id % 3) = 0;
