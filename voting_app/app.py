from flask import Flask
import apis

def create_app():
	app = Flask(__name__)
	return app

if __name__ == "__main__":
	app = create_app()
	app.register_blueprint(apis.api)
	app.run(host="0.0.0.0")

