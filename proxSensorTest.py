from labjack import ljm
import time

# Open first found LabJack
#handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier
handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier

info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

# Setup and call eReadName to read from AIN0 on the LabJack.
proxLow = "AIN2"
proxHigh = "AIN3"

while True:
    low = ljm.eReadName(handle, proxLow)
    high = ljm.eReadName(handle, proxHigh)
    print(str(low))
    print(str(high))
    #print("\n%s reading : %f V" % (name, result))
    if low > 4:
        print("DETECTION")
        time.sleep(1)
    elif high > 4:
        print("NO PROX")
        time.sleep(1)
    else:
        print("----------")
        time.sleep(1)


# Close handle
ljm.close(handle)
