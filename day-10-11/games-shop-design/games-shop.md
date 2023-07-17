# SQL Practice - Developing a database for a games shop

## Instructions
> Think about the type of data that a games shop would want to store in their database. From here, think about the tables that you might find in the games shop's database. What kinds of information will they store?

- Customers
- Products
  - Games
  - Consoles
- Orders
- Employees

## Data we want to track
- Game name
- Customer
  - Customer account?
- Stock Level / Inventory 
- Sales transaction
- Genre
- Game compatibility
- Suppliers
- Ratings / Reviews
- Prices

## Tables
### Customers
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| customer_ID | INT | PRIMARY KEY AUTO_INCREMENT |
| email | VARCHAR(50) | NOT NULL |
| phone_number | VARCHAR(50) |
| pwd | binary(20) | NOT NULL |
| salt | binary(20) | NOT NULL |

```sql
CREATE TABLE customers (
  customer_ID INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(50) NOT NULL,
  phone_number VARCHAR(50),
  pwd BINARY(20) NOT NULL,
  salt BINARY(20) NOT NULL
);
```
    
### Products
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| product_ID | INT | PRIMARY KEY AUTO_INCREMENT |
| product_name | VARCHAR(50) | NOT NULL |
| FK_genre_ID | INT | FOREIGN KEY NOT NULL |
| rating | INT | DEFAULT = 0 |
| price | FLOAT | NOT NULL |
| FK_supplier_ID | INT | FOREIGN KEY NOT NULL |
| inventory | INT | DEFAULT = 0 |

```sql
CREATE TABLE products (
  product_ID INT PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(50) NOT NULL,
  FK_genre_ID INT NOT NULL,
  rating INT DEFAULT 0,
  price FLOAT NOT NULL,
  FK_supplier_ID INT NOT NULL,
  inventory INT DEFAULT 0,
  FOREIGN KEY (FK_genre_ID) REFERENCES genres(genre_id),
  FOREIGN KEY (FK_supplier_ID) REFERENCES suppliers(supplier_ID)
);
```

### Orders
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| order_ID | INT | PRIMARY KEY AUTO_INCREMENT |
| FK_customer_ID | INT | FOREIGN KEY NOT NULL |
| FK_product_ID | INT | FOREIGN KEY NOT NULL |
| quantity | INT | DEFAULT = 1  |
| transaction_amount | FLOAT | NOT NULL |
| transaction_date | DATE | NOT NULL |

```sql
CREATE TABLE orders (
  order_ID INT PRIMARY KEY AUTO_INCREMENT,
  FK_customer_ID INT NOT NULL,
  FK_product_ID INT NOT NULL,
  quantity INT DEFAULT 1,
  transaction_amount FLOAT NOT NULL,
  transaction_date DATE NOT NULL,
  FOREIGN KEY (FK_customer_ID) REFERENCES customers(customer_ID),
  FOREIGN KEY (FK_product_ID) REFERENCES products(product_ID)
);
```

### Suppliers
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| supplier_ID | INT | PRIMARY KEY AUTO_INCREMENT | 
| supplier_name | VARCHAR(50) | NOT NULL |
| supplier_location | VARCHAR(50) | NOT NULL |

```sql
CREATE TABLE suppliers (
  supplier_ID INT PRIMARY KEY AUTO_INCREMENT,
  supplier_name VARCHAR(50) NOT NULL,
  supplier_location VARCHAR(50) NOT NULL
);
```

### Genres
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| genre_id | INT | PRIMARY KEY AUTO_INCREMENT | 
| genre_name | VARCHAR(50) | NOT NULL |

```sql
CREATE TABLE genres (
  genre_id INT PRIMARY KEY AUTO_INCREMENT,
  genre_name VARCHAR(50) NOT NULL
);
```

## Playing around with data
### Suppliers
```sql
INSERT INTO suppliers 
	(supplier_name, supplier_location)
VALUES
	("Xbox", "USA"),
	("Nintendo", "JP"),
	("Tencent", "CH"),
	("Ubisoft", "USA"),
	("Sony", "JP"),
	("TO_BE_DELETED", "AAA")
;

SELECT * FROM suppliers;

DELETE FROM suppliers
WHERE supplier_location="AAA";
```

### Genres
```sql
INSERT INTO genres
	(genre_name)
VALUES
	("Horror"),
	("Fantasy"),
	("FPS"),
	("MMORPG"),
	("Moba")
;
```

### Customers
```sql
INSERT INTO customers
	(email, pwd, salt)
VALUES
	("customer1@gmail.com", "hashed_pwd", "salt_placeholder"),
	("customer2@gmail.com", "hashed_pwd", "salt_placeholder"),
	("customer3@gmail.com", "hashed_pwd", "salt_placeholder"),
	("customer4@gmail.com", "hashed_pwd", "salt_placeholder"),
	("customer5@gmail.com", "hashed_pwd", "salt_placeholder")
;
```

### Products
```sql
INSERT INTO products
	(product_name, FK_genre_ID, price, FK_supplier_ID, inventory)
VALUES
	("Game 1", 1, 9.99, 1, 5),
	("Game 2", 5, 8.77, 3, 8),
	("Game 3", 2, 14.99, 4, 3),
	("Game 4", 4, 19.99, 5, 1),
	("Game 5", 3, 49.99, 2, 0)
; 
```

### Orders
```sql
INSERT INTO orders
	(FK_customer_ID, FK_product_ID, transaction_amount, transaction_date)
VALUES
	(1, 1, 14.99, '2023-02-06'),
	(2, 2, 13.77, '2023-03-22'),
	(1, 3, 19.99, '2022-02-24'),
	(4, 4, 24.99, '2023-04-17'),
	(3, 5, 55.99, '2023-06-03')
;

UPDATE orders
SET transaction_amount=54.99
WHERE transaction_date='2023-06-03'
;
```