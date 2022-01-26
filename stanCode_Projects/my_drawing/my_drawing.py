"""
File: my_drawing
Name: LEE HSUAN HSUAN
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon ,GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Sometimes little things in daily life that bring us happiness.
    Hope everyone can enjoy every moment of your life:)
    """
    window = GWindow(500,500, title='The little things')

    tail = GOval(50,30,x=140,y=380)
    tail.filled = True
    tail.fill_color = 'lightgray'
    tail.color = 'lightgray'
    window.add(tail)

    tail_2 = GOval(80,35,x=130,y=365)
    tail_2.filled = True
    tail_2.fill_color = 'white'
    tail_2.color = 'white'
    window.add(tail_2)

    body_2 = GPolygon()
    body_2.add_vertex((180,425))
    body_2.add_vertex((300,425))
    body_2.add_vertex((230,320))
    body_2.filled = True
    body_2.fill_color = 'lightgrey'
    body_2.color = 'lightgrey'
    window.add(body_2)

    body = GPolygon()
    body.add_vertex((170,440))
    body.add_vertex((270,440))
    body.add_vertex((200,290))
    body.filled = True
    body.fill_color = 'lightgrey'
    body.color = 'lightgrey'
    window.add(body)

    ear_2 = GOval(100,120,x=120,y=175)
    ear_2.filled = True
    ear_2.fill_color = 'lightgray'
    ear_2.color = 'lightgray'
    window.add(ear_2)

    ear_1 = GOval(110,100,x=110,y=240)
    ear_1.filled = True
    ear_1.fill_color = 'lightgrey'
    ear_1.color = 'lightgrey'
    window.add(ear_1)

    nose_1 = GOval(80,110,x=260,y=190)
    nose_1.filled = True
    nose_1.fill_color = 'lightgrey'
    nose_1.color = 'lightgrey'
    window.add(nose_1)

    nose_2 = GOval(60,90,x=260,y=175)
    nose_2.filled = True
    nose_2.fill_color = 'white'
    nose_2.color = 'white'
    window.add(nose_2)

    head = GOval(150,150,x=150,y=190)
    head.filled = True
    head.fill_color = 'lightgrey'
    head.color = 'lightgrey'
    window.add(head)

    eye = GOval(30,30,x=233,y=240)
    eye.filled = True
    eye.fill_color = 'darkgray'
    eye.color = 'darkgray'
    window.add(eye)

    eye_2 = GOval(10,10,x=248,y=242)
    eye_2.filled = True
    eye_2.fill_color = 'white'
    eye_2.color = 'white'
    window.add(eye_2)

    mouth = GArc(30,50,180,180,x=248,y=289)
    mouth.filled = True
    mouth.fill_color = 'darkgray'
    mouth.color = 'darkgray'
    window.add(mouth)

    mouth_2 = GOval(32,12,x=247,y=297)
    mouth_2.filled = True
    mouth_2.fill_color = 'lightgrey'
    mouth_2.color = 'lightgrey'
    window.add(mouth_2)

    bubble = GOval(90,90,x=285,y=138)
    bubble.filled = True
    bubble.fill_color = 'skyblue'
    bubble.color = 'skyblue'
    window.add(bubble)

    bubble = GOval(10,25,x=295,y=160)
    bubble.filled = True
    bubble.fill_color = 'snow'
    bubble.color = 'snow'
    window.add(bubble)

    bubble_2 = GOval(10,10,x=295,y=193)
    bubble_2.filled = True
    bubble_2.fill_color = 'snow'
    bubble_2.color = 'snow'
    window.add(bubble_2)

    word = GLabel('"What makes you happy?"')
    word.color = "slategray"
    word.font = "Times New Roman-18-bold"
    window.add(word,125,80)

    word_2 = GLabel('"Blowing bubbles."')
    word_2.color = "slategray"
    word_2.font = "Times New Roman-18-bold"
    window.add(word_2,150,110)

    word_3 = GLabel('"The little things."')
    word_3.color = "slategray"
    word_3.font = "Times-14-bold-italic"
    window.add(word_3,350,445)


if __name__ == '__main__':
    main()
