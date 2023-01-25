import re
t = ['%s ilike %s', '%s ilike %s']
m = ['name', '%yael%', 'address', '%tel%']
sql = f"SELECT * FROM customer WHERE {' and '.join(t)};" % tuple(m)
print(sql)

print(re.match('[0-9]+$', '15342a'))