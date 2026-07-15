P=int(input("Enter Principle:"))
R=int(input("Enter Rate:"))
T=int(input("Enter Time:"))
Amount=P*(1+R/100)**T
CI=Amount-P
print("Compound Interest=",CI)
print("Total Amount=",Amount)
