import pyrebase
def senddata(a):
    config={
        "apiKey": "AIzaSyCMdwsdzWycUH_WVbkG9RRfIEadWazLaIo",
        "authDomain": "homeautomation-ddfdd.firebaseapp.com",
        "databaseURL": "https://homeautomation-ddfdd-default-rtdb.firebaseio.com",
        "projectId": "homeautomation-ddfdd",
        "storageBucket": "homeautomation-ddfdd.appspot.com",
        "messagingSenderId": "587715575052",
        "appId": "1:587715575052:web:6e2d075cb4e846bd21dd29",
        "measurementId": "G-YYKQMGCPCG"
        }
    firebase= pyrebase.initialize_app(config)
    database=firebase.database()
    users=database.child("pc message").set(str(a))

def getdata():
    import pyrebase
    config={
          "apiKey": "AIzaSyCMdwsdzWycUH_WVbkG9RRfIEadWazLaIo",
          "authDomain": "homeautomation-ddfdd.firebaseapp.com",
          "databaseURL": "https://homeautomation-ddfdd-default-rtdb.firebaseio.com",
          "projectId": "homeautomation-ddfdd",
          "storageBucket": "homeautomation-ddfdd.appspot.com",
          "messagingSenderId": "587715575052",
          "appId": "1:587715575052:web:6e2d075cb4e846bd21dd29",
          "measurementId": "G-YYKQMGCPCG"
        }
    firebase= pyrebase.initialize_app(config)
    database=firebase.database()
    users=database.child("pc message").get()
    msg=users.val()
    return msg

def returnmsgtopc(a):
    config={
        "apiKey": "AIzaSyCMdwsdzWycUH_WVbkG9RRfIEadWazLaIo",
        "authDomain": "homeautomation-ddfdd.firebaseapp.com",
        "databaseURL": "https://homeautomation-ddfdd-default-rtdb.firebaseio.com",
        "projectId": "homeautomation-ddfdd",
        "storageBucket": "homeautomation-ddfdd.appspot.com",
        "messagingSenderId": "587715575052",
        "appId": "1:587715575052:web:6e2d075cb4e846bd21dd29",
        "measurementId": "G-YYKQMGCPCG"
        }
    firebase= pyrebase.initialize_app(config)
    database=firebase.database()
    users=database.child("return pc message").set(str(a))

