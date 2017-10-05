import random
import time

while True:
	print("".join([str(random.randint(1, 9)) for i in range(60)]))
	time.sleep(0.25);