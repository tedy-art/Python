total = 100
country = "US"
#country = "AU"

if country == "US":
    if total <= 50:
        print("shipping cost is $50.")

elif total <=100:
    print("shipping cost is $25.")
else:
    print("FREE")

if country == "AU":
    if total <= 50:
        print("shipping cost is $100.")
else:
    print("FREE")
