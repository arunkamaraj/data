import os
import sys
import xlrd
import csv
import datetime
import time
import MySQLdb
import smtplib
mysql = MySQLdb.connect('localhost','opsuser','OPS!@#','TMS_Data')
cursor=mysql.cursor()
from warnings import filterwarnings
import MySQLdb as Database
import pdb
filterwarnings('ignore', category = Database.Warning)

book=xlrd.open_workbook('/tmp/LS closeout report we 221213.xls')
book1=xlrd.open_workbook('/tmp/latest.xls')
book2=xlrd.open_workbook('/tmp/uses1.xls')
#sheet=book.sheet_by_index(0)
f=open('lscloseout.csv','wb')

def gen_table(Header,Tuple,opt="center"):
    html_str=''
    if Tuple:
        if Header:
            html_str+='<table style="font-size:14px" border=1 cellspacing=0><tr>'
            for value in Header:
                print str(value), opt
                print 'html_str',html_str
                html_str+='<th bgcolor="yellowgreen" align="'+opt+'">'+str(value)+'</th>'
            html_str+='</tr>\n'
        for rows in Tuple:
            html_str+='\n<tr>'
            for value in rows:
                html_str+='<td align="'+opt+'">'+str(value)+'</td>'
            html_str+='</tr>'
        html_str+='</table>'
    else:
        html_str='<br /> --No Data--'
    return html_str

def sendmail(sender,receiver,sub,htmlmsg,cc=[]):
        message="""From:<uklops@global-analytics.com>
To:"""+','.join(receiver) + """
cc:"""+','.join(cc) + """
MIME-Version:1.0
Content-type: text/html
Subject: """ + sub + """
"""+htmlmsg
        smtpObj=smtplib.SMTP('localhost')
        smtpObj.sendmail(sender,receiver+cc,message)

class closure:

        def xlstocsv(self,i):
                if i=='closure':
                        sheet=book.sheet_by_index(0)
                        for row_index in range(1,sheet.nrows):
                                row_num=row_index
                                clientcode=sheet.cell(row_index,0).value
                                clientref= sheet.cell(row_index,1).value
                                LoanID=int(clientref)
                                AccID=sheet.cell(row_index,2).value
                                CustName=sheet.cell(row_index,3).value
                                Balance=(sheet.cell(row_index,4).value)
                                status=sheet.cell(row_index,5).value
                                statusDate=sheet.cell(row_index,6).value
                                status_date=datetime.datetime(*xlrd.xldate_as_tuple(statusDate, book.datemode)).date()
                                reason=sheet.cell(row_index,7).value
                                Description=sheet.cell(row_index,8).value
                                s="'%s','%s','%s','%s','%s','%s','%s','%s','%s'"%(clientcode,LoanID,AccID,CustName,Balance,status,status_date,reason,Description)
                                insertquery='''insert into test.MHClosedHistory_test values('%s','%s','%s',"%s",'%s','%s','%s','%s','%s','','',now())'''%(clientcode,LoanID,AccID,CustName,Balance,status,status_date,reason,Description)
#                               print insertquery
#                               print s
                                cursor.execute(insertquery)
                                f.write(str(s)+'\n')
                elif i=='openMH':
                        sheet=book1.sheet_by_index(0)
                        for row_index in range(1,sheet.nrows):
                                row_num=row_index
                                clientref=sheet.cell(row_index,2).value
                                LoanID=int(clientref)
                                AscentRef=sheet.cell(row_index,3).value
                                CustName=sheet.cell(row_index,4).value
                                InstrDate=sheet.cell(row_index,5).value
                                Status=sheet.cell(row_index,6).value
                                StatusDate=sheet.cell(row_index,7).value
                                Reason=sheet.cell(row_index,8).value
                                DESCRIPTION=sheet.cell(row_index,9).value
                                ClientReason=sheet.cell(row_index,10).value
                                InstrBal=sheet.cell(row_index,11).value
                                paid=sheet.cell(row_index,12).value
                                ClearedPayments=sheet.cell(row_index,13).value
                                Adjusted=sheet.cell(row_index,14).value
                                CommTotal=sheet.cell(row_index,15).value
                                InvBalance=sheet.cell(row_index,16).value
                                cursor.execute("select count(*) from test.MHopenHistory_test where LoanID='%s'"%LoanID)
                                a=cursor.fetchone()
#                               print int(a[0])
                                insertquery='''insert into test.MHopenHistory_test values('%s','%s',"%s",'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','','',now(),'0')'''%(LoanID,AscentRef,CustName,InstrDate,Status,StatusDate,Reason,DESCRIPTION,ClientReason,InstrBal,paid,ClearedPayments,Adjusted,CommTotal,InvBalance)
                                if int(a[0]):
#                                       print "in-1"
                                        aa="update test.MHopenHistory_test set override_flag=1 where LoanID='%s'"%LoanID
                                        cursor.execute(aa)

                                cursor.execute(insertquery)
                elif i=='openCRS' :
                        sheet=book2.sheet_by_index(0)
                        print "sheet readed"
                        for row_index in range(1,sheet.nrows):
                                row_num=row_index
                                Debtcode=sheet.cell(row_index,0).value
                                dtcliref=sheet.cell(row_index,1).value
                                Dtdatinstr=sheet.cell(row_index,2).value
                                dtcurbal=sheet.cell(row_index,3).value
                                dtpdtodate=sheet.cell(row_index,4).value
                                cursor.execute("select count(*) from test.CRSopenHistory_current where dtcliref='%s'"%dtcliref)
                                a=cursor.fetchone()
#                               print int(a[0])
                                print "inserting.."
                                insertquery='''insert into test.CRSopenHistory_current values('%s','%s',"%s",'%s','%s',now())'''%(Debtcode,dtcliref,Dtdatinstr,dtcurbal,dtpdtodate)
                                if int(a[0]):
#                                       print "in-1"
                                        aa="update test.CRSopenHistory_test set override_flag=1 where dtcliref='%s'"%dtcliref
                                        cursor.execute(aa)
                                cursor.execute(insertquery)

                if i=='closure':
                        nos="select count(*) from test.MHClosedHistory_test where date(currenttime)=curdate()"
                        cursor.execute(nos)
                        uooo=cursor.fetchone()
                        print "%s rows inserted today"%uooo
                elif i=='open':
                        nos="select count(*) from test.MHopenHistory_test where date(currenttime)=curdate()"
                        cursor.execute(nos)
                        uooo=cursor.fetchone()
                        print "%s rows inserted today"%uooo
        def loadcsv(self):
                print "--loading into table--"
                loadquery="load data local infile 'lscloseout.csv' into table test.MHClosedHistory_test fields terminated by ',' enclosed by ''' lines terminated by '\n' ignore 1 lines"

                countq="select count(*) from test.MHClosedHistory_test limit '%s'"
                print "--done--"
                cursor.execute(loadquery)
        def queries(self,i):
                if i=='closure':
                        print "--update collectionInfo closures into current table"
                        CollectioInfo_closure="update test.MHClosedHistory_test mh join TMS_Data.Collection_Info cl on cl.loan_id=mh.loanid set CI_closure_cd=closure_cd where dca_name='MH' and date(mh.currenttime)=curdate()"
                        cursor.execute(CollectioInfo_closure)
                        print "updated"
                        print "updating ReportsData files"
                        Reportsdata="update test.MHClosedHistory_test mh join REPORTS_Data.ClosureFile cf on cf.loan_id=mh.loanid set ClosureFile_Status=1 where generated_by='Web Service' and date(mh.currenttime)=curdate()"
                        cursor.execute(Reportsdata)
                        print "done...cool"
                elif i=='open':
                        TMSInvBalance="update test.MHopenHistory_test mho join (select py.loan_id,(pc.OutstandingInterest+pc.OutstandingFee+py.OPB) as InventoryBalance from Payments py join (select loan_id,sum(if(pc.payment_type rlike 'LZD',pc.payment_amt-pc.paid_amt,0)) as OutstandingInterest,sum(if(pc.payment_type rlike 'FEE',pc.payment_amt-pc.paid_amt,0)) as OutstandingFee from PaymentCalendar as pc join test.MHopenHistory_test mh on pc.loan_id=mh.loanid  where pc.override_flag=0 group by loan_id) pc on py.loan_id = pc.loan_id)a on a.loan_id=mho.loanid set TMSInvBalance=InventoryBalance"
                        cursor.execute(TMSInvBalance)
                        print "TMS InvBalance open-updated"
                        paidinTMS="update test.MHopenHistory_test mho join(select loan_id, sum(debit)debsum from TMS_Data.Transactions t join test.MHopenHistory_test mh on t.loan_id=mh.loanid where payment_method='COLLECTION AGENCY' and merchant_name='Mackenzie Hall' group by 1)a on mho.loanid=a.loan_id set PaidInTMS=debsum"
                        cursor.execute(paidinTMS)
                        print "paidinTMS open-udpated"

        def reporting(self):
                reportq="select loanid,CI_closure_cd,if(Reason='BANKRUPT','BKT',if(Reason='cli_req','CRQ',if(Reason='FRAUD','FRD',Reason)))Reas from test.MHClosedHistory_test where CI_closure_cd!=Reason having CI_closure_cd!=Reas"
                countq="select count(*) from (select loanid,CI_closure_cd,if(Reason='BANKRUPT','BKT',if(Reason='cli_req','CRQ',if(Reason='FRAUD','FRD',Reason)))Reas from test.MHClosedHistory_test where CI_closure_cd!=Reason having CI_closure_cd!=Reas)a"
                Nullq="select count(*) from test.MHClosedHistory_test where CI_closure_cd is NULL"
                BalanceMis="select count(*) from test.MHopenHistory_test where InvBalance!=TMSInvBalance"
                cursor.execute(BalanceMis)
                Balancechk=cursor.fetchall()
                cursor.execute(Nullq)
                LoansNotClosed=cursor.fetchall()
                cursor.execute(reportq)
                reportdata=cursor.fetchall()
                cursor.execute(countq)
                mismatchcnt=cursor.fetchall()
                Header=['LoanID','MH Status','TMS Collection Status']
                Header2=['No. of Loans not closed in TMS']
                Header1=['Count of Loans Mismatched']
                Header3=['Open Loans Balance Mismatch']
#               mailcontent = "<font face='arial' size = 2>Hi,<br></br>PFB the count of Loans mismatched in closure file : <br/>"+gen_table(Header1,mismatchcnt)+"<br/><br>"+gen_table(Header2,LoansNotClosed)+"<br>PFB the count of Loans mismatched in open file :<br/>"+gen_table(Header3,Balancechk)+"</br>PFB the List of Loans & their status Mismatched: <br/>"+gen_table(Header,reportdata)+" <br/> <br><br/>Regards,<br/>Gokul<br>"
                mailcontent = "<font face='arial' size = 2>Hi,<br></br>PFB the count of Loans mismatched in closure file : <br/>"+gen_table(Header1,mismatchcnt)+"<br/><br>"+gen_table(Header2,LoansNotClosed)+"<br>PFB the count of Loans mismatched in open file :<br/>"+gen_table(Header3,Balancechk)+" <br/> <br><br/>Regards,<br/>Gokul<br>"
                sender= "gokul.b@global-analytics.com"
                to=['gokul.b@global-analytics.com']
                cc=['']
                subject='Collection : Mismatch Report'
                sendmail(sender,to,subject,mailcontent,cc)

if __name__== '__main__':

        whatsapp=closure()
        if str(sys.argv[1])=='reports':
                whatsapp.reporting()
        whatsapp.xlstocsv(str(sys.argv[1]))
        whatsapp.queries(str(sys.argv[1]))

