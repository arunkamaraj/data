import telnetlib, time


print ("Starting Client...")
host    = input("127.0.0.1")
timeout = 10

print ("Connecting...")
try:
    session = telnetlib.Telnet(host, 5554, timeout)
except socket.timeout:
    print ("socket timeout")
else:
    print("Sending Commands...")
    session.write("sms send +919790554929 hi da".encode('ascii') + b"\r")
    print("Reading...")
    output = session.read_until(b"/r/n/r/n#>", timeout )
    session.close()
    print(output)
    print("Done")
