# coding: utf-8
# -*-coding:Latin-1 -*
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from getpass import getpass
import socket 

autorisation=0
for i in range(1,6):
    print("                                 ")
print("Avez vous autorisez Votre gmail a être utiliser par des applications tierces")
print("SI oui TAPER 1")
for i in range(1,6):
    print("                                 ")
print("SI non TAPER 2")
for i in range(1,6):
    print("                                 ")
autorisation=int(input("Choisissez entrez 1 ou 2 :"))

if autorisation==1 :

    print("vous pouvez utilisez SPAMM ACCOUNT")
    nombre_de_mail_envoyé = 0
    Estimation_du_temps = 0


    email = str(input("saisir votre adresse mail :"))
    for i in range (1,3):
        print("                                 ")
    adresse_mail_de_la_victime = str(input("saisir l'adresse mail de la victime : "))
    for i in range (1,3):
        print("                                 ")
    mdp = getpass("saisir votre  mot de passe : ")
    for i in range (1,2):
        print("                                 ")
    objet = str(input("saisir l'objet du mail : "))
    for i in range (1,2):
        print("                                 ")
    corps = str(input("saisir le corps du mail : "))
    for i in range (1,2):
        print("                                 ")
    nombre_de_message_a_envoyé = int(input("saisir le nombre de message a envoyé : "))
    for i in range (1,2):
        print("                                 ")
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
        print("Message n°",nombre_de_mail_envoyé,"envoyé avec succès")
    webbrowser.open("https://www.youtube.com/channel/UCE1JBg4bH1HTRUtWAvKBn0Q/about")

else:
    print("Vous ne pouvez pas utilisez SPAMM ACCOUNT")
    for i in range (1,10):
        print("-----------------------------------------------------------")
    
    webbrowser.open("")



                                                                                                                                     
