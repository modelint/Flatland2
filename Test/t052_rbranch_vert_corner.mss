// t052_rbranch_vert_corner.mss – Vertical rut branch with a corner and two bends
diagram class
notation Starr
presentation diagnostic
orientation landscape
sheet letter
nodes
    // Node placement examples
    // Aircraft 3,2     :: Node named "Aircraft" positioned at row 3, column 2
    // node [wrap] row,col align [ right | left ] [top | bottom]
    Aircraft 3,2
    Helicopter 1,1
    Fixed Wing 1,3
    Hybrid Wing 4,5
connectors
    // Binary connector examples:
    // <side><connector name>[>bend] : <side><lines> <face><anchor>|<node> : <side><lines> <face><anchor>|<node>
    // Trunk connector examples:
    //
    //
    +R1 : b|Aircraft { t+1|Helicopter>>, t|Fixed Wing : L1R-2 } { l|Hybrid Wing : L3 }