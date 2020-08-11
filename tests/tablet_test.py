"""
tablet_test.py - Verify that tablet works okay apart from the app
"""

from flatlanddb import FlatlandDB
from tablet import Tablet
from geometry_types import Rect_Size, Position

fdb = FlatlandDB()
t = Tablet(size=Rect_Size(height=8.5*72, width=11*72), output_file='tab_test.pdf',
           drawing_type='class diagram', presentation='default')
ink_area, leading = t.text_size(asset='class attributes', text_line='Altitude : MSL')
rsize = Rect_Size(height=ink_area.height+10, width=ink_area.width+10)
t.add_rectangle(asset='local compartment', lower_left=Position(100, 50), size=rsize)
t.add_text(asset='class attributes', text='Altitude : MSL', lower_left=Position(106, 50+leading))
t.render()
print(t)