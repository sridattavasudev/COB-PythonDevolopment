import smtplib

sender_email = "thebrainiac20@gmail.com"
receiver_email = input("Enter receiver email: ")
password = "rnrz wrrv wybd yewc"
msg = input("Enter the message you want to send: ")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    print("Logged in successfully")
    server.sendmail(sender_email, receiver_email, msg)
    print("Successfully sent")
except smtplib.SMTPException as error:
    print(f"An error occurred: {error}")
finally:
    server.quit()
