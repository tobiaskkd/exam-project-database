import mysql.connector
import yaml


class DBConnection():

    def __init__(self):
        self._host = self.readConfig('host')
        self._user = self.readConfig('user')
        self._password = self.readConfig('password')
        self._port = self.readConfig('port')
        db_name = self.readConfig('database')
        self._database = self.createDB(db_name)
        self._db_conn = self.connectDB(db_name)
        self._cursor = self._db_conn.cursor(buffered=True)
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

    @property
    def database(self):
        return self._database

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
        try:
            self.cursor.execute(sql, params or (), multi=multi)
        except Exception as e:
            print(e)

    def query(self, sql, params=None, multi=False):
        try:
            self.cursor.execute(sql, params or (), multi=multi)
            self.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

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
        self.connection.cmd_change_user(
            username=username, password=password, database=self._database, charset=33)

    def connectDB(self, database=None):
        return mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=database,
            port=self._port,
            auth_plugin='mysql_native_password'
        )

    def createDB(self, db_name='newDB'):
        db_conn = self.connectDB()
        db_conn.cursor().execute(
            f'CREATE SCHEMA IF NOT EXISTS {db_name} DEFAULT CHARACTER SET utf8 ;')
        db_conn.close()
        return db_name
