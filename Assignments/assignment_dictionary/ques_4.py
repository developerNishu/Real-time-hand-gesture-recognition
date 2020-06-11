# Python script to concatenate following dictionaries to create a new one

#sample
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic_new = {}

for d in (dic1, dic2, dic3): dic_new.update(d)
print(dic_new)