CREATE TABLE customer (
    customer_id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_id TEXT NOT NULL,
    birth_date INTEGER NOT NULL,
    home_address TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email_address TEXT NOT NULL
);

CREATE TABLE employee (
    employee_id INTEGER NOT NULL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    home_address TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    work_availability INTEGER NOT NULL,
    hour_worked INTEGER
);

CREATE TABLE dvd (
    dvd_id INTEGER NOT NULL PRIMARY KEY,
    title TEXT NOT NULL,
    actor TEXT NOT NULL,
    director TEXT NOT NULL,
    genre TEXT NOT NULL,
    rent_price REAL NOT NULL,
    sell_price REAL NOT NULL,
    amount_instock INTEGER NOT NULL,
    amount_bought INTEGER NOT NULL,
    amount_sold INTEGER NOT NULL
);

CREATE TABLE administrator (
    admin_id INTEGER NOT NULL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE credit_card (
    card_number TEXT NOT NULL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    expire_date INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE rental (
    rental_id INTEGER NOT NULL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    dvd_id INTEGER NOT NULL,
    rent_date INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (dvd_id) REFERENCES dvd(dvd_id)
);

CREATE TABLE request (
    customer_id INTEGER NOT NULL,
    dvd_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (dvd_id) REFERENCES dvd(dvd_id),
    PRIMARY KEY (customer_id, dvd_id)
);
