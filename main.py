import mysql.connector



# import mysql.connector
#
# # TLS-enabled MySQL connection
# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="y123omg456",   # replace with your actual password
#     database="dummy",   # replace with your DB name
#     ssl_verify_cert=True ,       # enforce certificate validation
#     # Optional if you have certs:
#     ssl_ca="/path/to/ca-cert.pem",
# #     ssl_cert="/path/to/client-cert.pem",
# #     ssl_key="/path/to/client-key.pem"
# )
#
# cursor = conn.cursor()
# cursor.execute("SELECT VERSION();")
# print("Connected to MySQL Server version:", cursor.fetchone()[0])
#
# cursor.close()
# conn.close()

import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123omg456",
    database="dummy",


    # currently not required
    # ssl={
    #     "ca": "C:/Program Files/MySQL/MySQL Server 8.0/ssl/ca.pem",
    #     "cert": "C:/Program Files/MySQL/MySQL Server 8.0/ssl/client-cert.pem",
    #     "key": "C:/Program Files/MySQL/MySQL Server 8.0/ssl/client-key.pem"
    # }
)

cursor = conn.cursor()
cursor.execute("SELECT VERSION();")
print("Connected to MySQL Server version:", cursor.fetchone()[0])
cursor.execute("SELECT * FROM programmers")
print(cursor.fetchall())

cursor.close()
conn.close()
