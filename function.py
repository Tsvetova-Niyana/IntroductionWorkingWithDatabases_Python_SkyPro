import csv


def add_employee(file_name, cur):
    """Функция добавления данных в таблицу employees из файла employees_data.csv"""

    with open(file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                """INSERT INTO employees(first_name, last_name, title, birth_date, notes)
                VALUES(%s, %s, %s, %s, %s)
            """, (row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))


def add_customers(file_name, cur):
    """Функция добавления данных в таблицу customers из файла customers_data.csv"""

    with open(file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                """INSERT INTO customers (customer_id, company_name, contact_name)
                VALUES(%s, %s, %s)
                """, (row["customer_id"], row["company_name"], row["contact_name"])
            )


def add_orders(file_name, cur):
    """Функция добавления данных в таблицу orders из файла orders_data.csv"""
    with open(file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                """INSERT INTO orders(order_id, customer_id, employee_id, order_date, ship_city)
                VALUES(%s, %s, %s, %s, %s)
                """, (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"])
            )


