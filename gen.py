tables=[]
col=[]
tables=input("Enter table names").split(',')
for i in tables:
    print('Enter columns of',i)
    col.append(input().split(','))
print()
for i in range(len(tables)):
    print('CREATE TABLE',tables[i],'(\n',',\n'.join(col[i]),');\n\n')
for i in range(len(tables)):
    cols=[]
    for j in col[i]:
        cols.append(j.split(' ')[0])
    print('Enter table=',tables[i],'columns=',','.join(cols))
    print('INSERT INTO',tables[i],'(',','.join(cols),') VALUES (',input(),');')
