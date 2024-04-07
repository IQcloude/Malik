from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    
    #رابط الصوره
    image_url = "https://pin.it/3n1DMpL5f"    
    #الترحيب
    page_title = "Welcome"
    #الوصف
    welcome_message = "مكتب مالك الزيـدي"

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ page_title }}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-color: #260701;
                color: #FFA500;
                text-align: center;
                margin: 0;
                padding: 0;
                font-size: 16px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 0px rgba(255, 255, 255, 0.5);
            }
            h1 {
                margin-top: 20px;
                font-size: 24px;
                text-shadow: 0px 0px 30px #ffffff;
            }
            p {
                font-size: 15px;
                margin-top: 7px;
                margin-bottom: 30px; 
                text-shadow: 1px 1px 2px #333;
                color: #FFFFFF;
            }
            .button {
                padding: 10px 20px;
                margin: 10px;
                border: none;
                cursor: pointer;
                font-size: 18px;
                border-radius: 30px;
                transition: all 0.3s ease;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .button1 {
                background-color: #774936;
                color: #ffffff;
                width: 220px;
                height: 40px;
                padding-left: 25px; 
                text-align: left; 
                background-image: url('https://up6.cc/2023/09/169570616241691.png');
                background-repeat: no-repeat;
                background-size: 40px; 
                background-position: 10px center; 
            }
            .button2 {
                background-color: #774936;
                color: #ffffff;
                width: 190px;
                height: 40px;
                padding-left: 20px; 
                text-align: left; 
                background-image: url('https://up6.cc/2023/09/16957061624633.png');
                background-repeat: no-repeat;
                background-size: 40px; 
                background-position: 10px center; 
            }
            .button3 {
                background-color: #653A2A;
                color: #ffffff;
                width: 160px;
                height: 40px;
                padding-left: 20px; 
                text-align: left; 
                background-image: url('https://up6.cc/2023/09/169570616244282.png');
                background-repeat: no-repeat;
                background-size: 40px; 
                background-position: 10px center; 
            }
            .button4 {
                background-color: #5C3324;
                color: #ffffff;
                width: 130px;
                height: 40px;
                padding-left: 20px; 
                text-align: left; 
                background-image: url('https://up6.cc/2023/09/169570648628541.png');
                background-repeat: no-repeat;
                background-size: 30px; 
                background-position: 10px calc(100% - 8px); 
            }

            .button:hover {
                transform: scale(0.9);
                box-shadow: 0px 0px 20px #555;
                background-color: #260701;
                transition: background-color 0.5s ease;
            }
                   
        </style>
    </head>
    <body>
        <img src="{{ image_url }}" alt="صورة">
        <h1>{{ page_title }}</h1>
        <p>{{ welcome_message }}</p>
        <a href="{{ url_for('button1') }}" class="button button1">I S T A G R A M</a>
        <a href="{{ url_for('button2') }}" class="button button2">TELEGRAM</a>
        <a href="{{ url_for('button3') }}" class="button button3">TIK TOK</a>
        <a href="{{ url_for('button4') }}" class="button button4">YouTube</a>
    </body>
    </html>
    """
    
    return render_template_string(html_template, image_url=image_url, welcome_message=welcome_message, page_title=page_title)


@app.route('/button1')
def button1():
    return redirect("https://wa.me/9647842229883")

@app.route('/button2')
def button2():
    return redirect("https://t.me/MalikH23")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
