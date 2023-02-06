import gtts
from playsound import playsound

with open('aquivo.txt', 'r') as arquivo:#abrindo o arquivo de texto, [arquivo] e o objeto - 'r' é read/leitura.
    for linha in arquivo:#laço for q cria a variavel linha q recebe os dados do arquivo 
        frase = gtts.gTTS(linha,lang='pt-br')#variavel frase recebe a transriçao do arquivo txt, lang='portugues'
        frase.save('aquivo.mp3')#objeto frase usa o metodo save e define o nome do arquivo mp3
        playsound('aquivo.mp3')#tocando o arquivo

