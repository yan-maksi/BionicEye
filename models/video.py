from sqlalchemy import Table, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship, mapper

from consts import BASE


class Video(BASE):
    __tablename__ = 'Video'

    video_name = Column(Text, primary_key=True)
    video_path = Column(Text)
    frame_amount = Column(Integer)
    frames = relationship("Frame", back_populates="Video")