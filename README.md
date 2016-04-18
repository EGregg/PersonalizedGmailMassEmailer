# PersonalizedGmailMassEmailer

### Developed using python 3.5x

### Developed for a user to send out many emails from a designated Gmail account, with the same body but with a few details changed to personalize it for each recipient.

<strong> Contents: </strong> <br>
genericIMAGE.jpg<br>
genericMessage.txt<br>
genericPDF.pdf<br>
genericPersonalization.txt<br>
pythonGmailEmailer.py<br>

<strong> Directions:</strong> <br>
Place all files into the same directory.

Under account settings in Gmail, Sign-in & Security set Allow less secure apps: ON.

Edit pythonGmailEmailer.py variables gmail_user and gmail_pwd to be the user name and password to login.

Run $pythonGmailEmailer.py from command line.

Running pythonGmailEmailer.py will attempt to attach genericPDF.pdf and genericIMAGE.jpg. pythonGmailEmailer.py will read line by line from genericPersonalization.txt and split each line into 3 indices, the first 2 will be substituted into the email message, the third index from a line will be the intended recipient. pythonGmailEmailer.py will read genericMessage.txt and insert the text from that file into the body of the email.
