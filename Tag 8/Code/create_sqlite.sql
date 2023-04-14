/* DROP in reverse order because of foreign key constraints */
DROP TABLE IF EXISTS Shipments;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers(
    Id INTEGER NOT NULL PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Address TEXT NOT NULL,
    City TEXT NOT NULL
);

CREATE TABLE Orders(
    Id INTEGER NOT NULL PRIMARY KEY,
    CustomerId INTEGER NOT NULL,
    OrderDate TEXT NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(Id)
);

CREATE TABLE Shipments(
    Id INTEGER NOT NULL PRIMARY KEY,
    OrderId INTEGER NOT NULL,
    ShipmentDate TEXT NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES Orders(Id)
);