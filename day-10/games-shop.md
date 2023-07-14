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
| customer_ID | INT | PRIMARY KEY |
| email | VARCHAR(50) | NOT NULL |
| phone_number | VARCHAR(50) |
| hash | binary(20) | NOT NULL |
| salt | binary(20) | NOT NULL |

```sql
CREATE TABLE customers (
  customer_ID INT PRIMARY KEY,
  email VARCHAR(50) NOT NULL,
  phone_number VARCHAR(50),
  hash BINARY(20) NOT NULL,
  salt BINARY(20) NOT NULL
);
```
    
### Products
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| product_ID | INT | PRIMARY KEY |
| name | VARCHAR(50) | NOT NULL |
| genre_ID | INT | FOREIGN KEY |
| rating | INT | DEFAULT = 0 |
| price | FLOAT | NOT NULL |
| supplier_ID | INT | FOREIGN KEY |
| stock | INT | DEFAULT = 0 |

```sql
CREATE TABLE products (
  product_ID INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  genre_id INT,
  rating INT DEFAULT 0,
  price FLOAT NOT NULL,
  supplier_ID INT,
  stock INT DEFAULT 0,
  FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
  FOREIGN KEY (supplier_ID) REFERENCES suppliers(supplier_ID)
);

```

### Orders
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| order_ID | INT | PRIMARY KEY |
| customer_ID | INT | FOREIGN KEY |
| product_ID | INT | FOREIGN KEY |
| quantity | INT | DEFAULT = 1  |
| amount | FLOAT | NOT NULL |
| sale | DATE | NOT NULL |

```sql
CREATE TABLE orders (
  order_ID INT PRIMARY KEY,
  customer_ID INT,
  product_ID INT,
  quantity INT DEFAULT 1,
  amount FLOAT NOT NULL,
  sale DATE NOT NULL,
  FOREIGN KEY (customer_ID) REFERENCES customers(customer_ID),
  FOREIGN KEY (product_ID) REFERENCES products(product_ID)
);
```

### Suppliers
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| supplier_ID | INT | PRIMARY KEY | 
| supplier_name | VARCHAR(50) | NOT NULL |
| location | VARCHAR(50) | NOT NULL |

```sql
CREATE TABLE suppliers (
  supplier_ID INT PRIMARY KEY,
  supplier_name VARCHAR(50) NOT NULL,
  location VARCHAR(50) NOT NULL
);
```

### Genres
| Field | Type | Constraints |
| ----- | ---- | ----------- |
| genre_id | INT | PRIMARY KEY |
| genre_name | VARCHAR(50) | NOT NULL |

```sql
CREATE TABLE genres (
  genre_id INT PRIMARY KEY,
  genre_name VARCHAR(50) NOT NULL
);
```