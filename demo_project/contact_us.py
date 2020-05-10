from flask import Flask, render_template, request
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='your email address'
app.config['MAIL_PASSWORD']= 'your email password'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail = Mail(app)

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.form,
    ))
  
@app.route("/")
def student():
   return render_template("contact_us.html")


@app.route("/contactus", methods=["POST"])
def sendContactEmail():
    if request.method == "POST":
        result = request.form
        info = render_template('result.html', result=result)
        
        contact_name = request.form.getlist('name')[0]
        contact_email=request.form.getlist('email')[0]
        contact_desc= request.form.getlist('Description')[0]
        
        msg = Message("New contact enquiry - from - %s"%contact_name, sender="wadhwani.deep52@gmail.com", recipients = ["wadhwani.deep52@gmail.com","wadhwani.suman@gmail.com"])
        
        msg.body = "name:"+contact_name + "\nemail:"+contact_email + "\ndesc:"+contact_desc
        msg.html = render_template('result.html', result = result)
        mail.send(msg)
        print(info)
        #print(contact_name,contact_email,contact_desc)
        return result

if __name__ == '__main__':
   app.run(debug = True)

