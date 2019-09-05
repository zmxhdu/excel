# coding = utf-8
import connect_to_oracle
import configparser


TIDX_SQL = 'select I_CODE,A_TYPE,M_TYPE from TIDX order by I_CODE'
TFND_SQL = 'select I_CODE,A_TYPE,M_TYPE from TFND order by I_CODE'
STOCK_SQL = 'select I_CODE,A_TYPE,M_TYPE from TSTK order by I_CODE'
TBND_SQL = 'select I_CODE,A_TYPE,M_TYPE from TBND order by I_CODE'
CASHLB_SQL = 'select I_CODE,A_TYPE,M_TYPE from TTRD_CASHLB order by I_CODE'
PAYMENT_SQL = 'select I_CODE,A_TYPE,M_TYPE from TBND order by I_CODE ' \
              'union all ' \
              'select I_CODE,A_TYPE,M_TYPE from TTRD_CASHLB order by I_CODE'
BONDFUTUER_SQL = 'select I_CODE,A_TYPE,M_TYPE from TBNDFUTURE order by I_CODE'
STOCKIDXFUTUER_SQL = 'select I_CODE,A_TYPE,M_TYPE from TSTK_IDX_FUTURE order by I_CODE'
CVTBOND_SQL = 'select I_CODE,A_TYPE,M_TYPE from TBND where A_TYPE=:A_TYPE order by I_CODE'
CVTBOND_PARAMS = {'A_TYPE':'SPT_CB'}
STOCKOPTION_SQL = 'select I_CODE,A_TYPE,M_TYPE from TEQOPTION order by I_CODE'
TIRSWAP_SQL = 'select I_CODE,A_TYPE,M_TYPE from TEQOPTION order by I_CODE'

config = configparser.ConfigParser()
config.read('config.config')
database = 'database_66'

db = connect_to_oracle.DataBase(
        host=config.get(database, 'host'),
        port=config.get(database, 'port'),
        dbname=config.get(database, 'dbname'),
        username=config.get(database, 'username'),
        password=config.get(database, 'password')
    )
res = db.sql(TIDX_SQL)
print(res)
