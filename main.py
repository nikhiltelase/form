from flask import Flask, render_template, request
import requests as sheet
import smtplib

app = Flask(__name__)
api_url = "https://dashboard.sheety.co/projects/65d06017ec339004d7c680dc/sheets/sheet1"

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['fullName']
    email = request.form['email']
    mobile = request.form['mobile']
    message = request.form['message']
    # saving data into google sheet
    data = {
        'sheet1': {
            'name': name,
            'email': email,
            'mobile': mobile,
            'message': message,
        }
    }
    sheet.post("https://api.sheety.co/06611c666efcc4e05beb6ca9c244f4fa/visitors/sheet1", json=data)


    # sending mail
    # my_email = "nikhiltelase17@gmail.com"
    # password = "qyhtmfnyyebfayqz"
    # to_mail = email
    # mail_message = f"Subject: Thankyou \n\nThankyou {name} visiting my web.\nI will contact soon.\nYour message if valuble for me"
    #
    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()  # seure
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(from_addr=my_email,
    #                         to_addrs=[to_mail],
    #                         msg=mail_message)
    return render_template("thankyou.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
