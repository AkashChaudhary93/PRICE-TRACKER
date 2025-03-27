import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_prices (
                product_name TEXT NOT NULL,
                platform TEXT NOT NULL,
                price REAL,
                PRIMARY KEY (product_name, platform)
            )
        """)
        self.conn.commit()

    def insert_price(self, product_name, platform, price):
        self.cursor.execute("""
            INSERT OR REPLACE INTO product_prices (product_name, platform, price)
            VALUES (?, ?, ?)
        """, (product_name, platform, price))
        self.conn.commit()

    def get_price(self, product_name, platform):
        self.cursor.execute("""
            SELECT price FROM product_prices
            WHERE product_name = ? AND platform = ?
        """, (product_name, platform))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close_connection(self):
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    # Example usage (for testing this module independently)
    db = DatabaseManager("test_prices.db")
    db.insert_price("Laptop", "Amazon", 50000.00)
    price = db.get_price("Laptop", "Amazon")
    print(f"Price of Laptop on Amazon: {price}")
    db.close_connection()