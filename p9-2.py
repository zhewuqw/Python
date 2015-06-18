from wsgiref.simple_server import make_server
import sqlite3

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

def hello_world_app(environ, start_response):
    conn = sqlite3.connect("zoo.sqlite")
    cursor = conn.cursor()

    #print("ENVIRON:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)


    if(environ['REQUEST_METHOD'] == 'POST'):
        message += "<br>Your data has been recorded:"
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        form_vals = get_form_vals(request_body)

        cursor.execute("INSERT INTO animal_count(name, count) VALUES (?, ?)",
                       (form_vals["animal"], form_vals["count"]) )

        for item in form_vals.keys():
            print (item + ": " + form_vals[item])
            message += "<br/>"+item + " = " + form_vals[item]

    message += "<h1>Welcome to the Zoo</h1>"
    message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
    message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"

    conn.commit()
    conn.close()

    return [bytes(message, 'utf-8')]



httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()


#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled13/p9-2.py
#Serving on port 8000...
#127.0.0.1 - - [18/Jun/2015 16:17:11] "GET / HTTP/1.1" 200 184
#Submit: Submit+Query
#127.0.0.1 - - [18/Jun/2015 16:17:16] "POST / HTTP/1.1" 200 274
#count: 11
#animal: cat
