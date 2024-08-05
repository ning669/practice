#test
print ("hello world!")
#test on webx = [...] ## replace this with your object
try:
    result = x.index("c")
except AttributeError:
    if isinstance(x, list):
        result = "The list does not contain the element 'c'."
    else:
     result = (f"The {type(x).__name__} object does not have the .index() method.")

except ValueError:
    if isinstance(x, list):
        result = "The list does not contain the element 'c'."
    else:
        result = f"The {type(x).__name__} object does not have the .index() method."

print(result)
