"""
PyArt by JustJeeCode 

- User needs to create their artwork
- Then the art gets printed or emailed
"""
import smtplib
from email.message import EmailMessage
import emailDetails

# Erasing content from the file
def clear_pyart():
    pyArt = open('pyart.txt', 'r+')
    pyArt.truncate(0)
    pyArt.close()

clear_pyart()

# Opening file
pyArt = open("pyart.txt", "w+")

# Pyart title screen
print(" _____                     _")   
print("|  __ \         /\        | |")
print("| |__) |   _   /  \   _ __| |_")
print("|  ___/ | | | / /\ \ | '__| __|")
print("| |   | |_| |/ ____ \| |  | |_")
print("|_|    \__, /_/    \_\_|   \__|")
print("       __/ /                   ")
print("      |___/                    ")
print("Made by JustJee")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("When you finish your artwork enter [done]")
print("")

finishedArt = False

# Drawing
while finishedArt == False:
    draw = input(">>> ")

    if draw == "[done]":
        finishedArt = True
        sendArt = input("\nWould you like to [p]rint or [e]mail your artwork >>> ")
        if sendArt == "p" or "P" or "print":
            pass
        elif sendArt == "e" or "E" or "email":
            email = input("\nPlease enter your email (NOTE: It has to be a gmail account): ")

            try:
                EMAIL_ADRESS =  emailDetails.EMAIL_ADDRESS
                EMAIL_PASSWORD = emailDetails.EMAIL_PASSWORD

                msg = EmailMessage()
                msg['Subject'] = 'Shopping List!'
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = email
                msg.set_content('Here is your Art Work...')

                with open('pyart.txt', 'rb') as f:
                    file_data = f.read()
                    file_name = f.name

                msg.add_attachment(file_data, maintype='txt', subtype='txt', filename=file_name)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                    smtp.send_message(msg)

                print("\nEmail Sent!")
            except:
                print("\nError, Email failed to send!")
        break

    else:
        pyArt.write(draw)
        pyArt.write("\n")

