"""
styledb_test.py – Ensure that we can build the drawing domain database
"""

from flatlanddb import FlatlandDB
from styledb import StyleDB

fdb = FlatlandDB()
sdb = StyleDB(drawing_type='Starr class diagram', presentation='diagnostic')
print("Finished")
