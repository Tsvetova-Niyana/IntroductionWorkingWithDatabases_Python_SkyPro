import psycopg2
from function import *

if __name__ == '__main__':
    file_1 = "north_data/employees_data.csv"
    file_2 = "north_data/customers_data.csv"
    file_3 = "north_data/orders_data.csv"

    with psycopg2.connect(
            database="north",
            user="postgres",
            password="123") as conn:
        with conn.cursor() as cur:

            add_employee(file_1, cur)
            add_customers(file_2, cur)
            add_orders(file_3, cur)
