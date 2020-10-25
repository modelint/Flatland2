// t001_straight_binary_horiz.mss – Two nodes and a single horizontal binary connector
diagram class
notation Starr
presentation diagnostic
orientation landscape
sheet letter
nodes
    // node [wrap] row,col align [ right | left ] [top | bottom]
    Aircraft 3,1
    Pilot 1,1
connectors
    // <side><connector name>[>bend] : <side><lines> <face><anchor>|<node> : <side><lines> <face><anchor>|<node>
    -R1   : +/1 b|Aircraft  : +/2  t|Pilot