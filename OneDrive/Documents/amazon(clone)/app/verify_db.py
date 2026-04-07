import sqlite3

print('='*60)
print('Local Marts Database Verification')
print('='*60)
conn = sqlite3.connect('amazon_clone.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]
print('Tables:', tables)
print()

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f'  {table}: {count} rows')

print()
cursor.execute('SELECT COUNT(*) FROM "user" WHERE role=\"admin\"')
admin_count = cursor.fetchone()
print(f'Admin Users: {admin_count[0] if admin_count else 0}')

conn.close()

print()
print('='*60)
print('Sri Vasavi Database Verification')
print('='*60)
conn = sqlite3.connect('C:/Users/DELL/OneDrive/Documents/sri-vasavi-computers/app/sri_vasavi.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]
print('Tables:', tables)
print()

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f'  {table}: {count} rows')

conn.close()
