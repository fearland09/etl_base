from datetime import date
import time
from sqlalchemy import create_engine
import pandas as pd
import pymysql

#Se realiza la conexión a la base de datos que contiene la información extraída
connection = pymysql.connect(host='mysql',
                             user='root',
                             password='admin',
                             database='Financiera',
                            )

#Se define el query a la tabla que cuenta con los datos de entrada en tabla datos de la BD Financiera
query='select * from datos'

"Extraccion"
#Se extrae la información del query al dataframe para leer la información
df=pd.read_sql_query(query,connection)

"Trasformación"
#Se asigna el nombre con el que quedara las columnas de la tabla destino
df = df.rename(columns={'id':'id_trasaccion','name':'nombre_negocio','company_id':'id_negocio','monto':'amount','status':'estatus_pago','created_at':'fecha_creacion','paid_at':'fecha_pago'})

#Se asigna el tipo de dato fecha a los campos fecha_pago y fecha_creacion antes paid_at y created_at 
df['fecha_pago']=pd.to_datetime(df['fecha_pago'],format='ISO8601')
df['fecha_creacion']=pd.to_datetime(df['fecha_creacion'],format='ISO8601')


#Se elimina la Tabla resultado si es que existe para insertar la nueva data 
query='DROP TABLE IF EXISTS DWH.resultado;'
cur=connection.cursor()
cur.execute(query)
connection.close()

#Se hace una pausa para ver el borrado de la tabla
time.sleep(10)

"Carga"
#Se configura la cadena de conexión a la base de datos destino DWH
cadena_conexion= 'mysql+pymysql://root:admin@mysql:3306/DWH'

#Se realiza la conexion a la base de datos destino DWH
conexion=create_engine(cadena_conexion)

#Se realiza la inserción de datos desde el dataframe que fue procesado
df.to_sql(name='resultado', con=conexion)
