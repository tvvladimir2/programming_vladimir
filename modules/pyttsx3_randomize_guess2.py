# Import the random module, and display a random number between 1 and 9:
import random
# Import the required module for text to speech conversion
import pyttsx3
# import time module
import time

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# Voice change
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # voices[1].id Русский, voices[0].id ENGLISH
# SPEECH RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5) # minus to slow down, plus to speed up

points = 0
scoreWin = 5

engine.say("Добро пожаловать. Набери " + str(scoreWin) + " очков и ты выиграл. Ноль или меньше значит проиграл." )
engine.say("Ну давай начнём. Проверим твой интеллект. ")
# engine.say("Sound check")
engine.runAndWait()

# select an item from a list?
# answer1 = "Hahahah ahah ahhha ha ha ha ha ha, dumb, dumb."
# answer2 = "Missed it. Failed it. Ha ha."
# answer3 = "Nope! Muahaha"
# answer4 = "Excellent! You are wrong!"
# answer5 = "I'm amazed. Are all humans so dumb?"
# answerListEN = [answer1, answer2, answer3, answer4, answer5]

answer1 = "Ха ха ха, не парся, всё равно не получится. "
answer2 = "Не смеши корову! Метод тыка тут не работает. Если тебе смешно, то корова это ты."
answer3 = "Жааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааль. Жаль жаль жаль."
answer4 = "Вот здорово! Синички поют на дворе, а ты так лажаешь. Не соси палец, это не прилично."
answer5 = "Завалил такой простой вопрос. Не хочу больше разочаровываться. Уходи, больше не играй. "
answerList = [answer1, answer2, answer3, answer4, answer5]

# print(str(random.choice(answerList)))
# engine.say(str(random.choice(answerList)))

# def LOL():
#     engine.say(str(random.choice(answerList)))

while True:
    print("\n")
    print("У тебя сейчас " + str(points) + " очков. Набери " + str(scoreWin) + " и ты выиграл.")
    print("\n")
    a = random.randrange(1, 10)
    b = random.randrange(1, 100)
    operatorList = ['+', '-', '*']
    c = random.choice(operatorList)
    q = eval(str(a)+str(c)+str(b))
    print("What is the result of the following equation?")
    print(a, c, b, "=")
    w = int(input(""))

    if w == q:
        # print("Well done!")
        # engine.say('Well done!')
        print("Отлично!")
        engine.say('Отлично!')
        if str(c)=="*":
            sayWin = str(str(a) + "умножить на" + str(b) + "=" + str(w))
            engine.say(sayWin)
        else:
            sayWin = str(str(a) + str(c) + str(b) + "=" + str(w))
            engine.say(sayWin)
        points += 1
        if points == scoreWin:
            print("Поздравляю! Ты набрал " + str(scoreWin) + " очков!")
            engine.say("Я не ожидал, но ты выиграл. Приходи играть ещё. Ты можешь выиграть большой приз. Хотя я не верю что ты сможешь пройти следующий уровень.")
            engine.runAndWait()
            break
        time.sleep(1)
        # engine.say("Let's try again")
        engine.say("Давай продолжим")
        engine.runAndWait()

    else:
        # print(str(random.choice(answerList)))
        e = random.choice(answerList)
        points -= 1
        if points == 0 or points == -1:
            print("Ты проиграл. У тебя 0 очков или меньше.")
            engine.say("Ты проиграл, уходи и не возвращайся. Можешь плакать сколько влезет. Я жестокая программа.")
            engine.runAndWait()
            break
        print(str(e))
        engine.say(str(e))
        time.sleep(1)
        # engine.say("Let's try again")
        engine.say("Ну попробуй снова")
        engine.runAndWait()

# engine.runAndWait()
