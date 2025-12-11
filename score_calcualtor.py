"""
Calculate a given score and avergaes it to a percentage. 
"""

score = int(input("Score: "))
Out_of = int(input("out of: "))

x = (score / Out_of) * 100

print(f"{round(x, 2)}%")