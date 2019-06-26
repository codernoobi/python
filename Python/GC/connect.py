import os

from flask import Flask
import pymysql

db_user = os.environ.get('id0461')  #cloud_sql_username
db_password = os.environ.get('tiger')  #CLOUD_SQL_PASSWORD
db_name = os.environ.get('encyclopedia')    #CLOUD_SQL_DATABASE_NAME
db_connection_name = os.environ.get('cosmic-attic-222006:asia-south1:id0461')    #CLOUD_SQL_CONNECTION_NAME
                                #to find connection name in cloud console :gcloud sql instances describe YOUR-INSTANCE-ID
app = Flask(__name__)


@app.route('/')
def main():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`
    if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        # If running locally, use the TCP connections instead
        # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
        # so that your application can use 127.0.0.1:3306 to connect to your
        # Cloud SQL instance
        host = '127.0.0.1'
        cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)

    with cnx.cursor() as cursor:
        cursor.execute('SELECT NOW() as now;')
        result = cursor.fetchall()
        current_time = result[0][0]
    #cnx.close()

    return str(current_time)