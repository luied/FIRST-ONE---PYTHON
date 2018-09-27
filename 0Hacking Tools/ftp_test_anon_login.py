from ftplib import FTP
import subprocess

site = input("\nInsira o site\n")
ftp = FTP("%s" %site)

ftp.set_debuglevel(3)
print("\nConectando-se a %s"%(site))
ftp.login("anonymous","anonymous")
ftp.set_pasv(False)

while True:
    comando = input("%s> "%site)
    if str(comando) == str("help"):
        print("\n\n\
                Only 'dir' avaliable\n\
        ftp.rename(original,novo)\n\
        ftp.delete(arquivo)\n\
        ftp.cwd(passwd/)\n\
        ftp.mkd(pasta)\n\
        ftp.rmd(pasta)\n\
        ftp.size(arquivo)\n\
dir     ftp.dir()\n\
quit    ftp.close()\n\
        \n\
        DOWNLOAD AND UPLOAD\n\
        ftp.retrbinary(RETR BASH_BLA,OPEN(BASH_BLA,wb).write)\n\
        ftp.storbinary(STOR README, open(README,rb))")
    elif str(comando) == str("quit"):
        print("QUITTING...")
        try:
            ftp.close()
        except:

    elif str(comando) == str("dir"):
        try:
            ftp.dir()
        except:
            pass



#ftp.rename("originao","novo")
#ftp.delete("arquivo")
#ftp.cwd("passwd/")
#ftp.mkd("pasta")
#ftp.rmd("pasta")
#ftp.size("arquivo")

#baixar arquivo
#ftp.retrbinary("RETR ARQUIVO_REMOTO",open("NOME_NOVO_DO_ARQUIVO","wb").write)
#upload ftp.storbinary("STOR ARQUIVO_LOCAL",open("ARQUIVO_REMOTO","rb"))
