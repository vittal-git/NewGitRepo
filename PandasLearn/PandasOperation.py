from sqlalchemy import create_engine
import pandas as pd

oracle_connection = create_engine( "oracle+cx_oracle://sys:Admin@localhost:1521/orcl?mode=SYSDBA")
sql_query = """select *from emp"""
df = pd.read_sql(sql_query,oracle_connection)
print(df)
