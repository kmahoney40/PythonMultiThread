import piplates.RELAYplate as RELAY

#RELAY.relayOFF(0,3)
#RELAY.relayOFF(0,4)

def getBool(n, exp):
    exp = exp - 1
    retVal = 0
    e = 2 ** exp
    print n
    print e
    if((n & (2 ** exp)) > 0):
        retVal = 1
    return retVal

def print_relays(val):
    print val
    print "1: " + str(getBool(val, 1))
    print "2: " + str(getBool(val, 2))
    print "3: " + str(getBool(val, 3))
    print "4: " + str(getBool(val, 4))
    print "5: " + str(getBool(val, 5))
    print "6: " + str(getBool(val, 6))
    print "7: " + str(getBool(val, 7))

def reset(pid):
    RELAY.relayOFF(pid, 1)
    RELAY.relayOFF(pid, 2)
    RELAY.relayOFF(pid, 3)
    RELAY.relayOFF(pid, 4)
    RELAY.relayOFF(pid, 5)
    RELAY.relayOFF(pid, 6)
    RELAY.relayOFF(pid, 1)

#RELAY.RESET(0)
reset(0)


result = RELAY.relaySTATE(0)
print_relays(result)

RELAY.relayON(0,1)
RELAY.relayON(0,2)
RELAY.relayON(0,6)

result = RELAY.relaySTATE(0)
print_relays(result)

#RELAY.RESET(0)
reset(0)
result = RELAY.relaySTATE(0)
print_relays(result)




