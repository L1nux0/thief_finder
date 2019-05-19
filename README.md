# thief_finder

This Python 3.7.3 script is design to work on windows after make it a .exe file with Pyinstaller.
The idea behind is create a 'Guest' user without authentication, with this program running, to be used 
for the person who steals our computer!!! Once he connects to internet we will receive every five minutes
his IP address (obtained with the Web https://ip-api.com), a screenshot and you can choose to take pics with
web-cam if your computer has one. That info will be sent using a Gmail account with "allow less secure
 applications" activated.  
 
 Instructions:
 
 Generate a exe file place it in the folder of your choice and to gain persistence you have to make a 
 Shortcut to your file, place it in the next route (W10):
 C:\Users\( your guest user)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ . 
