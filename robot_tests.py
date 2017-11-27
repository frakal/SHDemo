import unittest

from robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()
        self.robot.place(0,0,0)

    def test_rotation(self):
        self.assertEqual(self.robot.orientation, 0)
        self.robot.right()
        self.assertEqual(self.robot.orientation, 3)
        self.robot.right()
        self.assertEqual(self.robot.orientation, 2)
        self.robot.right()
        self.assertEqual(self.robot.orientation, 1)
        self.robot.left()
        self.assertEqual(self.robot.orientation, 2)
        self.robot.left()
        self.assertEqual(self.robot.orientation, 3)
        self.robot.left()
        self.assertEqual(self.robot.orientation, 0)

    def test_ignore_move(self):
        #the move command should be ignored in the following scenarios
        self.robot.place(0,0,2)
        self.robot.move()
        self.assertEqual(self.robot.x_pos, 0)
        self.assertEqual(self.robot.y_pos, 0)
        self.robot.place(4,0,0)
        self.robot.move()
        self.assertEqual(self.robot.x_pos, 4)
        self.assertEqual(self.robot.y_pos, 0)
        self.robot.place(0,0,3)
        self.robot.move()
        self.assertEqual(self.robot.x_pos, 0)
        self.assertEqual(self.robot.y_pos, 0)
        self.robot.place(0,4,1)
        self.robot.move()
        self.assertEqual(self.robot.x_pos, 0)
        self.assertEqual(self.robot.y_pos, 4)

    def test_move(self):
        self.robot.place(0,0,0)
        self.robot.move()
        self.assertEqual(self.robot.x_pos, 1)
        self.assertEqual(self.robot.y_pos, 0)
        self.robot.place(0,0,1)
        self.robot.move()
        self.assertEqual(self.robot.x_pos, 0)
        self.assertEqual(self.robot.y_pos, 1)


if __name__ == '__main__':
    unittest.main()