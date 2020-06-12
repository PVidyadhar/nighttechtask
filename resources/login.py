from flask_restful import Resource
from flask import request,json
import shutil

class Login(Resource):
    def post(self):
        data=request.form['data']
        data = json.loads(data) 
        image=request.files.get('file','')
        filename=f'''D:/{data['name']}.jpg'''
        #if image.status_code == 200:
        #image.raw.decode_content = True
        #image.save(f'''D:/{data['name']}.jpg''')
        with open(filename,'wb') as f:
            shutil.copyfileobj(image, f)
        if (image is None):
            return {"message":"image cannot be empty"},201
        if data['name'] == "":
            return {"message":"name cannot be empty"},201
        if data['emailid'] == "":
            return {"message":"emailid cannot be empty"},201

        try:
            return f"""Your name is {data['name']} and email id is {data['emailid']} and image is received succesully"""
        except:
            return {"message":"There was an error while returning data."},500