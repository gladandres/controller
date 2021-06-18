from cotroll_library import get_status, set_request
from flask import Flask, jsonify
from flask import abort
#from controll_library import *
#from article_class import *
#from app_scraping import *



app = Flask(__name__)
IP = '192.168.100.101'


@app.route('/comand/REL/<string:relnumb>/<string:state>', methods=['GET'])
def get_command_rele(relnumb, state):
    if not int(relnumb) in range(1,5):
        return jsonify({'status_command': 'Error parametr 1'}) 
    if not int(state) in range(2):
        return jsonify({'status_command': 'Error parametr 2'})
    com = 'REL'
    command = ','.join([com,relnumb, state])
    status = set_request(IP, command)
    if not isinstance(status,str):
        abort(404)
    return jsonify({'status_command': status, 'command':command})


@app.route('/comand/OUT/<string:linumb>/<string:state>', methods=['GET'])
def get_command_out(linumb, state):
    if not int(linumb) in range(1,13):
        return jsonify({'status_command': 'Error parametr 1'}) 
    if not int(state) in range(2):
        return jsonify({'status_command': 'Error parametr 2'})
    com = 'OUT'
    command = ','.join([com, linumb, state])
    status = set_request(IP, command)
    if not isinstance(status,str):
        abort(404)
    return jsonify({'status_command': status, 'command':command})

@app.route('/comand/PWM/<string:power>', methods=['GET'])
def get_command_pwm(power):
    if not int(power) in range(101):
        return jsonify({'status_command': 'Error parametr 1'}) 
    com = 'PWM'
    command = ','.join([com, power])
    status = set_request(IP, command)
    if not isinstance(status,str):
        abort(404)
    return jsonify({'status_command': status, 'command':command})
    

@app.route('/status', methods=['GET']) 
def get_news_site():
    status = get_status(IP)
    if not isinstance(status,dict):
       abort(404)
    return jsonify({'status': status})        
    


if __name__ == '__main__':
    app.run(debug=True)