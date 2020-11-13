// t052_rbranch_vert_corner.mss – Vertical rut branch with a corner and two bends
diagram class
notation Starr
presentation diagnostic
orientation landscape
sheet letter
nodes
    // node [wrap] row,col align [ right | left ] [top | bottom]
    Aircraft 3,2
    Helicopter 1,1
    Fixed Wing 1,3
    Hybrid Wing 4,5
connectors
    // <side><connector name>[>bend] : <side><lines> <face><anchor>|<node> : <side><lines> <face><anchor>|<node>
    -R1 : b|Aircraft [ t|Helicopter, t|Fixed Wing l|Hybrid Wing ] : L3,R+1
