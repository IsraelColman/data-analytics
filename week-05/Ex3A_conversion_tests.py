# Description: this script tests various numeric
#              conversion techniques
# Authour: Israel Colman


# Step 1
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Step 3
a_float = float(a)
b_int = int(b)
c_str = str(c)
d_str = str(d)

# Step 4 (printing)
print(a_float, type(a_float))
print(b_int, type(b_int))
print(c_str, type(c_str))
print(d_str, type(d_str))

# Step 5 a)
# a_int = int(a) I get a value error

# Step 5 b)
# b_float = float(b) I get a value error

# Step 5 c)
a_int_float = int(float(a))
print(a_int_float)

# Step 5 d)
c_slice = int(c [0:3])
print(c_slice, type(c_slice))

# Step 5 e)
print(c.strip())
print(d.strip())