import pywhatkit

contacts = ["+555484341334", "+555499726015"]

header = '''
Opa, tudo bem? Aqui é o Voltolini, do Objetivismo Brasil.
'''
message = '''
Preciso dizer que essa é uma mensagem muito importante.
'''
goodbye = '''
Muito obrigado e boa semana.
Lucas Voltolini
'''

message = header + message + goodbye 
for contact in contacts:
    pywhatkit.sendwhatmsg_instantly(contact, message = message, wait_time = 8, tab_close = True)