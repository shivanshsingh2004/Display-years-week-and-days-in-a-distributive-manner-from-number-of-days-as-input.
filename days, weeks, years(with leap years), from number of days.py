y=int (input("no. of days"))

#no. of days in weeks

#0.25 for every four years there is a leap year

x = int((y // (365.25)))

if x < 4:
    a = x
    b = int(y // 7)
    c = int(y % 7)

elif x >= 4:
    a = x
    b = int(((y % 365.25 ) // 7))
    c = int((y % 365.25) % 7)

else:
    a = int((y // (365)))
    b = int(((a) // 7))
    c = int((y % 365) % 7)

print("number of years=", a, ": numbers of weeks=", b, "number of days=", c, "code by the_cahintosh")
