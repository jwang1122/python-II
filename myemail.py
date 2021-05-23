import yagmail

yagmail.register('jwang1122@gmail.com', 'Qianjiang@1122')

yag = yagmail.SMTP('jwang1122@gmail.com')

to = 'wangqianjiang@live.com'
subject = 'Quite the subject line'
body = 'Pretty sure this is the body.'

yag.send(to = [to], subject=subject, contents=body)

print("Email sent successfully.")