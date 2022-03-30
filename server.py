# from crypt import methods
from ast import Try
from email import message
from logging import exception
from os import abort
from traceback import format_tb
from turtle import pd
from flask import Flask, Response, request
from numpy import mintypecode
import json
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

############### connecting to database - MongoDB ###################
try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        ServerSelectionTimeoutMS=1000
    )
    db = mongo.curd
    mongo.server_info()  # when database not connect then trigger exception

except:
    print("ERROR - cannot connect db")


################ Get Users ###################

@app.route("/users", methods=["GET"])
def get_users():
    try:
        data = list(db.user.find({"status": 1}))
        for user in data:
            user["_id"] = str(user["_id"])
        print(data)
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json")

    except Exception as e:
        print(e)
        return Response(response=json.dumps({"message": "Can Not Read User"}), status=500, mimetype="application/json")


################ Get User By ID ###################

@app.route("/users/<id>", methods=["GET"])
def get_users_by_id(id):
    try:
        data = list(db.user.find({"_id": ObjectId(id)}))
        for user in data:
            user["_id"] = str(user["_id"])
        print(data)
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json")

    except Exception as e:
        print(e)
        return Response(response=json.dumps({"message": "Can Not Read User"}), status=500, mimetype="application/json")


################ Post Users ###################


@app.route("/add/data", methods=["POST"])
def addData():
    # import pdb
    # pdb.set_trace()
    try:
        requestData = request.json
        # user = {"name": requestData["name"],
        #         "roll_number": requestData["roll_number"], "age": requestData["age"], "status": 1}
        requestData["status"] = 1
        dbResponse = db.user.insert_one(requestData)
        # for attr in dir(dbResponce):
        #     print(attr)
        return Response(
            response=json.dumps(
                {"message": "user created", "id": f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        print(e, "************")

################ Update User ###################


@app.route("/users/update/<id>", methods=["POST"])
def update_user(id):
    try:
        # import pdb
        # pdb.set_trace()
        requestData = request.json
        print(requestData)
        dbResponse = db.user.update_one(
            {"_id": ObjectId(id)}, {"$set": requestData}
        )

        print(dbResponse)
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "User Updated"}),
                status=200,
                mimetype="application/json")
        else:
            return Response(
                response=json.dumps(
                    {"message": "Nothing to Update"}),
                status=500, mimetype="application/json"
            )
    except Exception as e:
        print(e)
        return Response(response=json.dumps({"message": "Can Not Update User"}), status=500, mimetype="application/json")


################ Soft Delete User ###################
@ app.route("/users/delete/<id>", methods=["POST"])
def delete_user(id):
    # import pdb
    # pdb.set_trace()
    print(id)

    try:

        dbResponse = db.user.update_one(
            {"_id": ObjectId(id)}, {"$set": {"status": 0}}
        )
        # dbResponse = db.user.update_one(
        #     {"_id": ObjectId(id)},
        #     {"$set": {"status": 0}}
        # )
        # for attr in dir(dbResponse):
        #     print(f"{attr}")
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "User Updated"}),
                status=200,
                mimetype="application/json")
        else:
            return Response(
                response=json.dumps(
                    {"message": "Nothing to Update"}),
                status=500, mimetype="application/json"
            )
    except Exception as e:
        print(e)
        return Response(response=json.dumps({"message": "Can Not Update User"}), status=500, mimetype="application/json")

# @app.route('/users/<id>', methods=['PATCH'])
# def delete_user(id):
#     try:
#         dbResponse = db.user.update_one(
#             {"_id": ObjectId(id)},
#             {"$set": {"is_deleted.status": 0}}

#         )
#         print(dbResponse)
#         # if dbResponse.is_deleted == 1:
#         return Response(
#             response=json.dumps(
#                 {"message": "User Delete"}),
#             status=200,
#             mimetype="application/json")
#     except Exception as e:
#         print(e)
#         return Response(response=json.dumps({"message": "User Not Found!!!!!!"}), status=500, mimetype="application/json")

        ################ Delete User ###################

        # @app.route("/users/<id>", methods=["DELETE"])
        # def delete_user(id):
        #     try:
        #         print(id)
        #         dbResponse = db.user.find_one_and_update(
        #             {"_id": ObjectId(id)},
        #         )
        #         print(dbResponse)
        #         return Response(
        #             response=json.dumps(
        #                 {"message": "User Delete"}),
        #             status=200,
        #             mimetype="application/json")

        #     except Exception as e:
        #         print(e)
        #         return Response(response=json.dumps({"message": "User Not Found!!!!!!"}), status=500, mimetype="application/json")
        ################ run ###################
if __name__ == "__main__":
    app.run(port=5000, debug=True)
