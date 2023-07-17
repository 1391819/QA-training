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
| FK_genre_ID | INT | FOREIGN KEY |
| rating | INT | DEFAULT = 0 |
| price | FLOAT | NOT NULL |
| FK_supplier_ID | INT | FOREIGN KEY |
| inventory | INT | DEFAULT = 0 |

```sql
CREATE TABLE products (
  product_ID INT PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(50) NOT NULL,
  FK_genre_id INT NOT NULL,
  rating INT DEFAULT 0,
  price FLOAT NOT NULL,
  FK_supplier_ID INT NOT NULL,
  inventory INT DEFAULT 0,
  FOREIGN KEY (FK_genre_id) REFERENCES genres(genre_id),
  FOREIGN KEY (FK_supplier_ID) REFERENCES suppliers(supplier_ID)
);
```

### Orders
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| order_ID | INT | PRIMARY KEY AUTO_INCREMENT |
| FK_customer_ID | INT | FOREIGN KEY |
| FK_product_ID | INT | FOREIGN KEY |
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
  supplier_ID INT PRIMARY KEY AUTO_INCREMENT ,
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
  genre_id INT PRIMARY KEY AUTO_INCREMENT ,
  genre_name VARCHAR(50) NOT NULL
);
```