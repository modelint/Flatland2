// test.mss – A simple test using hte lower corner of the Node Subsystem
diagram class
notation Starr
presentation diagnostic
orientation landscape
sheet tabloid
nodes
    // node [wrap] row,col align [ right | left ] [top | bottom]
    Sheet 1,1
    Canvas 3,1
    Diagram 3,3
    Annotation Layout/2 2,3 >right
connectors
    // <side><connector name>[>bend] : <side><lines> <face><anchor>|<node> : <side><lines> <face><anchor>|<node>
    -R14   : +/1 r0|Canvas   : -/3  l|Diagram
    +R13   : -/2 b|Canvas   : -/2  t|Sheet
    -R16>2 : +/2 b+2|Canvas : -/2  l+2|Annotation Layout
