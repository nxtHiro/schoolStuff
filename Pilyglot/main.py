import os
import pytesseract
import cv2
from Tkinter import *
import Tkinter as tk
from PIL import ImageTk, Image
from googletrans import Translator

def quit():
    window.destroy()

# Function to translate languages
def autoTranslateLang(langEnd,text):
    langDict = {"English": "en",
                "Spanish": "es",
                "Esperanto": "eo",
                "French": "fr",
                "German": "de",
                "Chinese": "zh-CN",
                "Japanese": "ja",
                "Korean": "ka",
                "Hindi": "hi",
                "Arabic": "ar",
                "Portugese": "pt",
                "Bengali": "bn",
                "Russian": "ru",
                "Telugu": "te",
                "Marathi": "mr",
                "Turkish": "tr",
                "Tamil": "ta",
                "Vietnamese": "vi",
                "Urdu": "ur"}
    # logic for the dropdown box and calls the translator
    if(langEnd == "       Choose One       "):
        return "Please pick a translate language"

    else:
         finalText = Translator().translate(text, langDict[langEnd])
         return finalText.text
def processImage(img):
    # runs process_image.py with the captured image and creates a processed image
    os.system('python process_image.py {} img_pro.png'.format(img))
    return pytesseract.image_to_string(Image.open('img_pro.png'))

# Class for the gui
class GUI(Frame):

    # constructor
    def __init__(self,master,text):
        Frame.__init__(self,master)
        master.attributes("-fullscreen", True)
        self.master = master

        # variable for dropdown box
        self.variable = StringVar(self.master)
        self.lang = 0

        # Time interval for often it checks dropdown box
        self.TimerInterval = 500

        self.Language = StringVar(self.master)

        # Text to be translated
        self.text = text

    # Function to start up GUI
    def setupGUI(self):

        image = Image.open('text.png')
        image.save('text.gif')
        
        img = PhotoImage(file = "text.gif")
        img = img.subsample(2,2)
        
        # uses the picture that is taken and puts it in gui
        panel = Label(self.master,image = img)
        panel.image=img
        panel.grid(row=2,column=0,rowspan=10,columnspan = 1, sticky=N+S+E+W,padx=5)

        # used for formatting
        l1 = Label(self.master,text="    ",height=8)
        l1.grid(row=16,column=1)

        # the translated text
        l2 = Label(self.master,textvariable=self.Language)
        l2.grid(row=13,column=0,columnspan = 3, sticky=W,padx=5,pady=5)

        # text label
        l3 = Label(self.master, text = "Translated Text:")
        l3.grid(row = 12, column = 0, sticky = W,padx=5,pady=5)

        #initial state of drop down box
        self.variable.set("       Choose One       ")
        
        # target language label
        l4 = Label(self.master, text = "Target Language: ")
        l4.grid(row = 2, column = 1, sticky = N+W)
        
        l5 = Label(self.master, text = "PiLyglot")
        l5.grid(row = 1, column = 0, sticky = N+W, padx = 5, pady = 5)
        
        l6 = Label(self.master, text = "                        ")
        l6.grid(row = 0, column = 0, columnspan = 2)
        # creates first dropdown box
        d1 = OptionMenu(self.master,self.variable,"English","Spanish","Esperanto","French","German","Chinese","Japanese","Korean","Hindi","Arabic","Portugese","Bengali","Russian","Telugu","Marathi","Turkish","Tamil","Vietnamese","Urdu")
        d1.grid(row=3,column=1,sticky=N+W+E)
        # exit to camera
        b1 = Button(self.master, text = "Return to camera", command = quit)
        b1.grid(row = 11, column = 1, sticky = S+W+E)
        
        # calls method that checks dropdown box
        self.getTrans()

    # checks dropdown box
    def getTrans(self):
        self.Language.set(self.lang)
        self.lang = autoTranslateLang(self.variable.get(),self.text)
        self.after(self.TimerInterval,self.getTrans)

# runs webcam in a gui
class webCam():
    # constructor
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("Press Space to Capture Image")
        self.runCam()

    # function to start the default system webcam
    def runCam(self):
        while True:
            ret, frame = self.cam.read()
            cv2.imshow("Press Space to Capture Image", frame)

            if not ret:
                break
            k = cv2.waitKey(1)

            if k%256 == 27:
                # ESC pressed
                break
            elif k%256 == 32:
                # SPACE pressed
                # captures and writes the image
                img_name = "text.png"
                cv2.imwrite(img_name, frame)

                # processes and extracts the text
                text = processImage(img_name)
                
                # sets up window and GUI
                global window
                window = Tk()

                # takes screen dimensions
                screen_width = window.winfo_screenwidth()
                screen_height = window.winfo_screenheight()

                # sets window title
                window.title('Pilyglot')

                # makes window occupy the screen
                window.geometry('{}x{}'.format(screen_width,screen_width))
                g = GUI(window,text)
                g.setupGUI()
                cv2.destroyAllWindows()
                window.mainloop()

        self.cam.release()

        cv2.destroyAllWindows()



# instantiates webCam class
webCam()
