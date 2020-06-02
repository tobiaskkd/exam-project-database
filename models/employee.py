class Employee():

    def __init__(self, first_name, last_name, title, start_date, salary, gender, store_id, db_conn, end_date=None, em_id=None):
        self._first_name = first_name
        self._last_name = last_name
        self._title = title
        self._start_date = start_date
        self._salary = salary
        self._gender = gender
        self._store_id = store_id
        self._db_conn = db_conn
        self._end_date = end_date
        self._em_id = em_id
        self._username = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET first_name = %s\n'
            sql += 'WHERE employee_id = %s;'
            vals = (first_name, self._em_id)
            self._db_conn.query(sql, vals)
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET last_name = %s\n'
            sql += 'WHERE employee_id = %s'
            vals = (last_name, self._em_id)
            self._db_conn.query(sql, vals)
        self._last_name = last_name

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET title = %s\n'
            sql += 'WHERE employee_id = %s'
            vals = (title, self._em_id)
            self._db_conn.query(sql, vals)
        self._title = title

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET start_date = %s\n'
            sql += 'WHERE employee_id = %s'
            vals = (start_date, self._em_id)
            self._db_conn.query(sql, vals)
        self._start_date = start_date

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET salary = %s\n'
            sql += 'WHERE employee_id = %s'
            vals = (salary, self._em_id)
            self._db_conn.query(sql, vals)
        self._salary = salary

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET gender = %s\n'
            sql += 'WHERE employee_id = %s'
            vals = (gender, self._em_id)
            self._db_conn.query(sql, vals)
        self._gender = gender

    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        if self._em_id:
            sql = 'UPDATE Employees'
            sql += 'SET store_id = %s'
            sql += 'WHERE employee_id = %s'
            vals = (store_id, self._em_id)
            self._db_conn.query(sql, vals)
        self._store_id = store_id

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if self._em_id:
            sql = 'UPDATE Employees\n'
            sql += 'SET end_date = %s\n'
            sql += 'WHERE employee_id = %s'
            vals = (end_date, self._em_id)
            self._db_conn.query(sql, vals)
        self._end_date = end_date

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if self._em_id and username:
            sql = 'UPDATE Employees\n'
            sql += 'SET employee_username = %s\n'
            sql += 'WHERE employee_id = %s;'
            vals = (username, self._em_id)
            self._db_conn.query(sql, vals)
        self._username = username

    def save(self):
        if self._em_id:
            raise Exception('Already saved')
        sql = "INSERT INTO Employees"
        fields = (
            'first_name',
            'last_name',
            'employee_title',
            'employee_start_date',
            'employee_salary',
            'employee_gender',
            'Store_store_id'
        )
        sql += "(%s, %s, %s, %s, %s, %s, %s)\n" % fields
        sql += "VALUES (%s, %s, %s, %s, %s, %s, %s);"
        vals = (
            self.first_name,
            self.last_name,
            self.title,
            self.start_date,
            self.salary,
            self.gender,
            self.store_id,
        )
        self._em_id = self._db_conn.query(sql, vals)

    def createUser(self, username, password):
        roles = {
            'Manager': 'GRANT ALL ON',
            'Warehouse Employee': 'GRANT SELECT, INSERT, TRIGGER ON TABLE',
            'Sales Assistant': 'GRANT SELECT, INSERT, TRIGGER ON TABLE',
        }
        sql = "create user %s identified by '%s';" % (
            username, password)
        self._db_conn.query(sql)
        sql = "%s supershopdb.* to %s;" % (roles[self.title], username)
        self._db_conn.query(sql)
        self.username = username