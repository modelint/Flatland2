"""
relvars.py – Relation variables (relvars / tables) in the flatland database
"""
from sqlalchemy import Table, Column, String, Integer, Boolean, Enum
from sqlalchemy import ForeignKey, UniqueConstraint, PrimaryKeyConstraint, ForeignKeyConstraint, CheckConstraint


def define(db):
    return {
        # Flatland diagram domain
        'sheet': Table('Sheet', db.MetaData,
                       Column('Name', String(20), nullable=False, primary_key=True),
                       # US or International names and units
                       Column('Group', Enum('us', 'int', name='enum_Group'), nullable=False),
                       # Based on landscape, so Width should be >= Height
                       # Sizes as string since all metric units are integer and some US values are
                       # half sizes such as 8.5".  Converted to numeric on load from DB
                       Column('Height', String(8), nullable=False),
                       Column('Width', String(8), nullable=False)
                       ),
        'diagram_layout_specification': Table('Diagram Layout Specification', db.MetaData,
                                              Column('Name', String(20), nullable=False, primary_key=True),
                                              Column('Default margin top', Integer, nullable=False),
                                              Column('Default margin bottom', Integer, nullable=False),
                                              Column('Default margin left', Integer, nullable=False),
                                              Column('Default margin right', Integer, nullable=False),
                                              Column('Default diagram origin x', Integer, nullable=False),
                                              Column('Default diagram origin y', Integer, nullable=False),
                                              Column('Default cell padding top', Integer, nullable=False),
                                              Column('Default cell padding bottom', Integer, nullable=False),
                                              Column('Default cell padding left', Integer, nullable=False),
                                              Column('Default cell padding right', Integer, nullable=False),
                                              Column('Default cell alignment vertical',
                                                     Enum('bottom', 'center', 'top', name='enum_Valign'),
                                                     nullable=False),
                                              Column('Default cell alignment horizontal',
                                                     Enum('left', 'center', 'right', name='enum_Halign'),
                                                     nullable=False),
                                              ),
        'connector_layout_specification': Table('Connector Layout Specification', db.MetaData,
                                                Column('Name', String(20), nullable=False, primary_key=True),
                                                Column('Default stem positions', Integer,
                                                       CheckConstraint('"Default stem positions" > 0' and
                                                                       '"Default stem positions" % 2 != 0',
                                                                       name='Stem_positions_odd'),
                                                       nullable=False),
                                                Column('Default rut positions', Integer,
                                                       CheckConstraint('"Default rut positions" > 0' and
                                                                       '"Default rut positions" % 2 != 0',
                                                                       name='Rut_positions_odd'),
                                                       nullable=False),
                                                Column('Runaround lane width', Integer, nullable=False),
                                                ),
        'notation': Table('Notation', db.MetaData,
                          Column('Name', String, nullable=False, primary_key=True),
                          Column('About', String, nullable=False),
                          Column('Why use it', String, nullable=False)
                          ),
        'diagram_type': Table('Diagram Type', db.MetaData,
                              Column('Name', String, nullable=False, primary_key=True),
                              Column('About', String, nullable=False)
                              ),
        'diagram_notation': Table('Diagram Notation', db.MetaData,
                                  Column('Diagram type', String,
                                         ForeignKey('Diagram Type.Name', name='R32_diagram_type'), nullable=False),
                                  Column('Notation', String,
                                         ForeignKey('Notation.Name', name='R32_notation'), nullable=False),
                                  PrimaryKeyConstraint('Diagram type', 'Notation', name='I1')
                                  ),
        'node_type': Table('Node Type', db.MetaData,
                           Column('Name', String, nullable=False),
                           Column('Diagram type', String, ForeignKey('Diagram Type.Name', name='R15'), nullable=False),
                           Column('About', String, nullable=False),
                           Column('Corner rounding', Integer, nullable=False),
                           Column('Border', String, nullable=False),
                           Column('Default height', Integer, nullable=False),
                           Column('Default width', Integer, nullable=False),
                           Column('Max height', Integer, nullable=False),
                           Column('Max width', Integer, nullable=False),
                           PrimaryKeyConstraint('Name', 'Diagram type', name='I1')
                           ),
        'compartment_type': Table('Compartment Type', db.MetaData,
                                  Column('Name', String, nullable=False),
                                  Column('Vertical alignment', String(10), nullable=False),
                                  Column('Horizontal alignment', String(10), nullable=False),
                                  Column('Pad top', Integer, nullable=False),
                                  Column('Pad bottom', Integer, nullable=False),
                                  Column('Pad left', Integer, nullable=False),
                                  Column('Pad right', Integer, nullable=False),
                                  Column('Text style', String(15), nullable=False),
                                  Column('Node type', String, ForeignKey('Node Type.Name', name='R4'), nullable=False),
                                  Column('Diagram type', String, ForeignKey('Node Type.Diagram type', name='R4_2'),
                                         nullable=False),
                                  Column('Stack order', Integer, nullable=False),
                                  PrimaryKeyConstraint('Stack order', 'Node type', 'Diagram type', name='I1'),
                                  UniqueConstraint('Name', 'Node type', 'Diagram type', name='I2')
                                  ),
        'connector_type': Table('Connector Type', db.MetaData,
                                Column('Name', String, nullable=False),
                                Column('About', String, nullable=False),
                                Column('Geometry', String, nullable=False),
                                Column('Diagram type', String, ForeignKey('Diagram Type.Name', name='R50'),
                                       nullable=False),
                                PrimaryKeyConstraint('Name', 'Diagram type', name='I1')
                                ),
        'connector_style': Table('Connector Style', db.MetaData,
                                 Column('Connector type', String, nullable=False),
                                 Column('Diagram type', String, nullable=False),
                                 Column('Notation', String, nullable=False),
                                 Column('Stroke', String, nullable=False),
                                 PrimaryKeyConstraint('Connector type', 'Diagram type', 'Notation', name='I1'),
                                 ForeignKeyConstraint(('Connector type', 'Diagram type'),
                                                      ['Connector Type.Name', 'Connector Type.Diagram type'],
                                                      name='R60_connector_type'),
                                 ForeignKeyConstraint(('Notation', 'Diagram type'),
                                                      ['Diagram Notation.Notation', 'Diagram Notation.Diagram type'],
                                                      name='R60_diagram_notation')
                                 ),
        'stem_type': Table('Stem Type', db.MetaData,
                           Column('Name', String, nullable=False),
                           Column('About', String, nullable=False),
                           Column('Diagram type', String, nullable=False),
                           Column('Connector type', String, nullable=False),
                           Column('Length', Integer, nullable=False),
                           PrimaryKeyConstraint('Name', 'Diagram type', name='I1'),
                           ForeignKeyConstraint(('Connector type', 'Diagram type'),
                                                ['Connector Type.Name', 'Connector Type.Diagram type'], name='R59')
                           ),
        'stem_semantic': Table('Stem Semantic', db.MetaData,
                               Column('Name', String, nullable=False),
                               Column('Diagram type', String, ForeignKey('Diagram Type.Name', name='R57'),
                                      nullable=False),
                               PrimaryKeyConstraint('Name', 'Diagram type', name='I1')
                               ),
        'stem_signification': Table('Stem Signification', db.MetaData,
                                    Column('Stem type', String, nullable=False),
                                    Column('Semantic', String, nullable=False),
                                    Column('Diagram type', String, nullable=False),
                                    PrimaryKeyConstraint('Stem type', 'Semantic', 'Diagram type', name='I1'),
                                    ForeignKeyConstraint(('Semantic', 'Diagram type'), ['Stem Semantic.Name',
                                                                                        'Stem Semantic.Diagram type'],
                                                         name='R62_stem_semantic'),
                                    ForeignKeyConstraint(('Stem type', 'Diagram type'), ['Stem Type.Name',
                                                                                         'Stem Type.Diagram type'],
                                                         name='R62_stem_type')
                                    ),
        'stem_end_decoration': Table('Stem End Decoration', db.MetaData,
                                     Column('Stem type', String, nullable=False),
                                     Column('Semantic', String, nullable=False),
                                     Column('Diagram type', String, nullable=False),
                                     Column('Notation', String, nullable=False),
                                     Column('Symbol', String, ForeignKey('Symbol.Name', name='R58_symbol'),
                                            nullable=False),
                                     Column('End', Enum('root', 'vine', name='enum_End'), nullable=False),
                                     PrimaryKeyConstraint('Stem type', 'Semantic', 'Diagram type', 'Notation', 'Symbol',
                                                          'End', name='I1'),
                                     ForeignKeyConstraint(('Stem type', 'Semantic', 'Diagram type', 'Notation'),
                                                          ['Decorated Stem.Stem type', 'Decorated Stem.Semantic',
                                                           'Decorated Stem.Diagram type', 'Decorated Stem.Notation'],
                                                          name='R58_decorated_stem')
                                     ),
        'decorated_stem': Table('Decorated Stem', db.MetaData,
                                Column('Stem type', String, nullable=False),
                                Column('Semantic', String, nullable=False),
                                Column('Diagram type', String, nullable=False),
                                Column('Notation', String, nullable=False),
                                Column('Stroke', String, nullable=False),
                                PrimaryKeyConstraint('Stem type', 'Semantic', 'Diagram type', 'Notation', name='I1'),
                                ForeignKeyConstraint(('Stem type', 'Semantic', 'Diagram type'),
                                                     ['Stem Signification.Stem type', 'Stem Signification.Semantic',
                                                      'Stem Signification.Diagram type'], name='R55_stem_sig'),
                                ForeignKeyConstraint(('Diagram type', 'Notation'),
                                                     ['Diagram Notation.Diagram type', 'Diagram Notation.Notation'],
                                                     name='R55_diagram_notation')
                                ),
        'annotation': Table('Annotation', db.MetaData,
                            Column('Stem type', String, nullable=False),
                            Column('Semantic', String, nullable=False),
                            Column('Diagram type', String, nullable=False),
                            Column('Notation', String, nullable=False),
                            Column('Label', String, ForeignKey('Label.Name', name='R54_label'), nullable=False),
                            Column('Default stem side', String(1), nullable=False),
                            Column('Vertical stem offset', Integer, nullable=False),
                            Column('Horizontal stem offset', Integer, nullable=False),
                            PrimaryKeyConstraint('Stem type', 'Semantic', 'Diagram type', 'Notation', name='I1'),
                            ForeignKeyConstraint(('Stem type', 'Diagram type', 'Semantic', 'Notation'),
                                                 ['Decorated Stem.Stem type', 'Decorated Stem.Semantic',
                                                  'Decorated Stem.Diagram type', 'Decorated Stem.Notation'],
                                                 name='R54_decorated_stem'),
                            ),
        'decoration': Table('Decoration', db.MetaData,
                            Column('Name', String, primary_key=True, nullable=False),
                            ),
        'symbol': Table('Symbol', db.MetaData,
                        Column('Name', String, ForeignKey('Decoration.Name', name='R104'), nullable=False),
                        Column('Shape', Enum('circle', 'arrow', 'cross', 'compound', name='enum_Shape'),
                               nullable=False),
                        PrimaryKeyConstraint('Name', name='I1')
                        ),
        'simple_symbol': Table('Simple Symbol', db.MetaData,
                               Column('Name', String, ForeignKey('Symbol.Name', name='R103'), nullable=False),
                               Column('Stroke', String, nullable=False),
                               Column('Terminal offset', Integer, nullable=False),
                               PrimaryKeyConstraint('Name', name='I1')
                               ),
        'arrow_symbol': Table('Arrow Symbol', db.MetaData,
                              Column('Name', String, ForeignKey('Simple Symbol.Name', name='R100'), primary_key=True,
                                     nullable=False),
                              Column('Base', Integer, nullable=False),
                              Column('Height', Integer, nullable=False),
                              Column('Fill', Enum('solid', 'hollow', 'open', name='enum_Fill'), nullable=False)
                              ),
        'circle_symbol': Table('Circle Symbol', db.MetaData,
                               Column('Name', String, ForeignKey('Simple Symbol.Name', name='R100'), primary_key=True,
                                      nullable=False),
                               Column('Radius', Integer, nullable=False),
                               Column('Solid', Boolean, nullable=False),
                               ),
        'cross_symbol': Table('Cross Symbol', db.MetaData,
                              Column('Name', String, ForeignKey('Simple Symbol.Name', name='R100'), primary_key=True,
                                     nullable=False),
                              Column('Width', Integer, nullable=False),
                              Column('Angle', Integer, nullable=False),
                              ),
        'label': Table('Label', db.MetaData,
                       Column('Name', String, ForeignKey('Decoration.Name', name='R104'), nullable=False),
                       PrimaryKeyConstraint('Name', name='I1')
                       ),
        'compound_symbol': Table('Compound Symbol', db.MetaData,
                                 Column('Name', String, ForeignKey('Symbol.Name', name='R103'),
                                        primary_key=True, nullable=False),
                                 ),
        'symbol_stack_placement': Table('Symbol Stack Placement', db.MetaData,
                                        Column('Position', Integer, nullable=False),
                                        Column('Compound symbol', String,
                                               ForeignKey('Compound Symbol.Name', name='R101_compound'),
                                               nullable=False),
                                        Column('Simple symbol', String,
                                               ForeignKey('Simple Symbol.Name', name='R101_simple'), nullable=False),
                                        Column('Arrange', Enum('adjacent', 'layer', 'last', name='enum_Arrange'),
                                               nullable=False),
                                        Column('Offset', Integer, nullable=False),
                                        PrimaryKeyConstraint('Position', 'Compound symbol', name='I1')
                                        ),
        # Tablet domain
        'asset': Table('Asset', db.MetaData,
                       Column('Name', String, nullable=False),
                       Column('Drawing type', String, nullable=False),
                       Column('Form', Enum('shape', 'text', name='enum_Form')),
                       PrimaryKeyConstraint('Name', 'Drawing type', name='I1'),
                       ),
        'text_style': Table('Text Style', db.MetaData,
                            Column('Name', String, primary_key=True),
                            Column('Typeface', String, ForeignKey('Typeface.Alias', name='R11'), nullable=False),
                            Column('Size', Integer, nullable=False),
                            Column('Slant', Enum('normal', 'italic', name='enum_Slant'), nullable=False),
                            Column('Weight', Enum('normal', 'bold', name='enum_Weight'), nullable=False),
                            Column('Color', String, ForeignKey('Color.Name', name='R10'), nullable=False)
                            ),
        'line_style': Table('Line Style', db.MetaData,
                            Column('Name', String, nullable=False),
                            Column('Pattern', String, ForeignKey('Dash Pattern.Name', name='R8'), nullable=False),
                            Column('Width', Integer, nullable=False),
                            Column('Color', String, ForeignKey('Color.Name', name='R9'), nullable=False),
                            ),
        'dash_pattern': Table('Dash Pattern', db.MetaData,
                              Column('Name', String, primary_key=True),
                              Column('Solid', Integer, nullable=False),
                              Column('Blank', Integer, nullable=False),
                              ),
        'presentation_style': Table('Presentation Style', db.MetaData,
                                    Column('Name', String, nullable=False),
                                    Column('Drawing type', String, ForeignKey('Drawing type.Name', name='R1'),
                                           nullable=False),
                                    PrimaryKeyConstraint('Name', 'Drawing type', name='I1')
                                    ),
        'text_presentation': Table('Text Presentation', db.MetaData,
                                   Column('Asset', String, nullable=False),
                                   Column('Style', String, nullable=False),
                                   Column('Drawing type', String, nullable=False),
                                   Column('Text_style', String, nullable=False),
                                   PrimaryKeyConstraint('Asset', 'Style', 'Drawing type', name='I1'),
                                   ForeignKeyConstraint(('Asset', 'Drawing type'),
                                                        ['Asset.Name', 'Asset.Drawing type'],
                                                        name='R5_R4_asset'),
                                   ForeignKeyConstraint(('Style', 'Drawing type'),
                                                        ['Presentation Style.Name', 'Presentation Style.Drawing type'],
                                                        name='R5_R4_pstyle'),
                                   ),
        'shape_presentation': Table('Shape Presentation', db.MetaData,
                                    Column('Asset', String, nullable=False),
                                    Column('Style', String, nullable=False),
                                    Column('Drawing type', String, nullable=False),
                                    Column('Line style', String, nullable=False),
                                    PrimaryKeyConstraint('Asset', 'Style', 'Drawing type', name='I1'),
                                    ForeignKeyConstraint(('Asset', 'Drawing type'),
                                                         ['Asset.Name', 'Asset.Drawing type'],
                                                         name='R5_R4_asset'),
                                    ForeignKeyConstraint(('Style', 'Drawing type'),
                                                         ['Presentation Style.Name', 'Presentation Style.Drawing type'],
                                                         name='R5_R4_pstyle'),
                                    ),
        'color': Table('Color', db.MetaData,
                       Column('Name', String, primary_key=True),
                       Column('R', Integer, nullable=False),
                       Column('G', Integer, nullable=False),
                       Column('B', Integer, nullable=False)
                       ),
        'typeface': Table('Typeface', db.MetaData,
                          Column('Alias', String, primary_key=True),
                          Column('Name', String, unique=True),
                          ),
    }
