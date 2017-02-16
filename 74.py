import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
data3 = pandas.concat([data1, data2])
data3.to_csv("output_74.txt", index=None)




