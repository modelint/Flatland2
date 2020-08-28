"""
tablet_test.py - Verify that tablet works okay apart from the app
"""

from flatlanddb import FlatlandDB
from tablet import Tablet
from geometry_types import Rect_Size, Position

fdb = FlatlandDB()

t = Tablet(size=Rect_Size(height=8.5*72, width=11*72), output_file='tab_test.pdf',
           drawing_type='Starr class diagram', presentation='diagnostic')
ink_area, leading = t.text_size(asset='attributes', text_line='Altitude : MSL')
rsize = Rect_Size(height=ink_area.height+10, width=ink_area.width+10)
t.add_rectangle(asset='class compartment', lower_left=Position(100, 50), size=rsize)
t.add_text(asset='attributes', text='Altitude : MSL', lower_left=Position(106, 50+leading))
arrow_points = [Position(200,203.5), Position(209,200), Position(200,196.5)]
t.add_polygon(asset='solid arrow', vertices=arrow_points)
bend_points = [Position(200, 300), Position(300, 300), Position(300, 400)]
t.add_open_polygon(asset='binary connector', vertices=bend_points)
t.render()
print(t)