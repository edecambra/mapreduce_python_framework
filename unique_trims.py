import MapReduce
import sys

"""
This example takes DNA sequencer data and trims the trailing 10 
nucleotides and checks them for uniquness 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[:-10], 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
