#given
a=10
b=10
print(id(a))
print(id(b))
#output
#140721592554904
#140721592554904
#here,to mange memory as both a and b contains same value integer and as we know integer is immutable so its id is same

a=[10]
b=[10]
print(id(a))
print(id(b))
#output
#1807620880384
#1807620763520
#basically, list are mutable so to make changes without affecting other as per future aspect they are store at different id's