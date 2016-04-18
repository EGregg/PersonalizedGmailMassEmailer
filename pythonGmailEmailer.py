#!/usr/bin/python
#created by egregg 041816

import getpass
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os

#set the Gmail login info here so that it will not have to be entered every time the script is ran
gmail_user = "ENTER IN YOUR EMAIL ADDRESS HERE"
gmail_pwd = "ENTER IN THE PASSWORD ASSOCIATED WITH EMAIL ADDRESS HERE"

#set the subject to be in every email here
email_subject = "ENTER IN THE SUBJECT HERE"

#set the email to be cc'd on every email here
email_cc = "ENTER IN CC ADDRESSES HERE OR LEAVE BLANK"

#set the location of the file with the message that will be sent, here. 
#if the file is in the same directory as the script, the name of the file will be sufficient with extension.
personalization_file = open('genericPersonalization.txt')

#the email_body can be changed, to a string but currently I had it reading from a message file and inserting elements from another file to personalize the emails
#email_body = IF HARD SETTING HERE, PLEASE COMMENT OUT THE email_body VARIABLE IN THE complete()
message_file = open('genericMessage.txt')

#for text attachments
#attach = "genericTEXT.txt"

#for picture attachments, the location of the file needs to be specified for windows (i.e. you can still use \)
#or you can put the name of the file with extension in the same directory as this script
pictureAttachment = "genericIMAGE.jpg"

#for picture attachments, the location of the file needs to be specified for windows (i.e. you can still use \)
#or you can put the name of the file with extension in the same directory as this script
secondaryPictureAttachment = "genericPDF.pdf"

#function made so that if the user would like to see the info being inserted into each email on one line
def info():
    with personalization_file as fp:
        for line in fp:
            print (line)
            global firstElem, secondElem, thirdElem
            firstElem = (line.split(',')[0]).strip()
            secondElem = (line.split(',')[1]).strip()
            thirdElem = (line.split(',')[2]).strip()
            
def readMessage():
    with message_file as myfile:
        global data
        data=myfile.read() #% (firstElem, secondElem)
        return data
    
def login(user):
   global gmail_user, gmail_pwd
   gmail_user = user
   #gmail_pwd = getpass.getpass('Password for %s: ' % gmail_user)

def mail(to_addr, subject, text, cc):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = to_addr
   msg['CC'] = cc
   msg['Subject'] = subject
   
   #This attaches an image file to the email
   img_data = open(pictureAttachment, 'rb').read()
   image = MIMEImage(img_data, name=os.path.basename(pictureAttachment))
   msg.attach(image) 
   
   #PDFs may be attached with MIMEapplication
   pdfAttachment_data = open(secondaryPictureAttachment, 'rb').read()
   pdf = MIMEApplication(pdfAttachment_data, name=os.path.basename(secondaryPictureAttachment))
   msg.attach(pdf)
   
   #This uses the variable text, to be the body of your message
   msg.attach(MIMEText(text, 'html'))
   
   #this is the part that controls the sending, DO NOT EDIT
   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   
   #sending using SMTP you have to merge the TO, CC, and BCC into one list of strings file
   complete_send = [to_addr, cc]
   
   #format for .sendmail is (user login info, who it's being sent to, details of the message including header)
   mailServer.sendmail(gmail_user, complete_send, msg.as_string())
   mailServer.close()

#this function will process everything and send to all individuals in the personalization_file
def proceedTosend():
    #You can either have this as a fixed email like I have set, or have them input their address each time
   #email = gmail_user #input("Your Gmail address: ")
   #login(email)
   with personalization_file as fp:
        for line in fp:
            readMessage()
            print (line)
            global firstElem, secondElem, thirdElem
            firstElem = (line.split(',')[0]).strip()
            secondElem = (line.split(',')[1]).strip()
            thirdElem = (line.split(',')[2]).strip()
            
            #as it is, I have the third element in the personalization_file to be the email address 
            email_to = thirdElem
            email_body = data % (firstElem, secondElem)
            print(email_body)
            mail(email_to, email_subject, email_body, email_cc)

proceedTosend()
