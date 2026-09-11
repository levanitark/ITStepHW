-- 0
CREATE DATABASE IF NOT EXISTS hw_26;
USE hw_26;

-- 1.
CREATE TABLE Authors (
    AuthorID   INT AUTO_INCREMENT PRIMARY KEY,
    FirstName  VARCHAR(50) NOT NULL,
    LastName   VARCHAR(50) NOT NULL,
    Country    VARCHAR(50)
);

-- 2.
CREATE TABLE Books (
    BookID     INT AUTO_INCREMENT PRIMARY KEY,
    Title      VARCHAR(100) NOT NULL,
    PubYear    INT,
    AuthorID   INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

-- 3.
INSERT INTO Authors (FirstName, LastName, Country)
VALUES
    ('Shota', 'Rustaveli', 'Georgia'),
    ('George', 'Orwell', 'UK'),
    ('Osamu', 'Dazai', 'Japan'),
    ('Daniel', 'Keyes', 'USA'),
    ('Albert', 'Camus', 'France');

INSERT INTO Books (Title, PubYear, AuthorID)
VALUES
    ('The Knight in the Panther''s Skin', 1200, 1),
    ('1984', 1949, 2),
    ('Animal Farm', 1945, 2),
    ('No Longer Human', 1948, 3),
    ('Flowers for Algernon', 1959, 4),
    ('The Foreigner', 1942, 5);

-- 4.
UPDATE Books
SET PubYear = 1966
WHERE BookID = 5;

-- 5.
SELECT b.BookID, b.Title, b.PubYear, a.FirstName, a.LastName, a.Country
FROM Books b
JOIN Authors a
ON b.AuthorID = a.AuthorID;

-- 6.
SET SQL_SAFE_UPDATES = 0;
DELETE FROM Books;
DELETE FROM Authors;
SET SQL_SAFE_UPDATES = 1;

-- 7.
DROP TABLE Books;
DROP TABLE Authors;