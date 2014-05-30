import os
import sys
import csv
import MySQLdb
sys.path.append("/public/gdp/trunk/src/python/")
import GDPCryptUtils
sys.path.append("/data/public/gdp/OPSScript")
import DBConfig
password_Enc='muCnEN2abAhTK/rB/wPAHA=='
password_Dec=GDPCryptUtils.GDPCrypt("glowballonalltix", "globa2b|!2banaly").decrypt(password_Enc)
conn = MySQLdb.connect('db1.localdomain','ukluser',password_Dec,'uklsoft')
cursor = conn.cursor()
connops=MySQLdb.connect('db2.localdomain','uklops','uklDB1@3','uklsoft')
cursorops=connops.cursor()
Bold = "\033[1m"
end = "\033[0;0m"
def lineformat(loan_id,fname,lname,bankname,sortcode,acctno,amount):
#       formatline='D,Lending Stream,%s,%s,%s,%s,%s,%s,%s %s,%s,RFU'
        formatline='871665,chaps_credit,%s,GBP,%s,%s,%s %s,LendingStream,%s'
        result=formatline %(amount*100,str(sortcode),str(acctno),fname,lname,str(loan_id))
        return result
def bacs_cost(count,BatchFile):
#        cost=(0.2/5)*count
        cost=0
        update_cost="update FasterPayments set FPSCost='%s' where BatchFileName='%s'"%(float(cost),BatchFile)
        print update_cost
        cursor.execute(update_cost)
def Table_Insert(loanid,Fname,Lname,Bankname,acctno,sortcode,BatchFile,amount):
        query="insert FasterPayments values('%s','%s','%s','%s','%s','%s',0,'%s',0,1,NULL,1,0,0,0,now(),0,NULL,'Zebit Cash Back or Refund',%s,'FPS','%s','TMS_ZEBIT',0,'0','TS3')" %(loanid,Fname,Lname,Bankname,acctno,sortcode,BatchFile,amount,amount)
        cursor.execute(query)
        print  query

def main():
        infile=raw_input("Enter the Input FileName: ")
        BatchFile=raw_input("Enter the BatchFileName: ")
        BatchfileCheck_Query="select distinct BatchFileName from uklsoft.FasterPayments where BatchFileName='%s'"%(BatchFile)
        cursorops.execute(BatchfileCheck_Query)
        result=cursorops.fetchall()
        if not result:
                Fetch_Data(infile,BatchFile)
        else:
                print Bold+"\nBatchFile Already exists in FasterPayments. Please give a new Name\n"+end
                BatchFile=raw_input("Enter the BatchFileName: ")
                BatchfileCheck_Query="select distinct BatchFileName from uklsoft.FasterPayments where BatchFileName='%s'"%(BatchFile)
                cursorops.execute(BatchfileCheck_Query)
                result=cursorops.fetchall()
                if not result:
                        Fetch_Data(infile,BatchFile)
                else:
                        print Bold+"\nThis Name also already exists in FasterPayments,Please check it and run the script again\n"+end
                        print Bold+"Exit"+end
                        sys.exit()
def Fetch_Data(infile,BatchFile):
        amountfinal=0
        outfile='/Payout/Pacnet/'+(BatchFile.replace('CSV','PACNET',1))
        filein=csv.reader(open(infile),delimiter='\n')
        fileout=open(outfile,"wb")
        fileout.write("RavenPaymentFile_v1.0")
        fileout.write("PaymentRoutingNumber,PaymentType,Amount,CurrencyCode,BankNumber,AccountNumber,AccountName,Description,Reference")
        count=0
        filein.next()
        filein.next()
        for row in filein:
                result=str(row[0]).split(',')
                print result
                if result :
                        print result
                        Agree = result[0]
                        cash = result[5]
                        ip = int(float(cash))
                        print ip
                        print Agree,cash
                        check_query = "select AgreementNumber, BatchFileName,`Payout Amount` from FasterPayments where AgreementNumber='%s' and (opscomment rlike 'CashBack' or  opscomment rlike 'Cash Back')"%(Agree)
                        print check_query
                        cursorops.execute(check_query)
                        Fast = cursorops.fetchall()
                        print Fast

                        if Fast :
                                for check in Fast :
                                        print check
                                        op = int(float(check[2]))
                                        if ip == op :
                                                print "\n"+Bold+" AgreementNumber '%s' is already present in BatchFileName: '%s' \n\n DONT BE CARELESS"%(check[0],check[1]) +end
                                                break
                                        else:
                                                print "Please Double check with FasterPayments for AgreementNumber '%s', Because it seems to be already paid"%(Agree)
                                                break
                        else :
                                sortcode=result[11]
#                               BanknameQuery="select mabankname) from FasterPayments where sortcode='%s'"%(sortcode)
#                               cursorops.execute(BanknameQuery);BankName=cursorops.fetchall()[0][0]
                                acctno=result[10]
                                amount_file=str(result[5])
                                amount_table=result[5]
                                loanid=result[0]
                                Fname=result[7]
                                Lname=result[8]
                                Bankname=result[9]
                                count+=1
                                acctnumber=GDPCryptUtils.GDPCrypt("glowballonalltix", "globa2b|!2banaly").encrypt(acctno)
                                result_Final=lineformat(loanid,Fname.capitalize(),Lname.capitalize(),Bankname,sortcode,acctno,amount_file)
                                amountfinal+=float(amount_file)*100
                                print result_Final
                                fileout.write(str(result_Final)+'\n')
                                Table_Insert(loanid,Fname,Lname,Bankname,acctnumber,sortcode,BatchFile,amount_table)
        cost=bacs_cost(count,BatchFile)
        fileout.write('RavenFooter',+str(count),str(amountfina))
        print "\nOutput File Generated: "+Bold +outfile +end

if __name__ == "__main__":
       main()
