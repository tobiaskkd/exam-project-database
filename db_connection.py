import mysql.connector
import yaml


class DBConnection():

    def __init__(self):
        self._host = self.readConfig('host')
        self._user = self.readConfig('user')
        self._password = self.readConfig('password')
        self._port = self.readConfig('port')
        self._database = self.createDB()
        self._dbcon = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database,
            port=self._port
        )
        self._cursor = self._dbcon.cursor(buffered=True)
        self.createTables()

    @property
    def connection(self):
        return self._db_conn

    @property
    def cursor(self):
        return self._cursor

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @user.setter
    def user(self, user):
        self._user = user

    @password.setter
    def password(self, password):
        self._password = password

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None, multi=False):
        self.cursor.execute(sql, params or (), multi=multi)

    def tableExists(self, table_name=None):
        if self.showTables():
            return table_name in self.showTables()
        return False

    def showTables(self):
        return self.execute('SHOW TABLES')

    def readConfig(self, setting):
        with open('config/config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return config[setting]

    def createDBCustomers(self):
        if self.tableExists('Customers'):
            return False
        self.execute("CREATE TABLE IF NOT EXISTS Customers (customer_id INT NOT NULL, first_name VARCHAR(45) NOT NULL, middle_name VARCHAR(45) NOT NULL, last_name VARCHAR(45) NOT NULL, customer_phone VARCHAR(11) NOT NULL, customer_email VARCHAR(45) NOT NULL, customer_address VARCHAR(45) NOT NULL, PRIMARY KEY (customer_id))")
        return True

    def createTables(self):
        with open('sql/create_tables.sql') as sql_file:
            sql = sql_file.read()
            for line in sql.split(';'):
                if not line.strip():
                    continue
                try:
                    self.execute(line)
                except Exception as e:
                    print(e)

    def login(self, username, password):
        self.cursor.cmd_change_user(
            username=username, password=password, database=self._database, charset=33)

    def createDB(self):
        db_name = self.readConfig('database')
        db_conn = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            port=self._port
        )
        db_conn.cursor().execute(
            f'CREATE SCHEMA IF NOT EXISTS {db_name} DEFAULT CHARACTER SET utf8 ;')
        return db_name
