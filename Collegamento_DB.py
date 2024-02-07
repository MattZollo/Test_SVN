import pyodbc
import pandas as pd

import sqlalchemy
import pymysql
import numpy as np

from sqlalchemy import create_engine



connector = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=;Database=;Trusted_Connection=yes;")

cursor = connector.cursor()

DIGITAML_STAGING = pd.read_sql("SELECT * FROM dbo.DIGITAML_STAGING_3 where cd_ind_analitico like 'IDIA%'",connector)

DIGITAML_STAGING.head()