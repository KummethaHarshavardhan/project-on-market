import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
url=" http://demo1867978.mockable.io/market_data"
response=requests.get(url)
print(response.status_code)
if response.status_code==200:
    get_data=response.json()
    print(get_data)
else:
    print("not avialable data") 
mydb=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='harsha6281240878',
    database='project market'
)
#print(mydb)
mycursor=mydb.cursor()
def login():
    productname=input("enter  product name: ")
    market_email=input("enter market email: ")
    sql="select*from market_products where productname=%s and market_email=%s" 
    val=(productname,market_email)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result:
        print(f"hi sir! the {productname} are  avilabe")
        def fruits():
            cost=100
            x=int(input("how many dagon you want: "))
            bill=x*cost #bill=100*2=200,
            gst=bill+5*x #gst=200+5*2=210
            total_bill=gst
            var=input("do you want  this product: ")
            if var=="yes":
                sender_email = "harshavardhan6281240878@gmail.com"
                y=input("enter you emil_id : ")
                receiver_email = y
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_bill}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def rice():
            cost=150
            x=int(input("how many kgs you want: "))
            bill=x*cost
            gst=bill+15*x
            total_bill=gst
            var=input("do you want this product: ")
            if var=="yes":
                y=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = y
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_bill}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def sugar():
            cost=40
            x=int(input("how many kgs you want: "))
            bill=x*cost
            gst=bill+2*x
            total_bill=gst
            var=input("do you want this product: ")
            if var=="yes":
                y=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = y
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_bill}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def eggs():
            cost=7
            x=int(input("how many eggs you want: "))
            bill=x*cost
            gst=bill+0.5*x
            total_bill=gst
            var=input("do you want this product: ")
            if var=="yes":
                y=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = y
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_bill}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def bread():
            cost=40
            x=int(input("how many packets you want: "))
            bill=x*cost
            gst=bill+2*x
            total_bill=gst
            var=input("do you want this product: ")
            if var=="yes":
                y=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = y
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_bill}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def seeds():
            cost=60
            x=int(input("how many kgs you want: "))
            bill=x*cost
            gst=bill+5*x
            total_bill=gst
            var=input("do you want this product: ")
            if var=="yes":
                y=input("enter you emil_id : ")
                sender_email = "harshavardhan6281240878@gmail.com"
                receiver_email = y
                password = "okpf axmv octs zvrh"
                subject = "Total Bill"
                body = f"Your total bill is: ${total_bill}"
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            else:
                print("thank you sir!")
        def main():
            z=int(input("enter product number: "))
            if z==1:
                fruits()
            elif z==2:
                rice()
            elif z==3:
                sugar()
            elif z==4:
                eggs()
            elif z==5:
                bread()
            elif z==6:
                seeds()
            else:
                print("not required this product")
        main()                                
    else:
        print("product not available")
login()  
'''output:-
200
{'fruits': 'productnumber-1', 'rice': 'productnumber-2', 'suggar': 'productnumber-3', 'eggs': 'productnumber-4', 'bread': 'productnumber-5', 'pulses': 'productnumber-6'}
enter  product name: rice
enter market email: dmart@gmail.com
hi sir! the rice are  avilabe
enter product number: 2
how many kgs you want: 25
do you want this product: yes
enter you emil_id : harshavardhankummeth@gmail.com
Email sent successfully!'''                      


                


                


                


                        


                


                


                


                        


                


                


                


                        


                


                


                


                        


                


                


                


                        


                


                


                


                