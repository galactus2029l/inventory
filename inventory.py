import sqlite3

# 1. Conexión a la base de datos real
sqliteConnection = sqlite3.connect('sqlite/inventory.db')


# 2. Consulta para obtener las tablas
sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""

# 3. Crear cursor
cursor = sqliteConnection.cursor()

# 4. Ejecutar la consulta para obtener las tablas
cursor.execute(sql_query)

# 5. Imprimir la lista de tablas
print("Tablas en la base de datos:")
print(cursor.fetchall())


# 6. Consulta para obtener los datos de la tabla inventory_type
cursor.execute("SELECT * FROM inventory_type")

# 7. Imprimir contenido de la tabla
print("\nContenido de 'inventory_type':")
for row in cursor.fetchall():
    print(row)

# 8. Cierre de cursor y conexión
cursor.close()
sqliteConnection.close()
