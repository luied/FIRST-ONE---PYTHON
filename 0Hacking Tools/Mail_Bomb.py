import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.encoders import encode_base64
import os
import re

email = "lui19masterson25@hotmail.com"
mail_to = open("emails.txt").read().strip()

smtp = "smtp-mail.outlook.com"
subject = "BOMB"



def logar():
    with open("emails.txt") as mail_to:
        for i in mail_to:
            global b
            b = i.split("@")[0]
            b = re.sub("[^a-z]"," ",b)
            b = b.title()
            msg = MIMEMultipart()
            msg["From"] = email
            msg["To"] = i
            msg["Subject"] = b
            body = '<div style="box-sizing: border-box; font-family: &quot;Proxima Nova&quot;; margin: 15px 0px 10px; padding: 16px; outline: 0px; font-weight: 300; border-radius: 5px; background-color: rgb(255, 243, 200); color: rgb(170, 135, 73); display: inline-block"><h2 style="box-sizing: border-box; font-family: &quot;Proxima nova&quot;, Arial, Helvetica, &quot;Nimbus Sans L&quot;, sans-serif; margin: 0px; outline: 0px; font-weight: 700; line-height: 1.2">Suspendemos a sua conta</h2>\n\
            <p style="font-family:&quot;Proxima nova&quot;,Arial,Helvetica,&quot;Nimbus Sans L&quot;,sans-serif; margin:10px 0px 0px; outline:0px; font-weight:300; font-size:14px; color:rgb(170,135,73)">\
Foi necessário suspender a sua conta<span>&nbsp;</span><strong style="margin:0px; outline:0px; font-weight:700">porque identificamos um comportamento irregular nas suas negociações.</strong></p>\
            <span style="color: rgb(170, 135, 73); font-family: &quot;Proxima nova&quot;, Arial, Helvetica, &quot;Nimbus Sans L&quot;, sans-serif; font-size: 14px; font-weight: 300; background-color: rgb(255, 243, 200); display: inline !important">Para que possamos reativar a sua conta, por favor,<span>&nbsp;</span></span> <a href="https://www.tomounocu.com.br">contate-nos</a>.</p>\
            <a class="ui-button ui-button--primary restriction-button" href="http://www.tomounocu.com.br">Ir para a Página principal</a>'
            msg.attach(MIMEText(body,"html"))#plain no lugar de html é o default
            file="Mercado Livre.bmp"
            attachment = open(file,"rb")
            part = MIMEBase("application","octet-stream")
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", "attachment; filename= "+file)
            msg.attach(part)
            text = msg.as_string()

            try:
                server = smtplib.SMTP(smtp,587)
                print("\n[+]Conectado-se a "+smtp)
                server.starttls()
                print("[+]Logando como: "+email)
                server.login(email,open("C:"+os.sep+"Users"+os.sep+"Lui19"+os.sep+"pass.txt").read())
                print("[+]Sucesso.\n[+]Enviando email para "+i+"\n")
                try:
                    server.sendmail(email,i,text)
                    print("\n[+]Email enviado com sucesso!\n\nMensagem: "+msg)
                except Exception as e:
                    print(e)
                    print("\n(-)O email pode nao ter sido enviado")
                    server.quit()

            except Exception as e:
                print(e)
                print("(-)Nao foi possivel conectar-se")
        print("Todo o trabalho foi feito.")
#------------------------------------------------------fim

def main():
    logar()

main()
