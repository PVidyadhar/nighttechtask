from flask_restful import Resource
from flask import request,json

class Login(Resource):
    def post(self):
        data=request.form['data']
        data = json.loads(data) 
        #image=request.files.get('file','')
        #image.save(f'''D:/{data['name']}.jpg''')
        '''if (open(f'''D:/{data['name']}.jpg''',"rb", buffering=0) is None):
            return {"message":"image cannot be empty"},201'''
        if data['name'] == "":
            return {"message":"name cannot be empty"},201
        if data['emailid'] == "":
            return {"message":"emailid cannot be empty"},201

        #try:
        return f"""Your name is {data['name']} and email id is {data['emailid']} and image is received succesully"""
        #except:
        #return {"message":"There was an error while returning data."},500