from flask import Flask, request
from flask_restful import Resource, Api
from Directory import Directory
from BinaryFile import BinaryFile
from LogTextFile import LogTextFile
from BufferFile import BufferFile
import json

app = Flask(__name__)
api = Api(app)

parentDirectory = Directory('parentDir')

fileName = 'binary file'
content = 'binary content'
binary = BinaryFile(fileName, content, parentDirectory)

name = 'buffer file'
size = 10
buffer = BufferFile(name, size)

maxElements = 10
name = 'directory'
directory = Directory(name, maxElements)

name = 'logTextFile'
log = LogTextFile(name, parentDirectory)

class BinaryApi(Resource):
    def __init__(self):
        self.binary = binary
    def get(self):
        return self.binary.read()
    def post(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        self.binary = BinaryFile(data["fileName"], data["content"], parentDir)
        return {'message': 'BinaryFile is successfully created'}
    def put(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        return self.binary.move(parentDir)
    def delete(self):
        return self.binary.delete()

class BufferApi(Resource):
    def __init__(self):
        self.buffer = buffer
    def get(self):
        return self.buffer.consume()
    def post(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        self.buffer = BufferFile(data["fileName"], data["maxSize"], parentDir)
        return {'message': 'BufferFile is successfully created'}
    def put(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        return self.buffer.move(parentDir)
    def patch(self):
        data = json.loads(request.data)
        return self.buffer.push(data["element"])
    def delete(self):
        return self.buffer.delete()

class DirectoryApi(Resource):
    def get(self):
        return {'hello': 'world'}
    def __init__(self):
        self.directory = directory
    def post(self):
        data = request.get_json()
        self.directory = Directory(data["name"], data["maxElements"])
        return {'message': 'Directory is successfully created'}
    def put(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        return self.directory.move(parentDir)
    def delete(self):
        return self.directory.delete()

class LogTextApi(Resource):
    def __init__(self):
        self.logText = LogTextFile
    def get(self):
        return self.logText.read()
    def post(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        self.logText = LogTextFile(data["fileName"], parentDir)
        return {'message': 'LogTextFile is successfully created'}
    def put(self):
        data = request.get_json()
        parentDir = Directory(data["parent"])
        return self.logText.move(parentDir)
    def patch(self):
        data = request.get_json()
        return self.logText.log(data["line"])
    def delete(self):
        return self.logText.delete()

api.add_resource(BinaryApi, '/binaryfile')
api.add_resource(BufferApi, '/bufferfile')
api.add_resource(DirectoryApi, '/directory')
api.add_resource(LogTextApi, '/logtextfile')

if __name__ == '__main__':
    app.run(debug=True)