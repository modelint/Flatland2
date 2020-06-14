"""
decorated_stem_end.py

Here all stem end decorations for supported notations appears.

Either end of a Stem (root or vine) may be decorated with one or more Symbols. A state
transition on a state machine diagram, for example, connects two state nodes. Each node
interface results in a Stem. In this example, only the Stem on the target state is decorated.
Here a solid arrow symbol is used to decorate the root end (where it attaches to the node).

Only those stem ends that are decorated are included here. In our example, the stem end
attached to the from state is just a line with no decoration on either the root or vine
ends and, therefore, has no decorated stem ends.
"""
from collections import namedtuple
from notation import StemSemantic, Notation
from connector_type import StemTypeName
from symbol import Symbol
from flatland_types import StemEnd
from diagram_type import DiagramTypeName
from layout_specification import undecorated_stem_clearance

DecoratedStemEndID = namedtuple('Decorated_Stem_End_ID', 'stem_type semantic dtype notation end')
DecoratedStemEndData = namedtuple('Decorated_Stem_End_Data', 'clearance symbols')
# symbols attribute is either a single symbol or a set of symbols
# a set indicates that there is a separate decoration on each end of the stem

decorated_stem_ends = {

    # xUML State Machine Diagram
    # 0 clearance for unary stems since we use the default_unary_branch_length instead
    DecoratedStemEndID(stem_type=StemTypeName.to_state, semantic=StemSemantic.Target_state,
                       dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=16, symbols={Symbol.Solid_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.to_init_state, semantic=StemSemantic.Initial_pstate,
                       dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=0, symbols={Symbol.Solid_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.to_init_state, semantic=StemSemantic.Initial_pstate,
                       dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.VINE
                       ): DecoratedStemEndData(clearance=0, symbols={Symbol.Solid_UML_dot}),

    DecoratedStemEndID(stem_type=StemTypeName.from_del_state, semantic=StemSemantic.Final_pstate,
                       dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.VINE
                       ): DecoratedStemEndData(clearance=0, symbols={Symbol.Bounded_UML_dot}),

    # xUML Class Diagram
    DecoratedStemEndID(stem_type=StemTypeName.gen_superclass, semantic=StemSemantic.Super_class,
                       dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=25, symbols={Symbol.Gen_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1,
                       dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=undecorated_stem_clearance, symbols={Symbol.UML_1}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1c,
                       dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=undecorated_stem_clearance, symbols={Symbol.UML_1c}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_M,
                       dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=undecorated_stem_clearance, symbols={Symbol.UML_M}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_Mc,
                       dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                       ): DecoratedStemEndData( clearance=undecorated_stem_clearance,symbols={Symbol.UML_Mc}),

    DecoratedStemEndID(stem_type=StemTypeName.assoc_class_mult, semantic=StemSemantic.Mult_M,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.VINE
                       ): DecoratedStemEndData( clearance=undecorated_stem_clearance, symbols={Symbol.UML_assoc_M}),

    # Starr Class Diagram
    DecoratedStemEndID(stem_type=StemTypeName.gen_superclass, semantic=StemSemantic.Super_class,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=25, symbols={Symbol.Gen_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=15, symbols={Symbol.Solid_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1c,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                       ):DecoratedStemEndData(clearance=15, symbols={Symbol.Hollow_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_M,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=24, symbols={Symbol.Double_solid_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_Mc,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=24, symbols={Symbol.Double_hollow_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.assoc_class_mult, semantic=StemSemantic.Mult_1,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.VINE
                       ): DecoratedStemEndData( clearance=15, symbols={Symbol.Solid_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.assoc_class_mult, semantic=StemSemantic.Mult_M,
                       dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.VINE
                       ): DecoratedStemEndData( clearance=24, symbols={Symbol.Double_solid_arrow}),

    # Shlaer-Mellor Class Diagram
    # Using the UML gen arrow for now, but model should be extended to accommodate the SM cross notation later
    DecoratedStemEndID(stem_type=StemTypeName.gen_superclass, semantic=StemSemantic.Super_class,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                       ): DecoratedStemEndData( clearance=25, symbols={Symbol.Gen_arrow, Symbol.SM_isa}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=15, symbols={Symbol.Open_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1c,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=15, symbols={Symbol.Open_arrow, Symbol.SM_cond}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_M,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=24, symbols={Symbol.Double_open_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_Mc,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                       ): DecoratedStemEndData(clearance=24, symbols={Symbol.Double_open_arrow, Symbol.SM_cond}),

    DecoratedStemEndID(stem_type=StemTypeName.assoc_class_mult, semantic=StemSemantic.Mult_1,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.VINE
                       ):DecoratedStemEndData(clearance=15, symbols={Symbol.Open_arrow}),

    DecoratedStemEndID(stem_type=StemTypeName.assoc_class_mult, semantic=StemSemantic.Mult_M,
                       dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.VINE
                       ): DecoratedStemEndData(clearance=24, symbols={Symbol.Double_open_arrow})
}
