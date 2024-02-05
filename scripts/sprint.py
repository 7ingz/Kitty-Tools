import os
import sys,time
def sprint(str):
	for i in str + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()

		time.sleep(3/90)


def command(str):
	os.system(str)
