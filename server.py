from express_server import express
import db
import glob
import json

app = express()
dbcon = db.connect_db()

# /search?drink_name=...
def seach_handler(req, res, next):
    drink_name = req.query.drink_name #henter drink navnet som brugeres har søgt på
    search_result = db.seach(dbcon, drink_name) #finder brugeres resultat
    return res.json(search_result)

def filter_handler(req, res, next):
    filter_req = json.loads(req.query.filter)
    filter = db.filter(dbcon, filter_req)
    return res.json(filter)

# /search?drink_name=...
def seach_handler2(req, res, next):
    drink_name = req.query.drink_name #henter drink navnet som brugeres har søgt på
    search_result = db.seach(dbcon, drink_name) #finder brugeres resultat
    return res.json(search_result)


def home(req, res, next):
    return res.sendfile("public/index.html")

def static_files(req, res, next):
    file_path = f"public{req.url}"
    return res.sendfile(file_path)

app.get("/", home)
app.get("/index", seach_handler)
app.get("/mydrinks_filter", filter_handler)
app.get("/mydrinks_seach", seach_handler2)
app.get("/*", static_files)

app.listen(3000)