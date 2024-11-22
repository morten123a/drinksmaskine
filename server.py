from express_server import express
import db
import glob
import json

app = express()
dbcon = db.connect_db()

# /search?drink_name=...
def seach_handler(req, res, next):
    try:
        drink_name = req.query.search#henter drink navnet som brugeres har søgt på
        search_result = db.seach(dbcon, drink_name) #finder brugeres resultat
        return res.json(search_result)
    except Exception as e:
        print(e.with_traceback())
        return res.json({ "ok": False, "msg": "server error" })

def filter_handler(req, res, next):
    filter_req = json.loads(req.query.filter)
    filter = db.get_recipes_by_included_ingredients(dbcon, filter_req)
    print(filter)
    return res.json(filter)

def home(req, res, next):
    return res.sendfile("public/index.html")

def static_files(req, res, next):
    file_path = f"public{req.url}"
    return res.sendfile(file_path)

app.get("/", home)
app.get("/search", seach_handler)
app.get("/mydrinks_filter", filter_handler)
app.get("/*", static_files)

app.listen(3000)