from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from consts import BASE


class Meta_Data(BASE):
    __tablename__ = 'Metadata'

    id = Column(Integer, primary_key=True)
    frame_label = Column(Boolean)
    azimuth = Column(Integer)
    elevation = Column(Integer)
    fov = Column(Integer)
