import MapReduce
import sys

"""
Inverted Index, which takes documents, processes words, 
and returns a dictionary of words and 
which document they are listed in.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    doc_list = []
    for v in list_of_values:
        if v not in doc_list:
            doc_list.append(v)
    mr.emit((key, doc_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
