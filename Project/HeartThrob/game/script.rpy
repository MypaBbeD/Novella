# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Main = Character("ГГ")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.
show Тянка что-то рисует
scene bg 1 at center


Main "Знаете что? Я никогда и не был каким-то сумасшедшим фанатом видеоигр,
    никогда не терял связь с реальностью, погружаясь в какой-то фильм, сериал или аниме. "

scene bg 2 at center


Main "Но… если бы у меня был выбор, остаться в любимом вымышленном мире или жить
    в реальности, я не раздумывая выбрал бы первое. Другое дело, если он не вымышленный,
    а просто отличающийся от нашего. "

scene bg 3 at center


Main "Там ведь тоже были бы свои проблемы, которые приходилось бы решать.
    Там тоже была бы кровь, разочарование, предательство.
    Да и к тому же, там не было бы видеоигр, фильмов и аниме! "

scene bg 4 at center


Main "Там не было бы моего друга, пусть и странного, но я к нему прикипел."

scene bg 5 at center


Main "Там не было бы клевых картинок с котами, видео с нелепыми падениями людей.."

scene bg 6 at center


Main "..блоггеров.."

scene bg 7 at center


Main "..хотя, это может даже к лучшему."
Main "любимой музыки, моей комнаты. Там не было бы её…  "

scene Школьный кабинет





    # This ends the game.

return
