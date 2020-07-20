"""
flatlanddb.py - Loads the existing flatland database
"""
import os
from sqlalchemy import create_engine, MetaData


class FlatlandDB:
    def __init__(self, rebuild=True):
        self.File = 'flatland.db'
        if rebuild:
            if os.path.exists(self.File):
                os.remove(self.File)

        self.Engine = create_engine(f'sqlite:///{self.File}', echo=True)
        self.Connection = self.Engine.connect()
        self.MetaData = MetaData(self.Engine)
        if rebuild:
            self.Relvars = self.Create_relvars()
            self.Populate()
        else:
            self.MetaData.reflect()

    def Create_relvars(self):
        import relvars
        r = relvars.define(self)
        self.MetaData.create_all(self.Engine)
        return r

    def Populate(self):
        for instances, relvar in self.Relvars.items():
            i = __import__(instances+'_instances')
            self.Connection.execute(relvar.insert(), i.population)


db = FlatlandDB()
