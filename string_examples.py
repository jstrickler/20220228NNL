s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string

print(len(s1), len(s2), len(s5))
print(s1)
print(s2)
print("Guido's the former BDFL of Python")
print('Guido is the former "BDFL" of Python')
print("""Guido's the former "BDFL" of Python""")

customer_query = """
select customer_last_name
from customers
where state = "NV"
order by "customer_last_name"
"""

print(customer_query)
print(repr(customer_query))

x = 5
print(repr(x))









