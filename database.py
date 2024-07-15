import sqlite3

class EmployeeDB:
    def __init__(self):
        self.connection = sqlite3.connect('employees.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Create an Employee table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employee (
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                Age INTEGER,
                Gender TEXT,
                Phone TEXT,
                Date_Of_Birth TEXT,
                Email TEXT,
                Department TEXT,
                Date_of_Joining TEXT,
                Skill TEXT,
                Basic_Salary REAL,
                Total_Salary REAL,
                Address TEXT
            )
        ''')
        self.connection.commit()

    def check_id_exists(self, id):
        self.cursor.execute('SELECT * FROM Employee WHERE ID=?', (id,))
        row = self.cursor.fetchone()
        return row is not None
    def check_phone_exists(self, phone):
        self.cursor.execute('SELECT * FROM Employee WHERE Phone=?', (phone,))
        row = self.cursor.fetchone()
        return row is not None

    def search_by_phone(self, phone):
        self.cursor.execute("SELECT * FROM Employee WHERE Phone=?", (phone,))
        rows = self.cursor.fetchall()
        return rows

    def search_by_id(self, id):
        self.cursor.execute("SELECT * FROM Employee WHERE ID=?", (id,))
        rows = self.cursor.fetchall()
        return rows

    def insert_data(self, id, name, age, gender, phone, dob, email, department, doj, skill, bs, ts, address):
        if self.check_phone_exists(phone):
            return "Phone number already exists"
        else:
            self.cursor.execute('''
                INSERT INTO Employee (ID, Name, Age, Gender, Phone, Date_Of_Birth, Email, Department, Date_of_Joining, Skill, Basic_Salary, Total_Salary, Address)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id, name, age, gender, phone, dob, email, department, doj, skill, bs, ts, address))
            self.connection.commit()
            return "Record inserted successfully"

    def fetch_data(self):
        self.cursor.execute('SELECT * FROM Employee')
        rows = self.cursor.fetchall()
        return rows

    def update_data(self, id, name, age, gender, phone, dob, email, department, doj, skill, bs, ts, address):
        self.cursor.execute('''
            UPDATE Employee SET Name=?, Age=?, Gender=?, Phone=?, Date_Of_Birth=?, Email=?, Department=?, Date_of_Joining=?, Skill=?, Basic_Salary=?, Total_Salary=?, Address=?
            WHERE ID=?
        ''', (name, age, gender, phone, dob, email, department, doj, skill, bs, ts, address, id))
        self.connection.commit()

    def delete_data(self, id):
        self.cursor.execute('DELETE FROM Employee WHERE ID=?', (id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()