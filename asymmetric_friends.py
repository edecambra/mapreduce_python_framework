import MapReduce
import sys

"""
Looks for asymmetric friend relationships, 
groups by sorted friend list and produces output list of relations
reduces by counting double relationships and omitting
then printing the asym relationship, symetrically

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # person: person identifier
    # friend: friend identifier
    record = sorted(record)
    mr.emit_intermediate(record[0], record[1])

def reducer(p, f):
    f_count = {}
    for friend in f:   
        f_count[friend] = f_count.get(friend, 0) + 1
    for k,v in f_count.items():
        if v == 1:
            mr.emit((p, k))
            mr.emit((k, p))
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
