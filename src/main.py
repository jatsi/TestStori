import pymysql
from process_transactions import process_transactions
from database import insert_transaction_data, show_all_transactions
from email_sender import send_email
import logging
import os

# Configure event logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(dest_email: str, smtp_server: str, smtp_port: int, smtp_username: str, smtp_password: str, db_host: str, db_user: str, db_password: str, db_database: str):
    """
    Main function that processes transaction data, stores it in a MySQL database,
    sends a summary via email, and logs events.

    Args:
        dest_email (str): Destination email address for the summary email.
        smtp_server (str): SMTP server for sending emails.
        smtp_port (int): SMTP port of the server.
        smtp_username (str): SMTP username.
        smtp_password (str): SMTP password.
        db_host (str): MySQL database host.
        db_user (str): MySQL database user.
        db_password (str): MySQL database password.
        db_database (str): MySQL database name.

    Returns:
        None
    """
    try:
        # Establish connection to MySQL database
        db_connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database,
            cursorclass=pymysql.cursors.DictCursor
        )

        # Step 1: Process the CSV file of transactions
        logger.info("Processing the CSV file of transactions...")
        transaction_data = process_transactions("data/transactions.csv")

        # Step 3: Insert transaction data into MySQL database
        logger.info("Inserting transaction data into the database...")
        insert_transaction_data("data/transactions.csv", db_connection, db_database)
        logger.info("Transaction data inserted successfully.")

        # Show all transactions in the transactions table (optional)
        logger.info("Showing all data from the transactions table...")
        show_all_transactions(db_connection, db_database)
        logger.info("Transaction data displayed successfully.")

        # Send email with the summary information
        logger.info("Sending email with summary information...")
        subject = "Stori Transaction Summary"
        send_email(subject, transaction_data, smtp_username, dest_email, smtp_server, smtp_port, smtp_username, smtp_password)
        logger.info("Email sent successfully.")

    except Exception as e:
        # Catch any exceptions and log them
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Call the main function with the provided arguments as environment variables
    main(
        os.getenv('DEST_EMAIL'),
        os.getenv('SMTP_SERVER'),
        int(os.getenv('SMTP_PORT')),
        os.getenv('SMTP_USERNAME'),
        os.getenv('SMTP_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_DATABASE')
    )
