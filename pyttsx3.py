#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3


# In[ ]:


It works offline, unlike other text-to-speech libraries. Rather than saving the text as audio file, 
pyttsx actually speaks it there. This makes it more reliable to use for voice-based projects.


# In[ ]:


#An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3.Engine instance.


# In[ ]:


#The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.


# In[ ]:


It supports three TTS engines :

sapi5 – SAPI5 on Windows
nsss  –  NSSpeechSynthesizer on Mac OS X
espeak – eSpeak on every other platform


# In[ ]:


Usage –
First we need to import the library and then initialise it using init() function. This function may take 2 arguments.
init(driverName string, debug bool)

drivername : [Name of available driver] sapi5 on Windows | nsss on MacOS
debug: to enable or disable debug output
After initialisation, we will make the program speak the text using say() function. This method may also take 2 arguments.
say(text unicode, name string)
text : Any text you wish to hear.
name : To set a name for this speech. (optional)
Finally, to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().


# In[5]:


# Import the required module for text  
# to speech conversion
import pyttsx3
  
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
  
# say method on the engine that passing input text to be spoken
engine.say('Hello sir, how may I help you, sir.')
  
# run and wait method, it processes the voice commands. 
engine.runAndWait()


# In[ ]:


getProperty(name : string) –> Gets the current value of an engine property.

setProperty(name, value) –> Queues a command to set an engine property.
The new property value affects all utterances queued after this command.


# In[2]:


import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#changing index changes voices but ony 0 and 1 are working here
engine.say('Hello sir, how may I help you, sir.')
engine.runAndWait()


# In[ ]:


#To get the list of voices, write the following code.


# In[5]:


engine = pyttsx3.init()
voices = engine.getProperty('voices')
  
for voice in voices:
    # to get the info.about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)


# In[ ]:


#Saving voice to a file


# In[6]:


import pyttsx3
engine = pyttsx3.init()
engine.save_to_file('Hello World' , 'test.mp3')
engine.runAndWait()


# In[ ]:


#Listening for events


# In[1]:


import pyttsx3
def onStart(name):
   print('starting', name) 

def onWord(name, location, length):
   print('word', name, location, length) 

def onEnd(name, completed):
   print('finishing', name, completed)

engine = pyttsx3.init()

engine.connect('started-utterance', onStart)

engine.connect('started-word', onWord)

engine.connect('finished-utterance', onEnd)

engine.say('The quick brown fox jumped over the lazy dog.')

engine.runAndWait()


# In[ ]:


#Changing voices


# In[2]:


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


# In[ ]:


#Changing speech rate


# In[5]:


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


# In[ ]:


#Changing volume


# In[6]:


engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


# In[ ]:




