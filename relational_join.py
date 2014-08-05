import MapReduce
import sys

"""
MapReduce script to preform a relational join as if in
an SQL database, with the following query:
SELECT *
FROM Orders, LineItem
WHERE Order.order_id = LineItem.order_id

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # order_id = individual order number to join on
    # contents = all table data
    order_id = record[1]
    contents = record
    mr.emit_intermediate(order_id, contents)

def reducer(order_id, contents):
    # order_id = individual order number to join on
    # contents = all table data
    for row in contents[1:]:
        join_rec = []
        for item in contents[0]:
            join_rec.append(item)
        for item in row:
            join_rec.append(item)
        mr.emit(join_rec)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
