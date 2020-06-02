class Products():

    def __init__(self, product_name, product_brand, supplier_id, product_stock, product_is_active, db_conn, product_id=None)
    self._product_id = product_id
    self._supplier_id = supplier_id
    self._product_name = product_name
    self._produxt_brand = product_brand
    self._product_stock = product_stock
    self._product_is_active = product_is_active
    self._db_conn = db_conn

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        if self._product_id:
            sql = 'UPDATE Prodducts\n'
            sql += 'SET product_name = %s\n'
            sql += 'WHERE product_id = %s;'
            vals = (product_name, self._product_id)
            self._db_conn.query(sql, vals)
        self._product_name = product_name

    @property
    def product_brand(self):
        return self._product_brand

    @product_brand.setter
    def product_brand(self, product_brand):
        if self._product_id:
            sql = 'UPDATE Products\n'
            sql += 'SET product_brand = %s\n'
            sql += 'WHERE product_id = %s;'
            vals = (product_brand, self._product_id)
            self._db_conn.query(sql, vals)
        self._product_brand = product_brand

    @property
    def product_stock(self):
        return self._product_stock

    @product_stock.setter
    def product_stock(self, product_stock):
        if self._product_id:
            sql = 'UPDATE Products\n'
            sql += 'SET product_stock = %s\n'
            sql += 'WHERE product_id = %s;'
            vals = (product_stock, self._product_id)
            self._db_conn.query(sql, vals)
        self._product_stock = product_stock

    @property
    def product_is_active(self):
        return self._product_is_active

    @product_is_active.setter
    def product_is_active(self, product_is_active):
        if self._product_id:
            sql = 'UPDATE Products\n'
            sql += 'SET product_is_active = %s\n'
            sql += 'WHERE product_id = %s;'
            vals = (product_is_active, self._product_is_active)
            self._db_conn.query(sql, vals)
        self._product_is_active = product_is_active

    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        if self._product_id:
            sql = 'UPDATE Products'
            sql += 'SET supplier_id = %s'
            sql += 'WHERE product_id = %s'
            vals = (supplier_id, self._product_id)
            self._db_conn.query(sql, vals)
        self._supplier_id = supplier_id

    
     def save(self):
        if self._product_id:
            raise Exception('Already saved')
        sql = "INSERT INTO Products"
        fields = (
            'product_name',
            'product_brand',
            'product_stock',
            'product_is_active'
        )
        sql += "(%s, %s)\n" % fields
        sql += "VALUES (%s, %s, %s, %s);"
        vals = (
            self.product_name = product_name,
            self.produxt_brand = product_brand,
            self.product_stock = product_stock,
            self.product_is_active = product_is_active
        )
        self._product_id = self._db_conn.query(sql, vals)
