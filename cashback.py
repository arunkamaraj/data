import os
import sys
import csv
sys.path.append('/home/arun.k/')
import GDPCryptUtils
import MySQLdb
conn = MySQLdb.connect('wenchuan','arun.k','EAsterly?7','uklsoft')
cur=conn.cursor()
def file():
        filename=raw_input("enter ur  batch file name :")
        new_filename=raw_input("enter new batch file for payment :")
        check="select distinct BatchFileName from uklsoft.FasterPayments where BatchFileName='%s'"%(new_filename)
        r=cur.execute(check)
        result=cur.fetchall()
        print filename
        print new_filename
        if result:
                print "no no"
        else:
                print "machi super"

if __name__=="__main__":
        file()
