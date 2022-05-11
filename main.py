from consts import BASE
from models.video import Video
from models.frame import Frame
from models.metadata import Meta_Data
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:12345678@localhost:5432/BionicEye", echo=True)
BASE.metadata.drop_all(engine, tables=[Frame.__table__, Meta_Data.__table__, Video.__table__])
BASE.metadata.create_all(engine, tables=[Frame.__table__, Meta_Data.__table__, Video.__table__])
