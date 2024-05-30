# Flask Contact Form Project

## Overview

This project is a simple Flask web application for a contact form. Users can input their name, email, mobile number, and a message through the form. Upon submission, the data is saved to a Google Sheet using Sheety API, and a confirmation email is sent to the user. 

## Files

- `app.py`: This file contains the Flask application code. It includes routes for rendering the home page, submitting the form, and handling redirection.
- `index.html`: The HTML template for the home page containing the contact form.
- `thankyou.html`: The HTML template for the thank you page displayed after form submission.

## Dependencies

- Flask: A micro web framework for Python.
- Requests: A Python HTTP library for sending HTTP requests.
- smtplib: A built-in Python library for sending emails.

## Setup

1. Clone the repository to your local machine:

```
git clone https://github.com/nikhiltelase17/form.git
```

2. Install the required dependencies:

```
pip install flask requests
```

3. Update the `my_email` and `password` variables in `app.py` with your Gmail credentials. Ensure that you enable less secure app access or use app-specific passwords if you have two-factor authentication enabled on your Gmail account.

4. Run the Flask application:

```
python app.py
```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Visit the home page of the application.
2. Fill out the contact form with your name, email, mobile number, and message.
3. Click on the submit button.
4. You will be redirected to a thank you page, and a confirmation email will be sent to the provided email address.
5. Data submitted through the form will be saved to a Google Sheet using Sheety API.

## Notes

- Ensure that you have an internet connection to access the Sheety API and send emails.
- This project is for demonstration purposes and may require further enhancements for production use, such as error handling, validation, and security improvements.

## Credits

- This project was created by Nikhil.

## License

This project is licensed under the [MIT License](LICENSE).
