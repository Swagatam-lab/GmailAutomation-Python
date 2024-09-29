import smtplib as s 

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('xyz123@gmail.com','password')
subject="Testing Gmail Automation  python"
body="I Love Python"
massage="subject:{}\n\n{}".format(subject,body)
listadd=['xya12323@gmail.com',
         "xya1235@gmail.com"]
ob.sendmail('xyz123@gmail.com',listadd,massage)
print("send mail")
ob.quit