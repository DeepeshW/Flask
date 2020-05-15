from flask import Flask 
from flask_mail import Mail,Message

app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='YourEmailID'
app.config['MAIL_PASSWORD']= 'YourEmailPassword'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message("Hello This is flask-mail test.", sender="SenderEmailID", recipients = ["RecipientsEmailID","RecipientsEmailID"])
    # for multiple recipients add recipients email ids in a list as above
    msg.body = "Hello flask message sent from flask-Mail"
    mail.send(msg)
    return "sent"

if __name__ == '__main__':
    app.run(debug=True)
    
