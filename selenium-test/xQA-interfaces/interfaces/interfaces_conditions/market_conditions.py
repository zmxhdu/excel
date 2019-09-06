# coding = utf-8
import connect_to_oracle
import configparser
import json


class Market_Conditions(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.config')
        database = 'database_66'
        SQL = 'SQL'

        db = connect_to_oracle.DataBase(
            host=config.get(database, 'host'),
            port=config.get(database, 'port'),
            dbname=config.get(database, 'dbname'),
            username=config.get(database, 'username'),
            password=config.get(database, 'password')
        )

        self.db =db
        self.config = config
        self.SQL = SQL

    def get_sql(self, type):
        sql = self.config.get(self.SQL, type.upper()+'_SQL').replace('\n',' ')
        params = json.loads(self.config.get(self.SQL, type.upper()+'_PARAMS'))
        fields = self.config.get(self.SQL, type.upper()+'_FIELDS').replace(' ','').split(',')
        sql_result = self.db.sql(sql, params)

        resultList = []
        for result in sql_result:
            param = dict(zip(fields, list(result)))
            resultList.append(param)

        return resultList
