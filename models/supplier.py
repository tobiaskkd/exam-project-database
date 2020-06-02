class supplier():

    def __init__(self, supplier_id=None, supplier_name, supplier_phone, db_conn)
    self._supplier_id = suppplier_id
    self._supplier_name
    self._supplier_phone
    self._db_conn = db_conn


@property
   def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        if self._supplier_id:
            sql = 'UPDATE Supplier\n'
            sql += 'SET supplier_name = %s\n'
            sql += 'WHERE supplier_id = %s;'
            vals = (store_supplier, self._supplier_id)
            self._db_conn.query(sql, vals)
        self._supplier_name = supplier_name

    @property
    def supplier_phone(self):
        return self._supplier_phone

    @supplier_phone.setter
    def supplier_phone(self, supplier_phone):
        if self._supplier_id:
            sql = 'UPDATE Supplier\n'
            sql += 'SET supplier_phone = %s\n'
            sql += 'WHERE supplier_id = %s;'
            vals = (supplier_phone, self._supplier_id)
            self._db_conn.query(sql, vals)
        self._supplier_phone = supplier_phone

    def save(self):
        if self._supplier_id:
            raise Exception('Already saved')
        sql = "INSERT INTO Supplier"
        fields = (
            'supplier_name',
            'supplier_phone'
        )
        sql += "(%s, %s)\n" % fields
        sql += "VALUES (%s, %s);"
        vals = (
            self.supplier_name,
            self.supplier_phone
        )
        self._supplier_id = self._db_conn.query(sql, vals)
