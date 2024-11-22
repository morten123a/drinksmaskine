from express_server import express
import db #henter vores database request-handler
#import glob        Dette er vist ikke vigtigt
import json

app = express()
dbcon = db.connect_db() #giver vores forbindelse et andet navn

def seach_handler(req, res, next):
    drink_name = req.query.search#henter drink navnet som brugeres har søgt på
    search_result = db.seach(dbcon, drink_name) #finder brugeres resultat
    return res.json(search_result) #sender resultatet tilbage til brugeren


def filter_handler(req, res, next):
    filter_req = json.loads(req.query.filter)
    filter = db.get_recipes_by_included_ingredients(dbcon, filter_req)
    return res.json(filter)

def home(req, res, next): #default siden
    return res.sendfile("public/index.html")

def static_files(req, res, next): #gør det nemmere at hente filer for clienten
    file_path = f"public{req.url}" #fortæller frontenden at vi bruger "public" som deafult directory
    return res.sendfile(file_path) #sender det til brugeren

#fortæller backenden hvilket directory der skal køre den respektive function
app.get("/", home)
app.get("/search", seach_handler)
app.get("/mydrinks_filter", filter_handler)
app.get("/*", static_files)

app.listen(3000)