import sqlalchemy

from sqlalchemy import Float
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import SmallInteger
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class GTF(Base):
    '''
    General Transfer Format representation.
    '''
    __tablename__ = 'gtfs'

    _id = Column(Integer, primary_key=True)
    sequence = Column(Integer, ForeignKey('gtf_sequences._id'))
    feature = Column(Integer, ForeignKey('gtf_features._id'))
    source = Column(Integer, ForeignKey('gtf_sources._id'))

    strand = Column(Boolean)
    frame = Column(SmallInteger)
    score = Column(Float)
    start = Column(Integer)
    end = Column(Integer)

    frame_constraint_0 = CheckConstraint('frame >= 0')
    frame_constraint_1 = CheckConstraint('frame <= 2')

    start_constraint = CheckConstraint('start >= 0')
    end_constraint = CheckConstraint('end >= start')

    attributes = relationship('GTFAttribute',
        backref=__tablename__,
        cascade='all, delete-orphan',
    )

class GTFSequence(Base):
    '''
    General Transfer Format Sequence
    '''
    __tablename__ = 'gtf_sequences'

    _id = Column(Integer, primary_key=True)
    sequence = Column(String, unique=True)

class GTFFeature(Base):
    '''
    General Transfer Format Feature
    '''
    __tablename__ = 'gtf_features'

    _id = Column(Integer, primary_key=True)
    feature = Column(String, unique=True)

class GTFSource(Base):
    '''
    General Transfer Format Source
    '''
    __tablename__ = 'gtf_sources'

    _id = Column(Integer, primary_key=True)
    source = Column(String, unique=True)

class GTFAttribute(Base):
    '''
    General Transfer Format Attributes
    '''
    __tablename__ = 'gtf_attributes'

    gtf = Column(Integer, ForeignKey('gtfs._id'), primary_key=True)
    key = Column(String, primary_key=True)
    val = Column(String, primary_key=True)
