import yagmail
user = 'schoolattendance3@gmail.com'
app_password = 'uswo oqqv dnqe lvix' # not plain password 
to = 'work.personal0001@gmail.com'
subject = 'test subject 1'
contents = ['mail body content','pytest.ini','test.png']

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, contents)
    print('Sent email successfully')

