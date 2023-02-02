from pymongo import MongoClient
from dotenv import dotenv_values
import time
import numpy as np
config = dotenv_values(".env")

client = MongoClient(config["DB_IP"])

def display_temps_acces(client):
    db = client["France"]
    collection = db["communes"]

    # Recherche par nom de ville
    ville = "Annecy"
    start_time = time.time()
    document = collection.find_one({"nom_communes": ville})
    end_time = time.time()

    # Calcul du temps nécessaire pour lire le document
    time_elapsed = end_time - start_time
    print("Temps nécessaire pour lire le document : ", time_elapsed, "seconds.")
display_temps_acces(client)
# all_communes = collection.find({}, {"nom_commune": 1, "_id": 0}, limit=100)
# time_elapsed=[]
# for commune in all_communes:
#     start_time = time.time()
#     document = collection.find_one({"nom_commune": commune["nom_commune"]})
#     end_time = time.time()

#     time_elapsed.append(end_time-start_time)
# print("Temps moyen pour lire le document", np.mean(time_elapsed))
# # Calcul du temps nécessaire pour lire le document

#db.mailing.updateOne({_id:ObjectId("63dbb600caccc52eadff32c1")},{$push:{emails:"a_new_test@gmail.com"}})

#db.lists.updateOne({_id:ObjectId("63dbb7d2caccc52eadff32c9")},{$push:{emails:"etienne.malc@gmail.com"}})

def display_mailing_list(client: MongoClient):
    db = client["mailing"]
    lists_collection = db["lists"]
    users_collection = db["users"]
    all_lists = lists_collection.find({})
    
    for l in all_lists:
        for user_id in range(len(l["users"])):
            l["users"][user_id] = users_collection.find_one({"_id": l["users"][user_id]})
        print(l)

display_mailing_list(client)
