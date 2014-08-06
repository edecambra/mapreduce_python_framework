import MapReduce
import sys

"""
This MapReduce script is to perform matrix multiplication
with a database matrix in sparse matrix notation:
[matrix, i, j, value]

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mat = record[0]
    val = record[3]
    i = record[1]
    j = record[2]
    for k in range(5): # loops over all rows and columns, change this for larger matricies, 
        if mat == "a":  
            mr.emit_intermediate((i,k), record)
        if mat == "b":
            mr.emit_intermediate((k,j), record)                      

def reducer(id, contents):
    a = {}  #initialize dictionary for calculations
    b = {}  #these store the matches for multiplication
    total = 0
    for cell in contents:
        if cell[0] == "a":
            a[cell[2]] = cell[3]
        if cell[0] == "b":
            b[cell[1]] = cell[3]
    for j in range(5):
        total = total + (a.get(j,0)*b.get(j,0))
    mr.emit((id[0],id[1],total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

