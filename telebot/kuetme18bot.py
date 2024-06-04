import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import os
token = os.environ['1393924527:AAHjxbXMdLhR1MLVyVD9qAAKb0I0d9QEfxA']


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    
    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/hi':
        bot.sendMessage (chat_id, str("Hi! I am MechaBot! What do you want?"))
    elif command == '/time':
        bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/kuetlogo':
        bot.sendPhoto (chat_id, photo = open('/home/pi/Downloads/logo.png'))
    #elif command == '/file':
    #    bot.sendDocument(chat_id, document=open('/home/pi/Aisha.py'))
    elif command == '/welcome_audio':
        bot.sendAudio(chat_id, audio=open('/home/pi/Downloads/welcome.mp3'))
    elif command == '/thermodynamics':
        bot.sendMessage (chat_id, str("Choose option: \n /mizansir \n /sharifulsir \n"))
    elif command == '/mizansir':
        bot.sendMessage (chat_id, str("/classnotesMizanSir \n /liveclassrecord \n /books \n /others"))
    elif command == '/sharifulsir':
        bot.sendMessage (chat_id, str("/classnotesSharifulSir \n /liveclassrecord \n /books \n /others"))
    elif command == '/classnotesMizanSir':
        bot.sendMessage (chat_id, str("https://drive.google.com/drive/folders/1P_tlXH2_0ThjGbE2B1aYnGDiHO2vDoIr?usp=sharing"))
    elif command == '/liveclassrecord':
        bot.sendMessage (chat_id,str('https://drive.google.com/drive/folders/1IOaVsP1LhgyqFL_TquPbyb0OGJwSm6jK?usp=sharing') )
    elif command == '/userguide':
        bot.sendMessage(chat_id,str('User Guide:\n (Type those words for access or click on the word)\n /hi \n /time \n /kuetlogo \n /welcome_audio \n /thermodynamics \n /fluidmechanics \n /math \n /sociology \n /Electronics \n '))
    elif command == '/books':
        bot.sendMessage(chat_id,str('https://drive.google.com/drive/folders/1E3N096a1Kseie9Ce4etfg0eUYLFQh6dU?usp=sharing'))
    elif command == '/fluidmechanics':
        bot.sendMessage (chat_id, str("Choose option: \n /aftabsir \n /iliasinamsir \n"))
    elif command == '/math':
        bot.sendMessage (chat_id, str("/classnotesMath \n /liveclassrecord \n /books \n /others"))
    elif command == '/sociology':
        bot.sendMessage (chat_id, str("/classnotesSociology \n /liveclassrecord \n /books \n /others"))
    elif command == '/math':
        bot.sendMessage (chat_id, str("/classnotesMath \n /liveclassrecord \n /books \n /others"))
    elif command == '/aftabsir':
        bot.sendMessage (chat_id, str("/classnotesAfrabSir \n /liveclassrecord \n /books \n /others")) 
    elif command == '/iliasinamsir':
        bot.sendMessage (chat_id, str("/classnotesIliasinamSir \n /liveclassrecord \n /books \n /others"))    
    elif command == '/classnotesAfrabSir':
        bot.sendMessage (chat_id, str("https://drive.google.com/drive/folders/13SS3IljkSieUTGL7T1N9dgUnlpoE6yxZ?usp=sharing"))
    elif command == '/classnotesIliasinamSir':
        bot.sendMessage (chat_id, str("https://drive.google.com/drive/folders/17A-VwnMmSwDjVDBXWYPyKwz1RbqzMuAS?usp=sharing"))
    elif command == '/classnotesMath':
        bot.sendMessage (chat_id, str("https://drive.google.com/drive/folders/154zxZtY512jGZBrqjhuIsf74AiARqgFo?usp=sharing"))
    elif command == '/classnotesSharifulSir':
        bot.sendMessage (chat_id, str("https://drive.google.com/drive/folders/1X8Fo55rUQHfQ27uQe6IGJyiw5057EI5a?usp=sharing")) 
    elif command == '/classnotesSociology':
        bot.sendMessage (chat_id, str("https://drive.google.com/drive/folders/1_6mv4w6zQKw5D_3ZpG5F4--LaTQYYZHI?usp=sharing")) 
    elif command == '/Electronics':
        bot.sendMessage (chat_id, str("Choose option: \n /nurnobisir \n /jahedulsir \n"))
    elif command == '/nurnobisir':
        bot.sendMessage (chat_id, str("/classnotesnurnobisir \n /liveclassrecord \n /books \n /others"))
    elif command == '/jahedulsir':
        bot.sendMessage (chat_id, str("/classnotesjahedulsir \n /liveclassrecord \n /books \n /others"))
    elif command == '/classnotesnurnobisir':
        bot.sendMessage (chat_id, str("https://drive.google.com/file/d/1Xpb438rb_qctDG0MQfmDfzeWWRlGL8z6/view?usp=sharing"))
    elif command == '/classnotesjahedulsir':
        bot.sendMessage (chat_id, str("https://drive.google.com/file/d/14B1vurjhZFpXIiN9yAlnR3sj6Fz4GSlT/view?usp=sharing"))
    elif command == '/help':
        bot.sendVideo(chat_id, video =open('/home/pi/Downloads/help.mp4'))




    bot.sendMessage(chat_id,str('For user guide : /userguide'))


bot = telepot.Bot(token)

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
