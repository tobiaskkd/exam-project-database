from models.db_connection import DBConnection
from models.employee import Employee

if __name__ == "__main__":
    dbcon = DBConnection()

    employee = Employee(
        'lars',
        'Ørred',
        'Manager',
        '2020-05-13',
        300000,
        'male',
        1,
        dbcon
    )
    employee.save()
    employee.createUser('tissemand5', 'rasha')