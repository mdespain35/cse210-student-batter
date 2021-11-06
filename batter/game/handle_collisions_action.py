from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        paddle_array = []
        bricks = cast["brick"]

        # Create array of points based on length of paddle's text
        for i in range(len(paddle.get_text())):
            x = paddle.get_position().get_x() + i
            y = paddle.get_position().get_y()
            paddle_array.append(Point(x, y))
        # Loop through array of points to check if ball hits any of them
        for p in paddle_array:
            if p.equals(ball.get_position()):
                ball.set_velocity(ball.get_velocity().reverse_y())
        # Loop through bricks array and check position. Only change velocity if a "brick" is still there.
        for brick in bricks:
            if brick.get_position().equals(ball.get_position()) and brick.get_text() != ' ':
                ball.set_velocity(ball.get_velocity().reverse_y())
                brick.set_text(' ')