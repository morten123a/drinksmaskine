from express_server import express
import db
import glob

app = express()
##dbcon = db.connect_db()

def saymyname(req, res, next):
    print(req.query.name)

    asdsadkj = ("asdas", 1232, False)
    return res.json({ "first": asdsadkj[1],   })

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
app.get("/*", static_files)

app.listen(3000)