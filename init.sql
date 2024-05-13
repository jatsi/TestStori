
CREATE DATABASE  transactions
    DEFAULT CHARACTER SET = 'utf8mb4';

use transactions;

CREATE TABLE transactions (
    Id INT PRIMARY KEY,
    Date DATE,
    Transaction DECIMAL(12,2)
);