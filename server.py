from express_server import express
import db
import glob

app = express()
dbcon = db.connect_db()

def saymyname(req, res, next):
    print(req.query.name)

    asdsadkj = ("asdas", 1232, False)
    return res.json({ "first": asdsadkj[1],   })


# /search?drink_name=...
def seach_handler(req, res, next):
    drink_name = req.query.drink_name #henter drink navnet som brugeres har søgt på
    search_result = db.seach(dbcon, drink_name) #finder brugeres resultat
    return res.json(search_result)

def get_recipe_requesthandler(req, res, next):
    drink_id = req.query.drink_id
    recipies = db.get_recipe(dbcon, drink_id)
    return res.json(recipies)



def createrecipe(req, res, next):
    db.create_recipe()
    print(req.query.name)

    asdsadkj = ("asdas", 1232, False)
    return res.json({ "first": asdsadkj[1],   })

def home(req, res, next):
    return res.sendfile("public/index.html")

def static_files(req, res, next):
    file_path = f"public{req.url}"
    return res.sendfile(file_path)

app.get("/", home)
app.get("/get-drink", get_recipe_requesthandler)
app.get("/get-drink", seach_handler)
app.get("/*", static_files)

app.listen(3000)