from app import app
from model import user_model
from flask import request



@app.route("/user/getall")
def user_getall_controller():
    return user_model.user_getall_model()

@app.route("/user/getbyid/<id>",methods=['GET'])
def user_getbyid_controller(id):
    # print("form request = ",request.form)
    return user_model.user_getbyid_model(id)



@app.route("/user/addone",methods=['POST'])
def user_addone_controller():
    # print("form request = ",request.form)
    return user_model.user_addone_model(request.form)

@app.route("/user/update",methods=['PUT','PATCH'])
def user_update_controller():
    print("form request = ",request.form)
    return user_model.user_update_model(request.form)


@app.route("/user/delete/<id>",methods=['DELETE'])
def user_delete_controller(id):
    # print("form request = ",request.form)
    return user_model.user_delete_model(id)


