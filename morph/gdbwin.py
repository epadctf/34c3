#!/usr/bin/python

import gdb
from sys import stdout

#run with gdb -q -x gdbwin.py

def callGdb(cmd):
	return gdb.execute(cmd, to_string=True).splitlines()

def getEntrypoint():
	callGdb("r")
	info = callGdb("info file")[3]
	entrypoint = info.split(": ")[1]
	return int(entrypoint, 16)

def getInputChar():
	l = callGdb("print $al")[0]
	c = l.split("= ")[1]
	return chr(int(c, 16))

def getExpected():
	l  = callGdb("x/i $rip")[0]
	c = l.split(",")[1]
	return chr(int(c, 16))

def fixCmp(expected):
	callGdb("set $al='"+expected+"'")

def runToCmp():
	callGdb("si")
	callGdb("s")
	callGdb("s")
	callGdb("s")

def setupInput():
	im = {}
	for i in range(23):
		im[chr(0x41+i)] = "*"
	return im

def printProgressOnFlaggu(inputDict):
	flag = ""
	for (key, value) in inputDict.items():
		flag += value
	stdout.write("\r"+flag)
	stdout.flush()

callOffset = 0xb95 - 0x7a0

callGdb("file ./morph")

entrypoint = getEntrypoint()
callRaxAddr = entrypoint+callOffset

callGdb("b *"+hex(callRaxAddr))

inputDict = setupInput()
inputString = "".join(["%s" % key for (key, _) in inputDict.items()])

callGdb("r "+inputString)

for i in range(len(inputString)-1):
	runToCmp()
	c = getInputChar()
	expected = getExpected()
	fixCmp(expected)
	inputDict[c] = expected
	callGdb("c")
	printProgressOnFlaggu(inputDict)

print("")
gdb.execute("q")

