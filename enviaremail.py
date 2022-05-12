import win32com.client as win32

# criando integração com o outlook(deve ter instalado na sua máquina)
outlook = win32.Dispatch('outlook.application')

#criando email
email = outlook.CreateItem(0)

#configurando informações do seu email, To = destino, Subject = assunto, body = corpo do email
email.To = "calebesantos@hotmail.com"
email.Subject = "Email automático do python"
email.HTMLBody = """
<p>Olá Calebe</p>

<p>Você conseguiu enviar um email automatico com python</p>
<p>Que incrivel não é?</p>
"""

#anexo = "C//users/calebe/downloads/arquivo.pdf"
#email.Attachments.Add(anexo)

email.Send()
print("Email Enviado")