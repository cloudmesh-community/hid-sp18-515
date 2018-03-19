from eve import Eve
from flask import Response as Rp
from psutil import virtual_memory
import json
import platform
import shutil
import getpass

settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'DOMAIN': {}
    }

app = Eve(settings = settings)


@app.route('/computer')
def computer():
    rp=Rp()
    rp.headers['status'] = 200
    rp.headers['Content-Type'] = "application/json ; charset=utf-8"
    data = {
        'processor': platform.processor(),
        'operating system': platform.system(),
        'memory': virtual_memory().total,
        'username': getpass.getuser(),

    }
    rp.data = json.dumps(data)
    return rp


@app.route('/memory')
def ram():
    rp = Rp()
    rp.headers['status'] = 200
    rp.headers['Content-Type'] = "application/json ; charset=utf-8"
    memory = virtual_memory()
    data = {
        'total': memory.total,
    }
    rp.data = json.dumps(data)
    return rp


@app.route('/username')
def user():
    rp = Rp()
    rp.headers['status'] = 200
    rp.headers['Content-Type'] = "application/json ; charset=utf-8"
    user = getpass.getuser()
    data = {
        'user': user,
    }
    rp.data = json.dumps(data)
    return rp


if __name__ == "__main__":
 app.run()
