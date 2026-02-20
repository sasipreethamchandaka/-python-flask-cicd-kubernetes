from flask import Flask, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pawan Kalyan Career</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body{
            background:#f4f4f4;
        }

        header{
            background:#111;
            color:#fff;
            padding:20px;
            text-align:center;
        }

        header h1{
            font-size:28px;
            letter-spacing:2px;
        }

        nav{
            background:#d32f2f;
            padding:10px;
            text-align:center;
        }

        nav a{
            color:#fff;
            text-decoration:none;
            margin:0 15px;
            font-weight:bold;
        }

        .hero{
            height:80vh;
            background:url('https://wallpaperaccess.com/full/2703651.jpg') no-repeat center center/cover;
            display:flex;
            justify-content:center;
            align-items:center;
            color:#fff;
            text-align:center;
        }

        .hero h2{
            font-size:40px;
            background:rgba(0,0,0,0.6);
            padding:20px;
        }

        .section{
            padding:50px 20px;
            text-align:center;
        }

        .section h2{
            margin-bottom:20px;
            color:#d32f2f;
        }

        .career-box{
            display:flex;
            justify-content:center;
            flex-wrap:wrap;
            gap:20px;
        }

        .card{
            background:#fff;
            width:280px;
            padding:20px;
            border-radius:8px;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
        }

        .card h3{
            margin-bottom:10px;
            color:#111;
        }

        .card p{
            font-size:14px;
            color:#555;
        }

        footer{
            background:#111;
            color:#fff;
            text-align:center;
            padding:15px;
            margin-top:30px;
        }

        .btn{
            display:inline-block;
            margin-top:15px;
            padding:10px 20px;
            background:#d32f2f;
            color:#fff;
            text-decoration:none;
            border-radius:5px;
        }

        .btn:hover{
            background:#b71c1c;
        }
    </style>
</head>

<body>

<header>
    <h1>Pawan Kalyan Career Journey</h1>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">Film Career</a>
    <a href="#">Political Career</a>
    <a href="#">Achievements</a>
</nav>

<section class="hero">
    <h2>Power Star Pawan Kalyan</h2>
</section>

<section class="section">
    <h2>Film Career</h2>
    <div class="career-box">
        <div class="card">
            <h3>Debut</h3>
            <p>Started film career with Akkada Ammayi Ikkada Abbayi (1996).</p>
        </div>

        <div class="card">
            <h3>Blockbusters</h3>
            <p>Tholi Prema, Gabbar Singh, Attarintiki Daredi, Vakeel Saab.</p>
        </div>

        <div class="card">
            <h3>Fan Base</h3>
            <p>One of the most influential actors in Telugu cinema.</p>
        </div>
    </div>
</section>

<section class="section">
    <h2>Political Career</h2>
    <div class="career-box">
        <div class="card">
            <h3>Jana Sena Party</h3>
            <p>Founded Jana Sena Party in 2014 to serve people.</p>
        </div>

        <div class="card">
            <h3>Public Service</h3>
            <p>Actively working for youth empowerment and social justice.</p>
        </div>
    </div>

    <a href="#" class="btn">Learn More</a>
</section>

<footer>
    © 2026 Pawan Kalyan Career Website | Designed by You
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
