import MapReduce
import sys

"""
Friend Count using simple simulated social network data
represented as person,friend tuples

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person identifier
    # value: friend identifier
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, 1)

def reducer(key, friend_counts):
    # key: word
    # value: list of occurrence counts
    total = 0
    for f in friend_counts:
      total += f
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
