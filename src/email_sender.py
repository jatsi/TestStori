import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject: str, transaction_data: str, from_email: str, to_email: str, smtp_server, smtp_port: int, smtp_username: str, smtp_password: str):
    """
    Function to send an email with transaction summary.

    Args:
    subject (str): Subject of the email.
    transaction_data (str): Transaction data in HTML format.
    from_email (str): Sender's email address.
    to_email (str): Recipient's email address.
    smtp_server: SMTP server address.
    smtp_port (int): SMTP server port.
    smtp_username (str): SMTP server username.
    smtp_password (str): SMTP server password.
    """
    # Construct HTML content dynamically with transaction data
    html_content = generate_html_content(subject, transaction_data)

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach HTML content with inline CSS
    msg.attach(MIMEText(html_content, 'html'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
 

def generate_html_content(subject: str, transaction_data: dict) ->str:
    """
    Function to generate HTML content for the email body.

    Args:
    subject (str): Subject of the email.
    transaction_data (dict): Dictionary containing transaction data.

    Returns:
    str: HTML content for the email body.
    """
    # HTML template with inline CSS
    html_content = f"""
    <!doctype html>
    <html lang="en-US">
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
        <title>Stori Transaction Summary</title>
        <meta name="description" content="Stori Transaction Summary Email Template.">
        <style type="text/css">
            a:hover {{text-decoration: underline !important;}}
            .logo img {{
                width: 40%; 
                height: auto; 
                max-width: 50px; 
            }}
        </style>
    </head>
    <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
        <!--100% body table-->
        <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8" style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
            <tr>
                <td>
                    <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
                        <tr>
                            <td style="height:80px;">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="text-align:center;">
                            <a href="https://www.storicard.com/" title="logo" target="_blank">
                                <img width="150" src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Stori_Logo_2023.svg" title="logo" alt="logo">
                            </a>
                            </td>
                        </tr>
                        <tr>
                            <td style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                            <td>
                                <table width="95%" border="0" align="justify" cellpadding="0" cellspacing="0" style="max-width:670px;background:#fff; border-radius:3px; -webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                    <tr>
                                        <td style="height:40px;">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td style="padding:0 35px;">
                                        <div style=" text-align:center;">
                                            <h1 style="color:#1e1e2d; text-align:center; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">{subject}</h1>
                                            <span style=" display:inline-block; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                        </div>
                                        <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">Total balance is {transaction_data["total_balance"]}</p>
        """
        # Append transaction data for each month
    for month, num_transactions in transaction_data["transactions_by_month"].items():
            html_content += f"""<p style="color:#455056; font-size:15px;line-height:24px; margin:0;">Number of transactions in {month}: {num_transactions}</p>"""

        # Append average debit and credit amounts
    html_content += f"""
                    <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">Average debit amount: {transaction_data["average_debit"]}</p>
                    <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">Average credit amount: {transaction_data["average_credit"]}</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="height:40px;">&nbsp;</td>
                                    </tr>
                                </table>
                            </td>
                        <tr>
                            <td style="height:20px;">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="text-align:center;">
                                <p style="font-size:14px; color:rgba(69, 80, 86, 0.7411764705882353); line-height:18px; margin:0 0 0;">&copy; <strong>www.storicard.com</strong></p>
                            </td>
                        </tr>
                        <tr>
                            <td style="height:80px;">&nbsp;</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        <!--/100% body table-->
    </body>
    </html>
    """
    return html_content
