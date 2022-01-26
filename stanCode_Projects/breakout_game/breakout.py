"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Add animation loop here!
    graphics = BreakoutGraphics()
    brick_nums = graphics.brick_cols * graphics.brick_rows
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        # check ball condition
        if graphics.check_brick():
            obj = graphics.check_brick()
            graphics.window.remove(obj)
            graphics.dy = -graphics.dy
            brick_nums -= 1
        if brick_nums == 0:
            break
        if graphics.ball_out_paddle():
            lives -= 1
            if lives > 0:
                graphics.switch = True
                print(lives)
            else:
                graphics.set_ball_position()
                break

        # ball moving
        graphics.ball.move(graphics.dx, graphics.dy)
        # make sure ball is in the window
        if graphics.ball.y + graphics.ball.height >= graphics.window.height or graphics.ball.y < 0:
            graphics.dy = -graphics.dy
        if graphics.ball.x < 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
            graphics.dx = -graphics.dx
        if graphics.check_paddle():
            graphics.dy = -graphics.dy


if __name__ == '__main__':
    main()
