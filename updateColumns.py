#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Author: David Prat

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import *

Base = declarative_base()

class MyTable(Base):

	__tablename__ = 'SomeTable'

	idX = Column(String(20), primary_key=True)
	idY = Column(String(20), primary_key=True)

	ValorI = Column(Integer)
	ValorT = Column(String(20))
	ValorF = Column(Float)
	
	idUser = Column(Integer)
	created = Column(Date)
	modified = Column(Date)

	def __init__(self, idX, idY, ValorI, ValorT, ValorF, idUser, created, modified ):
		self.idX = idX
		self.idY = idY
		self.ValorI = ValorI
		self.ValorT = ValorT
		self.ValorF = ValorF
		self.idUser = idUser
		self.created = created
		self.modified = modified

	def __repr__(self):
		return "<MyTable(%s, %s, %s, %s, %s )>" % (self.idX, self.idY, self.ValorI, self.ValorT, self.ValorF, self.idUser, self.cerated, self.modified)

def main(argv):

	#engine = create_engine('mysql://root:pass@0.0.0.0:3306/someBD', echo=False)
	engine = create_engine('mysql://root:pass@0.0.0.0:3306/someBD', echo=False)
	Session = sessionmaker(bind=engine)
	session = Session()
	
	#all_records = iiSettings.session.query(iiSettings.MyTable).all()
	#for record in all_records:
	#records = session.query(MyTable).filter_by((idY="asdf"))	# filter_by only for one search field 
	records = session.query(MyTable).filter(or_(MyTable.idY=="asdf", MyTable.idY=="asdf2", MyTable.idY=="asdf3", MyTable.idY=="asdf4", MyTable.idY=="asdf5"))

	for record in records:
		print "record "+str(record.idX)+" "+str(record.idY)

		ex2=update(MyTable.__table__).where( and_( MyTable.idX==record.idY, MyTable.idDato==record.idDato )).values(ValorF=record.ValorI, ValorI=None)
		#ex2=update(MyTable.__table__).where( and_( MyTable.idX==record.idX, MyTable.idY==record.idY )).values(ValorI=record.ValorF)
		session.execute(ex2)
		session.flush()

	session.commit()

main(sys.argv[1:])		