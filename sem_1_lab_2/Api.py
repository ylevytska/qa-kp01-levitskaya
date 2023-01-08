from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class BinaryApi(Resource):
    def get(self):
        return "BinaryApi"

class BufferApi(Resource):
    def get(self):
        return "BufferApi"

class DirectoryApi(Resource):
    def get(self):
        return "DirectoryApi"

class LogTextApi(Resource):
    def get(self):
        return "LogTextApi"

api.add_resource(BinaryApi, '/binaryfile')
api.add_resource(BufferApi, '/bufferfile')
api.add_resource(DirectoryApi, '/directory')
api.add_resource(LogTextApi, '/logtextfile')

if __name__ == '__main__':
    app.run(debug=True)