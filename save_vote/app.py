import redis
import json, time
import psycopg2

from config import *


while True:
	r = redis.Redis(host='redis', port=6379, db=0)
	connection = psycopg2.connect(database="test", user="souvik", password="test", host="postgres", port=5432)
	cursor = connection.cursor()
	final_value = {"cat":0, "dog":0}
	for key in r.scan_iter(match='*', count=100):
		value = r.get(key.decode())
		data = json.loads(value.decode())
		for k, v in data.items():
			final_value[k] += v
		r.expire(key.decode(), 0)

	print(final_value)
	rowcount = cursor.execute("""UPDATE vote SET cat = cat + %(cat)s, dog = dog + %(dog)s;""", final_value)
	connection.commit()
	print(cursor.rowcount)
	cursor.close()
	connection.close()

	time.sleep(SLEEP_TIME)