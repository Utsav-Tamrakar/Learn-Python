address={
  "Utsav":"Chainpur",
  "Rinki":"Denmark",
  "Sabu":"Japan",
  "Sonam":"Japan"
}
print(type(address))
print(address["Rinki"])

is_married = False
print(is_married)


d={110:"abc",101:"xyz",105:"pqr"}
print(d)
d={} #empty the dictionary
d["Laptop"]=40000
d["Mobile"]=15000
d["Earphone"]=1500
print(d)
print(d["Mobile"])


d={110:"abc",101:"xyz",105:"pqr"}
print(d.get(101))
print(d.get(125))
print(d.get(125,"NA"))
if 125 in d:
  print(d[125])
else:
  print("NA")


d={110:"abc",101:"xyz",105:"pqr",106:"bcd"}
d[101]="wxy"
print(len(d))
print(d)
print(d.pop(105))
print(d)
del d[106]
print(d)
d[108]="cde"
print(d.popitem())
