while True:
   stringName = raw_input("Convert string to hex & ascii(type stop to quit): ")
   if stringName == 'stop':
      break
   else:   
      convertedVal = stringName.encode("hex")
      new_list = []
      convertedVal.strip() #converts string into char
      for i in convertedVal:
         new_list = ord(i)


      print "Hex value: " + convertedVal
      print "Ascii value: " + new_list     
