#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Author: David Prat
#Date: 21/12/2017
#SQLAlchemy code that erases blank fields at the end of MySQL table entries

import sys
import traceback
import os
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
#from sqlalchemy import *

#Define the models class mapper
Base = declarative_base()
class MyTable(Base):
        __tablename__ = 'theTable'
	#Define the composited primary key
        indId = Column(String(20), primary_key=True)
        datId  = Column(String(20), primary_key=True)
	#Define the other table fields
        iVal = Column(Integer)
        tVal = Column(String(250))
	fVal = Column(Float)
	dVal = Column(String(250))
	
        def __init__(self, iVal, tVal, fVal, dVal):
                self.iVal = iVal
                self.tVal = tVal
                self.fVal = fVal
                self.dVal = dVal
	#Define the returned values and format when quering
        def __repr__(self):
                return "<MyTable(%s, %s, %s, %s, %s, %s )>" % (self.indId, self.datId, self.iVal, self.tVal, self.fVal, self.dVal)
                #return "<MyTable(indId=%s, datId=%s, iVal=%s, tVal=%s, fValue=%s, dVal=%s )>" % (self.indId, self.datId, self.iVal, self.tVal, self.fVal, self.dVal)


def main(argv):
	#Connect to the MySQL Database
	engine = create_engine('mysql://root:grr09Server@10.4.2.65:3306/celgene_ddbb_copy1', echo=False)
	#Call the session which bind the db engine to manipulate the database
	Session = sessionmaker(bind=engine)
	session = Session()
	#Query the table	
	all_records = session.query(MyTable).all()
	#Iterate through records
	for rec in all_records:
		#print rec.tValue
		tv  =str(rec.tVal)
		tvs =str(rec.tVal).strip()
		iv  =str(rec.iVal)
		ivs =str(rec.iVal).strip()
		fv  =str(rec.fVal)
		fvs =str(rec.fVal).strip()
		dv  =str(rec.dVal)
		dvs =str(rec.dVal).strip()
			
		#check if fields are formated such as strip() function. If not they should be fixed
		#In this case, only the tVal had differences, but the code should include the modifications for all fields
		if tv!=tvs:
			print "diff-t-------------->: -"+tv+"-"+tvs+"-"
			#Modify the table records
			#rec.tVal=tvs
			#session.commit()
			
		if iv!=ivs:
			print "diff-v-------------->: -"+iv+"-"+ivs+"-"
		if fv!=fvs:
			print "diff-f-------------->: -"+fv+"-"+fvs+"-"
		if dv!=dvs:
			print "diff-d-------------->: -"+dv+"-"+dvs+"-"


if __name__ == "__main__":	
	main(sys.argv[1:])

