from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return '''
<html>
<head></head>
<body>
<h1>Hello World</h1>
<p>
<a href="/vacation">vacation</a>
</p>

</body>
</html>
'''

@app.route("/vacation")
def vacation():
    return '''
<html>
<head></head>
<body>
<h1>You Are on Vacation</h1>
<p> 
<a href="/">home page</a>
</p>
</body>
</html>
'''