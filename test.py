import serial
import os.path
from time import strftime

dev = raw_input("Enter device directory: ")
print "entered device", dev

serialIO = serial.Serial("/dev/tty"+dev, 38400, timeout=1)



while True :

    serialIO.write("01 0C \r") 
    line_rpm = serialIO.readline().split(" ")
    rpm = int("0x"+line_rpm[4]+line_rpm[5], 16)/4
    print "RPM ", rpm "\n"
    
    serialIO.write("01 14 \r") 
    line_ox1 = serialIO.readline().split(" ")
    ox1 = int("0x"+line_ox1[4]+line_ox1[5], 16)/4
    print "OX1 ", ox1 "\n"
    #14-1B
    
    serialIO.write("01 10 \r")
    line_maf = serialIO.readline().split(" ")
    maf = int("0x"+line_maf[4]+line_maf[5], 16)/100
    print "MAF ", maf "\n"
    
    serialIO.write("01 11 \r")
    line_tp = serialIO.readline().split(" ")
    tp = int("0x"+line_tp[4], 16)*100/255
    print "TP ", tp "\n"
   #print speed, "km/h ; ",rpm, "rpm ; TP:",tp," ; Load:",load,"%\n"
