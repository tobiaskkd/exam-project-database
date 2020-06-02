class Customer():

    def __init__(self, customer_id=None, first_name, middle_name, last_name, customer_phone, customer_email, customer_address):
        self._customer_id = customer_id
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._customer_phone = customer_phone
        self._customer_email = customer_email
        self._customer_address = customer_address

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if self._customer_id:
            sql = 'UPDATE Customers'
            sql += 'SET first_name = %s'
            sql += 'WHERE customer_id = %s'
            vals = (first_name, self._customer_id)
            self._db_conn.execute(sql, vals)
        self._first_name = first_name

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        if self._customer_id:
            sql = 'UPDATE Customers'
            sql += 'SET middle_name = %s'
            sql += 'WHERE customer_id = %s'
            vals = (middle_name, self._customer_id)
            self._db_conn.execute(sql, vals)
        self._middle_name = middle_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if self._customer_id:
            sql = 'UPDATE Customers'
            sql += 'SET last_name = %s'
            sql += 'WHERE customer_id = %s'
            vals = (last_name, self._customer_id)
            self._db_conn.execute(sql, vals)
        self._last_name = last_name

    @property
    def customer_phone(self):
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, customer_phone):
        if self._customer_id:
            sql = 'UPDATE Customers'
            sql += 'SET customer_phone = %s'
            sql += 'WHERE customer_id = %s'
            vals = (customer_phone, self._customer_id)
            self._db_conn.execute(sql, vals)
        self._customer_phone = customer_phone

    @property
    def customer_email(self):
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        if self._customer_id:
            sql = 'UPDATE Customers'
            sql += 'SET customer_email = %s'
            sql += 'WHERE customer_id = %s'
            vals = (customer_email, self._customer_id)
            self._db_conn.execute(sql, vals)
        self._customer_email = customer_email

    @property
    def customer_address(self):
        return self._customer_address

    @customer_address.setter
    def customer_address(self, customer_address):
        if self._customer_id:
            sql = 'UPDATE Customers'
            sql += 'SET customer_address = %s'
            sql += 'WHERE customer_id = %s'
            vals = (customer_address, self._customer_id)
            self._db_conn.execute(sql, vals)
        self._customer_address = customer_address

    def save(self):
        if self._customer_id:
            raise Exception('Already created')
        sql = 'INSERT INTO Customers'
        fields += (
            'customer_id',
            'first_name',
            'middle_name',
            'last_name',
            'customer_phone',
            'customer_email',
            'customer_address'
        )
        sql += "('%s', '%s', '%s', '%s','%s', '%s')\n" % fields
        sql += "VALUES ('%s', '%s', '%s', '%s','%s', '%s');"

        vals = (
            self.customer_id,
            self.first_name,
            self.middle_name,
            self.last_name,
            self.customer_phone,
            self.customer_email,
            self.customer_address
        )
        self.customer_id = self._db_conn.query(sql, vals)


    def createUser(self):
        pass
