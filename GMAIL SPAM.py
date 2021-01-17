# coding: utf-8
# -*-coding:Latin-1 -*
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from getpass import getpass
import socket 
#NEW FEATURE VERIFIER SI IL EST CONNECTE A INTERNET#
autorisation=0
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("Avez vous autorisez Votre gmail a être utiliser par des applications tierces")
print("SI oui TAPER 1")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("SI non TAPER 2")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
print("                                 ")
autorisation=int(input("Choisissez entrez 1 ou 2 :"))

if autorisation==1 :

    print("vous pouvez utilisez SPAMM ACCOUNT")
    nombre_de_mail_envoyé = 0
    Estimation_du_temps = 0


    email = str(input("saisir votre adresse mail :"))
    print("                                 ")
    print("                                 ")
    print("                                 ")
    adresse_mail_de_la_victime = str(input("saisir l'adresse mail de la victime : "))
    print("                                 ")
    print("                                 ")
    print("                                 ")
    mdp = getpass("saisir votre  mot de passe : ")
    print("                                 ")
    print("                                 ")
    objet = str(input("saisir l'objet du mail : "))
    print("                                 ")
    print("                                 ")
    print("                                 ")
    corps = str(input("saisir le corps du mail : "))
    print("                                 ")
    print("                                 ")
    print("                                 ")
    nombre_de_message_a_envoyé = int(input("saisir le nombre de message a envoyé : "))
    print("                                 ")
    print("                                 ")
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
    print   ("            PRGM FAIT PAR GEORGES KIPS#KGE           ")
    webbrowser.open("https://www.youtube.com/channel/UCE1JBg4bH1HTRUtWAvKBn0Q/about")



                                                                                                                                     
