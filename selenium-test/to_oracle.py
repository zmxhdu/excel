import cx_Oracle


class DataBase(object):
    def __init__(self, host, port, dbname, username, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.username = username
        self.password = password

    def sql(self, sql):
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
            result = cursor.execute(sql).fetchall()
            cursor.close()
            db.close()
            return result
        except cx_Oracle.Error as e:
            raise e


if __name__ == '__main__':
    db = DataBase(
        host='191.168.6.6',
        port='1521',
        dbname='xalms',
        username='xalms_trd',
        password='xpar'
    )
    sql = 'select * from TTRD_CASHLB'
    res = db.sql(sql)
    print(res)
