import random
nums = ["find",1,2,3,4,5,6,7,8,9]
def uprowleft():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def uprowcenter():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def uprowright():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def centerrowleft():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def centerrowcenter():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def centerrowright():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def downrowleft():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def downrowcenter():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def downrowright():
    datarow1 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow2 = (random.choice(nums),random.choice(nums),random.choice(nums))
    datarow3 = (random.choice(nums),random.choice(nums),random.choice(nums))
    wholedata = [datarow1,datarow2,datarow3]
    return wholedata
def sudokuresult():
    print("Up Block: \n")
    print("Upper Row: ",uprowleft())
    print("Center Row: ",uprowcenter())
    print("Lower Row: ",uprowright())
    print("\n")
    print("Center Block: \n")
    print("Upper Row: ",centerrowleft())
    print("Center Row: ",centerrowcenter())
    print("Lower Row: ",centerrowright())
    print("\n")
    print("Down Block: \n")
    print("Upper Row: ",downrowleft())
    print("Center Row: ",downrowcenter())
    print("Lower Row: ",downrowright())
    print("\n")
    print("3 ROW,1 COLUMN SUDOKU MADE SUCCESFULLY")
print(sudokuresult())
'''
This dosent really make a sudoku
because some numbers will repeat...
ill try to fix it soon. so yeah,enjoy
'''
