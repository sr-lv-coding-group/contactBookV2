# Contact Book V2
## General Information
Contact Book V2 is a simple command-line application designed to manage contact information. Users can add, update, delete, and view contact records stored in a SQLite3 database. Each contact record includes details such as name, age, phone number, and location.

##Technologies
This application is built using the following technologies:

Python: The primary programming language used for the application logic.
SQLite3: The database management system used to store and manage contact records.
## Setup
How to Connect to the Database for SQLite3
To connect to the SQLite3 database for Contact Book V2, follow these steps:

Ensure you have SQLite3 installed on your system. You can check this by running the following command in your terminal:

sqlite3 --version
If SQLite3 is not installed, you can download and install it from the official SQLite website.

Clone the repository (if applicable) and navigate to the project directory:

git clone https://github.com/yourusername/contact-book-v2.git
cd contact-book-v2
Run the application to ensure the database file (contacts.db) is created and populated with initial data (if applicable).

Connect to the database using the SQLite3 command-line tool:

sqlite3 contacts.db
Once connected, you will see the SQLite prompt (sqlite>), indicating that you are now connected to the database. You can start executing SQL commands directly from this prompt.

## Example session:

$ sqlite3 contacts.db
SQLite version 3.34.0 2020-12-01 16:14:00
Enter ".help" for usage hints.
sqlite> .tables
CONTACTS
sqlite> SELECT * FROM CONTACTS;
1|John Doe|30|123-456-7890|New York
2|Jane Smith|25|987-654-3210|Los Angeles
sqlite> .exit