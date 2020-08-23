"""
annotation.py - Annotation class as modeled in the class diagram
"""
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stem_type import StemType


class Annotation:
    """

    """
    @staticmethod
    def getLabel(stem_type: 'Stem Type', semantic: str, notation: str):
        return None

