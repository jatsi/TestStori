
# TestStori

TestStori is a project designed to process transaction data, store it in a database, send summary emails, and provide logging functionality.

## Project Structure

```
TestStori/
│
├── resources/
│   └── assets/
│        └── Stori_logo_vertical.png   # Stori Logo
│
├── src/
│   ├── process_transactions.py        # Script to process the CSV file of transactions
│   ├── email_sender.py                # Script to send emails
│   ├── database.py                    # Script to interact with the MySQL database
│   └── main.py                        # Main script orchestrating the process
│
├── entrypoint.sh                      # Entrypoint script for Docker container
├── docker-compose.yml                 # Docker Compose file for setting up the environment
├── Dockerfile                         # Dockerfile for building the Docker image
├── requirements.txt                   # Python requirements file
├── init.sql                           # SQL script for initializing the database
└── README.md                          # Project instructions and documentation
```

## Description

- **resources/assets/Stori_logo_vertical.png**: This directory contains the Stori logo used in the project.

- **src/**: This directory contains Python scripts responsible for different functionalities of the project.
  - `process_transactions.py`: Script to process the CSV file of transactions.
  - `email_sender.py`: Script to send emails.
  - `database.py`: Script to interact with the MySQL database.
  - `main.py`: Main script orchestrating the process.

- **entrypoint.sh**: This Bash script serves as the entrypoint for the Docker container. It waits for 30 seconds before starting the `teststori` service.

- **docker-compose.yml**: This file defines the services, networks, and volumes required for the Docker environment setup.

- **Dockerfile**: This file contains instructions for building the Docker image.

- **requirements.txt**: This file lists the Python dependencies required for the project.

- **init.sql**: SQL script for initializing the database. It creates a `transactions` database and a `transactions` table with columns `Id`, `Date`, and `Transaction`.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your_username/TestStori.git
```

2. Navigate to the project directory:

```bash
cd TestStori
```

3. Fill in the necessary data in the `docker-compose.yml` file. Update the environment variables under the `teststori` service with your desired values.

      MySQL Service:
         Change `your_root_password_here` to your desired password for the MySQL root user.

      teststori Service:
         Change `/path/to/your/local/data` to the path of your local data you want to mount in the container.
         Specify the destination email address (`DEST_EMAIL`), SMTP server (`SMTP_SERVER`), SMTP port (`SMTP_PORT`), SMTP username (`SMTP_USERNAME`), SMTP password (`SMTP_PASSWORD`), MySQL database host (`DB_HOST`), MySQL database user (`DB_USER`), MySQL database password (`DB_PASSWORD`), and MySQL database name (`DB_DATABASE`).
4. Build and run the Docker containers:

```bash
docker-compose up --build
```

5. Access the application through the specified endpoints or functionalities.

## Author

This project was created by [Katia R Benitez Castro](mailto:jatsi.1992@gmail.com).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
