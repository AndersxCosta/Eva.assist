import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            audio.adjust_for_ambient_noise(source)
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'eva' in comando:
                comando = comando.replace('eva','')
                maquina.runAndWait()
    except:
        print('Microfone não detectado')
    
    return comando

def comando_Voz():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('São' + hora)
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por','')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        maquina.say(resultado)
        maquina.runAndWait() 

    elif 'tocar' in comando:
        musica = comando.replace('tocar', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando' + musica)
        maquina.runAndWait()

    elif 'pesquisar' in comando:
        pesquisa = comando.replace('pesquisar', '')
        maquina.say(f"Procurando por {pesquisa} no Google.")
        url = f"https://www.google.com/search?q={pesquisa}"
        maquina.runAndWait()
        webbrowser.open(url)

    elif 'lista de compras' in comando:
        maquina.say("Criando a lista de compras.")
        maquina.runAndWait()
        lista_compras = []
        maquina.say("Diga os itens da lista.")
        maquina.runAndWait()
        audio_compras = executa_comando()
        lista_compras.append(audio_compras)
        maquina.say("A lista de compras foi criada com sucesso!")
        maquina.runAndWait()
        print("Lista de Compras:")
        maquina.say(f"lista_compras: {lista_compras}") 
        maquina.runAndWait()
        return lista_compras
    
    else:
        maquina.say("Desculpe, não entendi o comando.")
        maquina.runAndWait()

comando_Voz()




