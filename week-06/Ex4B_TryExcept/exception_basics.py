# Israel Colman
# 11/19/2026

# Value Error
try: 
    num = int('fifty')
except ValueError:
    print('ValueError: Value must be an integer')
else: 
    print(num)
finally: 
    print("Let's try another one...")


# NameError
try:
    fav_movie = Interstellar 
except NameError:
    print("NameError: Variable does not exist.")
else:
    print(fav_movie)
finally:
    print("Let's try another one...")



# TypeError
try:
    result = 5 + "10"
except TypeError:
    print("TypeError: Cannot add a number and text together.")
else:
    print(result)
finally:
    print("Let's try another one...")


#SyntaxError
try:
    exec("if True print('Hello')")
except SyntaxError:
    print("SyntaxError: Invalid Python syntax.")
else:
    print("No syntax error.")
finally:
    print("Let's try another one...")