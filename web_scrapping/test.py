

data = "406 items found in Luggage Sets"

x = data.split(" ")

print()
y = (int(x[0])/40)
print(y)

if(type(y)==float):
    y=y+1
print(round(y))
