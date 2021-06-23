import mysql.connector

cnx = mysql.connector.connect(user='root', database='e_commerce')
cursor2 = cnx.cursor()
query2 = f"SELECT unique_id,product_id, product_name, prd_image FROM ecommerce where product_id='jwe1'"
cursor2.execute(query2)
for (unique_id, product_id, product_name, prd_image) in cursor2:
    prd_image = prd_image
    print(prd_image)