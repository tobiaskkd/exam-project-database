class store():

    def __init__(self, store_id=None, store_title, store_address, store_phone, db_conn)
    self._store_id = store_id
    self._store_title
    self._store_address
    self._store_phone
    self._db_conn = db_conn

    @property
    def store_title(self):
        return self._first_name

    @store_title.setter
    def store_title(self, store_title):
        if self._store_id:
            sql = 'UPDATE Store\n'
            sql += 'SET store_title = %s\n'
            sql += 'WHERE store_id = %s;'
            vals = (store_title, self._store_id)
            self._db_conn.query(sql, vals)
        self._store_title = store_title

    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, store_address):
        if self._store_id:
            sql = 'UPDATE Store\n'
            sql += 'SET store_address = %s\n'
            sql += 'WHERE store_id = %s'
            vals = (store_address, self._store_id)
            self._db_conn.query(sql, vals)
        self._store_address = store_address

    @property
    def store_phone(self):
        return self._store_phone

    @store_phone.setter
    def store_phone(self, store_phone):
        if self._store_id:
            sql = 'UPDATE Store\n'
            sql += 'SET store_phone = %s\n'
            sql += 'WHERE store_id = %s'
            vals = (store_phone, self._store_id)
            self._db_conn.query(sql, vals)
        self._store_phone = store_phone

    def save(self):
        if self._store_id:
            raise Exception('Already saved')
        sql = "INSERT INTO Store"
        fields = (
            'store_title',
            'store_address',
            'store_phone'
        )
        sql += "(%s, %s, %s)\n" % fields
        sql += "VALUES (%s, %s, %s);"
        vals = (
            self.store_title,
            self.store_address,
            self.store_phone
        )
        self._store_id = self._db_conn.query(sql, vals)
