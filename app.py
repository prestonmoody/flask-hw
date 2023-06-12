from flask import Flask
# some bits of text for the page.
html = '''
<html>
<head>
<title>Simple Flask Application</title>
</head>
<body>
<h1>Simple Flask app Home page!</h1>
</body>
</html>
'''
application = Flask(__name__)
application.add_url_rule('/', 'index', (lambda:html))
 
if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=5000)