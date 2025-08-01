from flask import Flask, render_template
import psycopg2


app = Flask(__name__)

connection = psycopg2.connect(database="test", user="souvik", password="test", host="postgres", port=5432)

@app.route("/")
def test():
	cursor = connection.cursor()
	cursor.execute("""SELECT cat, dog FROM vote;""")
	data = cursor.fetchone()
	cursor.close()
	cat, dog = 0, 0
	if data:
		cat, dog = data
		total = cat+dog
		if total != 0:
			cat, dog = round((cat*100)/total, 2), round((dog*100)/total, 2)

	print(cat, dog)
	return render_template("index.html", cat=cat, dog=dog)

if __name__ == "__main__":
	app.run(host="0.0.0.0")