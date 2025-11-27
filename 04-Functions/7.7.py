def binary_number(n):
    for digit in n:
        if digit!='1' and digit!='0':return False
    return True
print(f"f(1011001) returns {binary_number('1011001')}")
print(f"f(1231232110aa) returns {binary_number('1231232110aa')}")