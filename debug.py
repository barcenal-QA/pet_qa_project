data1 =['angular', 'commands', 'downloads', 'excel file.doc', 'veu', 'word file.doc']
data2 = ['angular', 'commands', 'downloads', 'excelfile', 'veu', 'wordfile']

data1 = [item.replace(' ','').replace('.doc','')
         for item in data1]
print(data1)
print(data2)

assert data1 == data2