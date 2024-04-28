import psycopg2 as db


def create_product_table():
    try:
        connection = db.connect(
            user="postgres",
            password="LevRaven.1",
            host="localhost",
            port=5432,
            database="production"
        )

        cursor = connection.cursor()

        create_table_query = '''CREATE TABLE IF NOT EXISTS products
                                (id SERIAL PRIMARY KEY,
                                name VARCHAR(255) NOT NULL,
                                price NUMERIC(10, 2) NOT NULL,
                                color VARCHAR(50),
                                image VARCHAR(255))'''

        cursor.execute(create_table_query)
        connection.commit()

        print("Product table created successfully!")

        insert_data(connection)
        update_data(connection)
        delete_data(connection)
        select_one_data(connection)
        select_all_data(connection)

    except (Exception, db.DatabaseError) as error:
        print("Error while working with PostgreSQL:", error)

        if connection:
            connection.rollback()
    else:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def insert_data(connection):
    try:
        cursor = connection.cursor()

        product_data = [
            ("Product 1", 10.99, "Red", "image1.jpg"),
            ("Product 2", 19.99, "Blue", "image2.jpg"),
            ("Product 3", 15.49, "Green", "image3.jpg")
        ]

        insert_query = '''INSERT INTO products (name, price, color, image)
                          VALUES (%s, %s, %s, %s)'''

        cursor.executemany(insert_query, product_data)
        connection.commit()

        print("Data inserted successfully!")

    except (Exception, db.DatabaseError) as error:
        print("Error while inserting data into PostgreSQL table:", error)

        if connection:
            connection.rollback()

        raise error
    else:
        cursor.close()


def update_data(connection):
    try:
        cursor = connection.cursor()

        update_query = '''UPDATE products
                          SET price = %s
                          WHERE id = %s'''

        cursor.execute(update_query, (12.99, 1))
        connection.commit()

        print("Data updated successfully!")

    except (Exception, db.DatabaseError) as error:
        print("Error while updating data in PostgreSQL table:", error)

        if connection:
            connection.rollback()

        raise error
    else:
        cursor.close()


def delete_data(connection):
    try:
        cursor = connection.cursor()

        delete_query = '''DELETE FROM products
                          WHERE id = %s'''

        cursor.execute(delete_query, (3,))
        connection.commit()

        print("Data deleted successfully!")

    except (Exception, db.DatabaseError) as error:
        print("Error while deleting data from PostgreSQL table:", error)

        if connection:
            connection.rollback()

        raise error
    else:
        cursor.close()


def select_one_data(connection):
    try:
        cursor = connection.cursor()

        select_query = '''SELECT * FROM products
                          WHERE id = %s'''

        cursor.execute(select_query, (1,))
        product = cursor.fetchone()

        print("Selected product:", product)

    except (Exception, db.DatabaseError) as error:
        print("Error while selecting data from PostgreSQL table:", error)

        if connection:
            connection.rollback()

        raise error
    else:
        cursor.close()


def select_all_data(connection):
    try:
        cursor = connection.cursor()

        select_query = '''SELECT * FROM products'''

        cursor.execute(select_query)
        products = cursor.fetchall()

        print("All products:")
        for product in products:
            print(product)

    except (Exception, db.DatabaseError) as error:
        print("Error while selecting data from PostgreSQL table:", error)

        if connection:
            connection.rollback()

        raise error
    else:
        cursor.close()


create_product_table()
