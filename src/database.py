import pymysql
import csv
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def insert_transaction_data(csv_file, connection, database):
    """
    Inserts transaction data from a CSV file into the specified MySQL database.

    Args:
        csv_file (str): Path to the CSV file containing transaction data.
        connection: MySQL database connection object.
        database: Name of the database.

    Returns:
        None
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {database}")
            with open(csv_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        current_year = datetime.now().year
                        date_with_year = f"{row['Date']}/{current_year}"
                        date_value = datetime.strptime(date_with_year, '%m/%d/%Y').strftime('%Y-%m-%d')
                        cursor.execute("""
                            INSERT INTO transactions (ID, Date, `Transaction`)
                            VALUES (%s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                            Date = VALUES(Date),
                            `Transaction` = VALUES(`Transaction`)
                        """, (int(row['Id']), date_value, float(row['Transaction'])))
                    except pymysql.Error as e:
                        logger.error(f"Error inserting data: {e}")
        connection.commit()
    except pymysql.Error as e:
        logger.error(f"Error inserting transaction data: {e}")


def show_all_transactions(connection,database):
    """
    Displays all transactions stored in the specified MySQL database.

    Args:
        connection: MySQL database connection object.

    Returns:
        None
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {database}")
            cursor.execute("SELECT * FROM transactions")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except pymysql.Error as e:
        logger.error(f"Error retrieving transactions: {e}")
