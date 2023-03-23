from gtts import gTTS

from os import path, mkdir

OUTPUT_DIR = "./results"

def generateTTS(text:str):
    tts = gTTS(text)

    

    return tts

if __name__ == "__main__":
    
    if not path.isdir(OUTPUT_DIR):
        mkdir(OUTPUT_DIR)

    choice = "y"
    while choice.lower() == "y":
        # make tts
        text = input("Type the text you want to be spoken: ")
        tts = generateTTS(text)
        # save audio file
        fileName = input("Type the output file name ('.mp3' is optional): ")
        if fileName[-4:].lower() != ".mp3":
            fileName += ".mp3"
        savePath = path.join(OUTPUT_DIR, fileName)
        tts.save(savePath)

        choice = input("Do you want to continue (Y/n)? ")