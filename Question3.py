#for immutaable
a=10
b=10
print(id(a))
print(id(b))
#output
#140721465349528
#140721465349528
#1)id functions returns the address of object were the value is store
#2)yes,the value returned by the id()function is same for two variable containing same values(applicable only for immuttable)

#for mutable
a=[10]
b=[10]
print(id(a))
print(id(b))
#output
#1807620880384
#1807620763520
#1)id functions returns the address of object were the value is store
#2)no,the value returned by the id()function is not same for two variable containing same values(applicable only for mutable)
