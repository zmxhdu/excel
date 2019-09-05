# coding = utf-8
import cx_Oracle


class DataBase(object):
    def __init__(self, host, port, dbname, username, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.username = username
        self.password = password

    def sql(self, sql, sql_params=''):
        try:
            dsn = cx_Oracle.makedsn(
                host=self.host,
                port=self.port,
                sid=self.dbname
            )

            db = cx_Oracle.connect(
                user=self.username,
                password=self.password,
                dsn=dsn,
                encoding='UTF-8'
            )
            cursor = db.cursor()
            result = cursor.execute(sql, sql_params).fetchall()
            cursor.close()
            db.close()
            return result
        except cx_Oracle.Error as e:
            raise e
