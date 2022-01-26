"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width,paddle_height,
                            x=window_width/2-paddle_width/2,
                            y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)
        self.draw_bricks()

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2,
                          x=window_width/2-ball_radius,
                          y=window_height/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0
        self.set_ball_velocity()

        self.switch = True

        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.start_game)

    # set ball velocity randomly
    def set_ball_velocity(self):
        self.dx = random.randint(0, MAX_X_SPEED)
        self.dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.dx = -self.dx

    # draw the bricks by the rows and cols
    def draw_bricks(self):
        for i in range(0,self.brick_cols):
            for j in range(0,self.brick_rows):
                self.brick_line1= GRect(self.brick_width,self.brick_height,
                                         x=0+self.brick_width*i+self.brick_spacing*i,
                                         y=self.brick_offset+self.brick_height*j+self.brick_spacing*j)
                self.brick_line1.filled = True
                if j <= 1:
                    self.brick_line1.fill_color = 'red'
                    self.brick_line1.color='red'
                elif 1 < j <= 3:
                    self.brick_line1.fill_color = 'orange'
                    self.brick_line1.color='orange'
                elif 3 < j <= 5:
                    self.brick_line1.fill_color = 'yellow'
                    self.brick_line1.color='yellow'
                elif 5 < j < 8:
                    self.brick_line1.fill_color = 'green'
                    self.brick_line1.color='green'
                else:
                    self.brick_line1.fill_color = 'blue'
                    self.brick_line1.color='blue'
                self.window.add(self.brick_line1)

    # use switch to control the game
    def start_game(self, event):
        if self.switch is True:
            self.set_ball_position()
            self.set_ball_velocity()
            self.switch = False

    # set the ball start position at the middle of the window
    def set_ball_position(self):
        self.ball.x = self.window.width/2-self.ball.width/2
        self.ball.y = self.window.height/2

    # paddle position which y position remain the same, and x position move with the mouse
    def paddle_position(self,event):
        if event.x-self.paddle.width <0:
            self.window.add(self.paddle,x=0,y=self.paddle.y)
        elif event.x+self.paddle.width > self.window.width:
            self.window.add(self.paddle,x=self.window.width-self.paddle.width,y=self.paddle.y)
        else:
            self.window.add(self.paddle,x=event.x-self.paddle.width/2,y=self.paddle.y)

    # check the object is paddle or not
    def check_paddle(self):
        obj3 = self.window.get_object_at(self.ball.x,self.ball.y + self.ball.height)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width,self.ball.y + self.ball.height)

        is_paddle = obj3 == self.paddle or obj4 == self.paddle
        return is_paddle

    # check the object is brick or not , if is remove the brick at the main function
    def check_brick(self):
        obj = self.window.get_object_at(self.ball.x,self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + self.ball.width,self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x,self.ball.y + self.ball.height)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width,self.ball.y + self.ball.height)
        if self.check_paddle() is False and obj is not None:
            return obj
        if self.check_paddle() is False and obj2 is not None:
            return obj2
        if self.check_paddle() is False and obj3 is not None:
            return obj3
        if self.check_paddle() is False and obj4 is not None:
            return obj4

    # check the ball is out of the paddle or not
    def ball_out_paddle(self):
        ball_out_paddle = self.ball.y + self.ball.height > self.paddle.y + self.paddle.height
        self.switch = True
        return ball_out_paddle
