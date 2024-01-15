print = "This is a string {}".format("INSERTED")  # This is a string INSERTED
print = "The {} {} {}".format("fox", "brown", "quick")  # The fox brown quick
print = "The {2} {1} {0}".format("fox", "brown", "quick")  # The quick brown fox
print = "The {0} {0} {0}".format("fox", "brown", "quick")  # The fox fox fox
print = "The {q} {b} {f}".format(f="fox", b="brown", q="quick")  # The quick brown fox
print = "The {f} {f} {f}".format(f="fox", b="brown", q="quick")  # The fox fox fox

result = 100 / 777
print = "The result was {r}".format(r=result)  # The result was 0.1287001287001287
print = "The result was {r:1.3f}".format(r=result)  # The result was 0.129
print = "The result was {r:10.3f}".format(r=result)  # The result was      0.129
print = "The result was {r:10.5f}".format(r=result)  # The result was    0.12870
print = "The result was {r:1.5f}".format(r=result)  # The result was 0.12870
print = "The result was {r:1.2f}".format(r=result)  # The result was 0.13
print = "The result was {r:1.0f}".format(r=result)  # The result was 0

name = "Jose"
print = (f"Hello, his name is {name}")
# Hello, his name is Jose. This is called an f-string.
# It is a new way to format strings introduced in Python 3.6.
# It is a much more readable way to do string formatting.

name = "Sam"
age = 3
print = (f"{name} is {age} years old.")
# Sam is 3 years old.
