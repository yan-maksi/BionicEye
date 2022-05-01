from sqlalchemy import create_engine, select, Table, Column, String, Integer, MetaData, ForeignKey

meta = MetaData()

data = Table('models ', meta,
             Column('id_video', Integer, primary_key=True),
             Column('Video', Integer),
             Column('Frame', Integer),
             Column('Metadata', String, nullable=False)
             )

engine = create_engine("mysql+mesqlconnctor://root:root@localhost/pyloungedb", echo=True)
meta.create_all(engine)

conn = engine.connect()

ins_data_query = data.insert().values(Video="Tel_Aviv")  # pass the parameters for writing to the database
conn.execute(ins_data_query)
