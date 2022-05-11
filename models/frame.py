from sqlalchemy import Table, Column, Integer, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from consts import BASE


class Frame(BASE):
    __tablename__ = 'Frame'

    os_frame_path = Column(Text, primary_key=True)
    frame_index = Column(Integer)

    video = relationship("Video", back_populates="Frame")
    video_name = Column(Text, ForeignKey('Video.video_name'))

    metadata_xs= relationship("Metadata", back_populates="Frame")
    metadata_id = Column(Integer, ForeignKey('Metadata.id'))
