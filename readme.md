# SARS-CoV-2 Vaccine Distribution Center

This repository contains a Python and SQLite-based implementation of a database system for managing a SARS-CoV-2 vaccine distribution center. The project was developed as part of the SPL211 course (Assignment 4).

## Assignment Overview

- **Create and Populate Database**: Build and populate an SQLite database (`database.db`) from a configuration file (`config.txt`).
- **Process Orders**: Execute a list of orders from an orders file (`orders.txt`) to receive vaccine shipments from suppliers and send vaccine doses to clinics.
- **Generate Summary**: Output a summary file (`output.txt`) that records the total inventory, total demand, total received shipments, and total sent shipments after each order.

## Files

- `main.py`: Main script for initializing the database, processing incoming orders, and writing the summary output.
- `repository.py`: Manages the persistence layer and orchestrates data operations.
- `vaccines.py`: Contains the Data Access Object (DAO) and Data Transfer Object (DTO) classes for the Vaccines table.
- `suppliers.py`: Contains DAO and DTO classes for the Suppliers table.
- `clinics.py`: Contains DAO and DTO classes for the Clinics table.
- `logistics.py`: Contains DAO and DTO classes for the Logistics table.

## How to Run

```
python3 main.py config.txt orders.txt output.txt
```

Make sure `config.txt` and `orders.txt` are located in the same directory as `main.py`.

## Project Highlights

- Implementation of a Persistence Layer using the DAO and DTO design patterns.
- Support for FIFO (First In First Out) vaccine shipment handling.
- Consistent transaction management to ensure database integrity.
- Clear separation between data representation, business logic, and storage.
