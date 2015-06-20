#******************************************************************************#
# The Python Hackathon Project                                                 #
#                                                                              #
# The website is used to listen the customer feedback and save the movie's     #
#  feedback into database.                                                     #
#*******************************************************************************

from wsgiref.simple_server import make_server
import sqlite3

#at the first time to create database and table
#conn = sqlite3.connect("move.sqlite")
#cursor = conn.cursor()
#cursor.execute("create table feedback(username text,movename text, stars integer)")

#conn.commit()
#conn.close()
def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

def hello_world_app(environ, start_response):
    conn = sqlite3.connect("move.sqlite")
    cursor = conn.cursor()

    #print("ENVIRON:", environ)
    message = ""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)

    message += "<h1>Welcome to the movie feedback!</h1>"
    message += "<table><img src = 1.png></table>"
    message += "<h2><font color= green >Inside_Out</h2>"
    message += "<table><font color= black ><tr> After young Riley is uprooted from her Midwest life and moved to San Francisco, " \
               "her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate " \
               "a new city, house and school.</tr><br />" \
               "<tr><font color= green >Directors:</tr><tr><font color= black > Pete Docter, Ronaldo Del Carmen</tr><br />" \
               "<tr><font color= green >Writers:</tr><tr><font color= black > Pete Docter (story), Ronaldo Del Carmen (story)</tr><br />" \
               "<tr><font color= green >Stars:</tr><tr><font color= black > Amy Poehler, Bill Hader, Lewis Black | See full cast and crew  </tr></table><br />"

    message += "<h2><font color= green >Dope</h2>"
    message += "<table><font color= black ><tr> Life changes for Malcolm, a geek who's surviving life in a tough neighborhood, " \
               "after a chance invitation to an underground party leads him and his friends into a Los Angeles adventure.</tr><br />" \
               "<tr><font color= green >Director:</tr><tr><font color= black >Rick Famuyiwa</tr><br />" \
               "<tr><font color= green >Stars:</tr><tr><font color= black > Shameik Moore, Tony Revolori, Kiersey Clemons, Kimberly Elise </tr></table><br />"

    message += "<h2><font color= green >Infinitely_Polar_Bear</h2>"
    message += "<table><font color= black ><tr>A manic-depressive mess of a father tries to win back his wife by attempting to take full responsibility " \
               "of their two young, spirited daughters, who don't make the overwhelming task any easier.</tr><br />" \
               "<tr><font color= green >Director:</tr><tr><font color= black >Maya Forbes</tr><br />" \
               "<tr><font color= green >Stars:</tr><tr><font color= black >Mark Ruffalo, Zoe Saldana, Imogene Wolodarsky, Ashley Aufderheide </tr></table><br />"

    message += "<form method='POST'><br>YourName:<input type=text name='username'>"
    message += "<br><br>MovieName:<input type=text name='movename'>"
    message += "<br><br>Stars:<input type=text name='stars'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"

    if(environ['REQUEST_METHOD'] == 'POST'):
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        form_vals = get_form_vals(request_body)

        cursor.execute("INSERT INTO feedback(username, movename, stars) VALUES (?, ?, ?)",
                       (form_vals["username"], form_vals["movename"], form_vals["stars"]) )

        result = cursor.execute("select * from feedback")
        message += "<br/><h1>People Feebdack</h1><br/>"
        for item in result:
            message += "<br/>Name:  "
            for i in item:
                message += " " +str(i) + " "
        conn.commit()
        conn.close()

    return [bytes(message, 'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()



