// test.mss – A simple test using hte lower corner of the Node Subsystem
diagram class
notation Starr
presentation diagnostic
orientation landscape
sheet tabloid
nodes
    // <node> <row>,<col>
    Sheet 1,1
    Canvas 3,1
    Diagram 3,3
    Annotation Layout 2,3
connectors
    // <side><connector name> : <side><lines> <face><anchor>|<node> : <side><lines> <face><anchor>|<node>
    -R14 : +1 r|Canvas   : -2  l|Diagram
    +R13 : -2 b|Canvas   : -2  t|Sheet
    +R16 : +2 b+2|Canvas : -2  l+2|Annotation Layout
