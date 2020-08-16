"""
flatlanddb.py - Loads the existing flatland database
"""
import os
from sqlalchemy import create_engine, MetaData
from symbol import Symbol


def Create_relvars():
    import relvars
    FlatlandDB.Relvars = relvars.define(db=FlatlandDB)
    FlatlandDB.MetaData.create_all(FlatlandDB.Engine)


def Populate():
    for instances, relvar in FlatlandDB.Relvars.items():
        i = __import__(instances + '_instances')
        FlatlandDB.Connection.execute(relvar.insert(), i.population)
    Symbol.update_symbol_lengths(FlatlandDB)


class FlatlandDB:
    File = os.path.expandvars("$FLATLAND3_PYCHARM/Database/flatland.db")
    MetaData = None
    Connection = None
    Engine = None
    Relvars = None

    def __init__(self, rebuild=True):
        if rebuild:
            if os.path.exists(FlatlandDB.File):
                os.remove(FlatlandDB.File)

        FlatlandDB.Engine = create_engine(f'sqlite:///{FlatlandDB.File}', echo=True)
        FlatlandDB.Connection = FlatlandDB.Engine.connect()
        FlatlandDB.MetaData = MetaData(FlatlandDB.Engine)
        if rebuild:
            Create_relvars()
            Populate()
        else:
            FlatlandDB.MetaData.reflect()


if __name__ == "__main__":
    FlatlandDB()
