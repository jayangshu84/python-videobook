import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
print (data_2)
data_2.to_csv("output_73.txt", index=None)

