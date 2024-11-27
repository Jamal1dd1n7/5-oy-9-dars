import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='postgres',
            user='postgres',
            host='localhost',
            password='252208'
        )
        self.table_names = []

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        result = None
        with self.database as db:
            with db.cursor() as cursor:
                if args:
                    cursor.execute(sql, args)
                else:
                    cursor.execute(sql)
                
                if commit:
                    db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
        return result
    
    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            category_name VARCHAR(50) NOT NULL UNIQUE
        );'''
        self.manager(sql, commit=True)

    def create_table_products(self):
        sql = '''CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            product_name VARCHAR(150) NOT NULL UNIQUE,
            product_price NUMERIC(7, 2) NOT NULL CHECK(product_price >= 0 AND product_price <= 99999.99),
            category_id INTEGER REFERENCES categories(category_id)
        );'''
        self.manager(sql, commit=True)

    def insert_categories(self):
        sql = '''
            INSERT INTO categories( category_name) VALUES
            ('Mevalar'),
            ('Ichimliklar'),
            ('Shirinliklar'),
            ('Fast Foodlar'),
            ('Xo`jalik mollari');
        '''
        self.manager(sql, commit=True)

    def insert_products(self):
        products = [
            ('Olma', 5000, 1),
            ('Banan', 12000, 1),
            ('Coca-Cola', 8000, 2),
            ('Fanta', 7500, 2),
            ('Shokolad', 10000, 3),
            ('Tort', 45000, 3),
            ('Burger', 25000, 4),
            ('Pizza', 60000, 4),
            ('Sovun', 3000, 5),
            ('Kir yuvish kukuni', 15000, 5),
            ('Non', 2500, None),
            ('Qand', 7000, None),
            ('Suv', 2000, None),
            ('Tuxum', 1200, None),
            ('Guruch', 10000, None)
        ] 
        for product in products:
            sql = '''
                INSERT INTO products( product_name, product_price, category_id) VALUES
                (%s, %s, %s);
            '''
            self.manager(sql, *product,commit=True)

    def join_categories(self):
        sql = '''
            SELECT categories.category_name, products.product_name 
            FROM categories 
            JOIN products 
            ON categories.category_id = products.category_id;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)


    def join_categories_is_null(self):
        sql = '''
            SELECT categories.category_name, products.product_name 
            FROM categories 
            LEFT JOIN products 
            ON categories.category_id = products.category_id;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)


    def join_products(self):
        sql ='''
            SELECT products.product_name, categories.category_name FROM products LEFT JOIN categories ON products.category_id = categories.category_id;
        ''' 
        result = self.manager(sql, fetchall=True)
        for a in result:
            print(a)
        
    def join_products_null(self):
        sql = '''
            SELECT product_name 
            FROM products 
            WHERE category_id IS NULL;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)

    def join_products_categories_null(self):
        sql = '''
            SELECT category_name 
            FROM categories 
            LEFT JOIN products 
            ON categories.category_id = products.category_id 
            WHERE products.category_id IS NULL;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)


    def select_products_categories(self):
        sql = '''
            SELECT categories.category_name, products.product_name 
            FROM categories 
            FULL OUTER JOIN products 
            ON categories.category_id = products.category_id;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)


    def not_joined(self):
        sql = '''
            SELECT categories.category_name AS unlinked_categories, 
                products.product_name AS unlinked_products 
            FROM categories 
            FULL OUTER JOIN products 
            ON categories.category_id = products.category_id 
            WHERE categories.category_id IS NULL OR products.category_id IS NULL;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)


    def cross_join(self):
        sql = '''
            SELECT categories.category_name, products.product_name 
            FROM categories 
            CROSS JOIN products;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)

    
    def natural_join(self):
        sql = '''
            SELECT * 
            FROM categories 
            NATURAL JOIN products;
        '''
        result = self.manager(sql, fetchall=True)
        for row in result:
            print(row)

    


    
    
        

































