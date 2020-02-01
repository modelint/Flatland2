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
from notation import ConnectorSemantic, Notation
from connector_type import StemTypeName
from symbol import Symbol
from flatland_types import StemEnd
from diagram_node_types import DiagramTypeName

DecoratedStemEnd = namedtuple('Decorated_Stem_End', 'stem_type semantic dtype notation end')

decorated_stem_ends = {

    # xUML State Machine Diagram
    DecoratedStemEnd(stem_type=StemTypeName.to_state, semantic=ConnectorSemantic.Target_state,
                     dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.Solid_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.to_init_state, semantic=ConnectorSemantic.Initial_state,
                     dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.Solid_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.to_init_state, semantic=ConnectorSemantic.Initial_state,
                     dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.VINE
                     ): {Symbol.Solid_UML_dot},

    DecoratedStemEnd(stem_type=StemTypeName.from_del_state, semantic=ConnectorSemantic.Final_state,
                     dtype=DiagramTypeName.SMD, notation=Notation.xUML, end=StemEnd.VINE
                     ): {Symbol.Bounded_UML_dot},

    # xUML Class Diagram
    DecoratedStemEnd(stem_type=StemTypeName.gen_subclass, semantic=ConnectorSemantic.Gen,
                     dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.Gen_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_1,
                     dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.UML_1},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_1c,
                     dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.UML_1c},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_M,
                     dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.UML_M},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_Mc,
                     dtype=DiagramTypeName.CD, notation=Notation.xUML, end=StemEnd.ROOT
                     ): {Symbol.UML_Mc},

    DecoratedStemEnd(stem_type=StemTypeName.assoc_class_mult, semantic=ConnectorSemantic.Mult_M,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.VINE
                     ): {Symbol.UML_assoc_M},

    # Starr Class Diagram
    DecoratedStemEnd(stem_type=StemTypeName.gen_subclass, semantic=ConnectorSemantic.Gen,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                     ): {Symbol.Gen_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_1,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                     ): {Symbol.Solid_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_1c,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                     ): {Symbol.Hollow_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_M,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                     ): {Symbol.Double_solid_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_Mc,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.ROOT
                     ): {Symbol.Double_hollow_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.assoc_class_mult, semantic=ConnectorSemantic.Mult_1,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.VINE
                     ): {Symbol.Solid_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.assoc_class_mult, semantic=ConnectorSemantic.Mult_M,
                     dtype=DiagramTypeName.CD, notation=Notation.Starr, end=StemEnd.VINE
                     ): {Symbol.Double_solid_arrow},

    # Shlaer-Mellor Class Diagram
    DecoratedStemEnd(stem_type=StemTypeName.gen_subclass, semantic=ConnectorSemantic.Gen,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                     ): {Symbol.Gen_arrow, Symbol.SM_isa},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_1,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                     ): {Symbol.Open_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_1c,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                     ): {Symbol.Open_arrow, Symbol.SM_cond},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_M,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                     ): {Symbol.Double_open_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.class_mult, semantic=ConnectorSemantic.Mult_Mc,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.ROOT
                     ): {Symbol.Double_open_arrow, Symbol.SM_cond},

    DecoratedStemEnd(stem_type=StemTypeName.assoc_class_mult, semantic=ConnectorSemantic.Mult_1,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.VINE
                     ): {Symbol.Open_arrow},

    DecoratedStemEnd(stem_type=StemTypeName.assoc_class_mult, semantic=ConnectorSemantic.Mult_M,
                     dtype=DiagramTypeName.CD, notation=Notation.SM, end=StemEnd.VINE
                     ): {Symbol.Double_open_arrow}
}