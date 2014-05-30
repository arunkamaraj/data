import telnetlib
host = "localhost"
port = "5554"
tn = telnetlib.Telnet(host,port)
i='sms send +65487 oporttant \n'
tn.write(i)
tn.close()
