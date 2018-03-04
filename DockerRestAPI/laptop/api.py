# Laptop Service

from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class CloseOnlyCSV(Resource):
    def get(self):
        if(request.args.get('top')
            top = int(request.args.get('top')
            lists = []
            lists = db.tododb.find().limit(top+1)
        else:
            lists = db.tododb.find()
        data.sort('name')
        close = ""
    for i in lists:
            name = lists['name']
            description = lists['description']
            cl_time = description[1]
            close = name+cl_time
    return close
class OpenOnlyCSV(Resource):
    def get(self):
        if(request.args.get('top')
            top = int(request.args.get('top')
            lists = []
            lists = db.tododb.find().limit(top+1)
        else:
            lists = db.tododb.find()
        data.sort('name')
        opent = ""
    for i in lists:
            name = lists['name']
            description = lists['description']
            op_time = description[0]
            opent = name+op_time
    return opent
class AllCSV(Resource):
    def get(self):
        if(request.args.get('top')
            top = int(request.args.get('top')
            lists = []
            lists = db.tododb.find().limit(top+1)
        else:
            lists = db.tododb.find()
        data.sort('name')
        total = ""
    for i in lists:
            name = lists['name']
            description = lists['description']
            op_time = description[0]
            cl_time = description[1]
            total = name+op_time+cl_time

class Open(Resource):
    def get(self):
        if(request.args.get('top')
            top = int(request.args.get('top')
            lists = []
            lists = db.tododb.find().limit(top+1)
        else:
            lists = db.tododb.find()
        data.sort('name')
        op = {}

        for i in lists:
            name = lists['name']
            description = lists['description']
            o_time = description[0]
            op[name] = o_time
        
        return op

class Close(Resource):
    def get(self):
        if(request.args.get('top')
            top = int(request.args.get('top')
            lists = []
            lists = db.tododb.find().limit(top+1)
        else:
            lists = db.tododb.find()
        data.sort('name')
        cl = {}

        for i in lists:
            name = lists['name']
            description = lists['description']
            cl_time = description[1]
            cl[name] = cl_time
        
        return cl
class ListAll(Resource):
    def get(self):
        if(request.args.get('top')
            top = int(request.args.get('top')
            lists = []
            lists = db.tododb.find().limit(top+1)
        else:
            lists = db.tododb.find()
        data.sort('name')
        all_l = {}

        for i in lists:
            name = lists['name']
            description = lists['description']
            a_list = description
            all_l[name] = a_list
        
        return all_l





#return {
           # 'Laptops': ['Mac OS', 'Dell', 
          #  'Windozzee',
	 #   'Yet another laptop!',
	#    'Yet yet another laptop!'
   #         ]
  #      }

# Create routes
# Another way, without decorators
api.add_resource(ListAll,'/ListAll')
api.add_resource(ListAll,'/ListAll/json')
api.add_resource(ListAll,'/ListAll/csv')


api.add_resource(OpenOnlyCSV,'/OpenOnlyCSV/csv')
api.add_resource(CloseOnlyCSV,'/CloseOnlyCSV/csv')
api.add_resource(AllCSV,'/AllCSV/csv')
# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
