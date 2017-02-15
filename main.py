import sys

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from random import randint

# game screens
scene_dict = {'day': True, 'snow': False, 'fog': False, 'night': False}

# road types
road_dict = {'straight': True, 'right_curve': False, 'left_curve': False}

# road_points
road_x_points = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
road_y_points = [35, 23.5, 12, 0.5, -11, -22.5, -34, -45.5, -57, -68.5, -80]

# variables - angle
anglep = 0

# variables - states
acceleration_time = 0
move_state = False
move_key_up = True


class Player(object):

    def __init__(self, speed, acceleration, x_trans, y_trans, x_scale, y_scale, r, g, b):
        self.speed = speed
        self.acceleration = acceleration
        self.x_trans = x_trans
        self.y_trans = y_trans
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.r = r
        self.g = g
        self.b = b
        self.box = [x_trans, x_trans+10, y_trans, y_trans+10]

    def draw_body(self):
        # print("draw body")
        # car body


        glBegin(GL_POINTS)
        glColor3ub(120, 120, 120)
        glVertex2i(-5, 5)
        glEnd()

        glColor3ub(self.r, self.g, self.b)
        glBegin(GL_POLYGON)
        glVertex2i(-10, 0)
        glVertex2i(-10, 6)
        glVertex2i(-9, 7)
        glVertex2i(-7, 7)
        glVertex2i(-5, 10)
        glVertex2i(5, 10)
        glVertex2i(7, 7)
        glVertex2i(9, 7)
        glVertex2i(10, 6)
        glVertex2i(10, 0)
        glEnd()

        # car window
        glColor3ub(0, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2i(-5, 7)
        glVertex2i(-4, 9)
        glVertex2i(4, 9)
        glVertex2i(5, 7)
        glEnd()

        # car tire
        glColor3ub(25, 25, 25)
        glBegin(GL_POLYGON)
        glVertex2i(-9, 0)
        glVertex2i(-9, -2)
        glVertex2i(-5, -2)
        glVertex2i(-5, -0)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex2i(9, 0)
        glVertex2i(9, -2)
        glVertex2i(5, -2)
        glVertex2i(5, -0)
        glEnd()

        # car lights
        glColor3ub(238, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2i(-7, 4)
        glVertex2i(-7, 5)
        glVertex2i(-6, 5)
        glVertex2i(-6, 4)
        glEnd()

        glColor3ub(238, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2i(7, 4)
        glVertex2i(7, 5)
        glVertex2i(6, 5)
        glVertex2i(6, 4)
        glEnd()

        # car object
        glColor3ub(255, 255, 255)
        glBegin(GL_POLYGON)
        glVertex2i(-3, 2)
        glVertex2i(-3, 3)
        glVertex2i(3, 3)
        glVertex2i(3, 2)
        glEnd()

    def animate_car(self):

        if self.x_scale <= 1.0 and self.y_scale <= 1.0:
            self.x_scale += 0.05
            self.y_scale += 0.05
            # print(self.x_scale)
        if self.y_trans <= -75:
            self.y_trans = 45
            self.x_trans = 10
            self.y_scale = 0
            self.x_scale = 0
        else:
            self.y_trans -= self.speed * 5
            self.x_trans += randint(-5, 5)

    def get_collision_box(self):
        print(self.box)


def draw_day():

    glClearColor(0.2, 0.6, 1.0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(0, 153, 51)
    glBegin(GL_POLYGON)
    glVertex2i(-100, 35)
    glVertex2i(100, 35)
    glVertex2i(100, -100)
    glVertex2i(-100, -100)
    glEnd()
    return


def draw_night():

    glClearColor(0.25, 0.25, 0.25, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2i(-100, 35)
    glVertex2i(100, 35)
    glVertex2i(100, -100)
    glVertex2i(-100, -100)
    glEnd()
    return


def draw_fog():

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(128, 128, 128)
    glBegin(GL_POLYGON)
    glVertex2i(-100, 5)
    glVertex2i(100, 5)
    glVertex2i(100, -100)
    glVertex2i(-100, -100)
    glEnd()
    return


def draw_snow():

    glClearColor(0.2, 0.6, 1.0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2i(-100, 35)
    glVertex2i(100, 35)
    glVertex2i(100, -100)
    glVertex2i(-100, -100)
    glEnd()
    return


def draw_background():

    if scene_dict.get('day'):
        draw_day()
    elif scene_dict.get('snow'):
        draw_snow()
    elif scene_dict.get('fog'):
        draw_fog()
    else:
        draw_night()
    return


def keyboard(key,   x, y):

    key = ord(key)
    global scene_dict, anglep, x_scale, y_scale
    print("keyboard: "+str(key))
    if key == 27:       # esc
        sys.exit(0)
    elif key == 49:     # 1
        scene_dict = {'day': True, 'snow': False, 'fog': False, 'night': False}
        glutPostRedisplay()
    elif key == 50:     # 2
        scene_dict = {'day': False, 'snow': True, 'fog': False, 'night': False}
        glutPostRedisplay()
    elif key == 51:     # 3
        scene_dict = {'day': False, 'snow': False, 'fog': True, 'night': False}
        glutPostRedisplay()
    elif key == 52:     # 4
        scene_dict = {'day': False, 'snow': False, 'fog': False, 'night': True}
        glutPostRedisplay()
    elif key == 97:     # a
        anglep += 15
        glutPostRedisplay()
    elif key == 115:    # s
        anglep -= 15
        glutPostRedisplay()
    elif key == 122:    # z
        x_scale += 0.1
        y_scale += 0.1
        glutPostRedisplay()
    elif key == 120:    # x
        x_scale -= 0.1
        y_scale -= 0.1
        glutPostRedisplay()
    elif key == 32:    # x
        print("opa")
    return


def move_player(direction):
    global acceleration_time, move_key_up, scene_dict
    if direction == 'right':
        player.x_trans += 2
        if move_key_up is False:
            acceleration_time += 2
            if scene_dict.get('snow') and acceleration_time == 2:
                player.x_trans -= 5
            player.speed += player.acceleration * acceleration_time
            if player.speed >= 8:
                player.speed = 8
                player.x_trans += player.speed
            if player.x_trans + player.speed >= 55:
                player.x_trans = 54
            print('player speed', player.speed)
            print('x_trans', player.x_trans)
    else:
        player.x_trans -= 2
        if not move_key_up:
            acceleration_time += 2
            if scene_dict.get('snow') and acceleration_time == 2:
                player.x_trans += 5
            player.speed += player.acceleration * acceleration_time
            if player.speed >= 8:
                player.speed = 8
                player.x_trans -= player.speed
            if player.x_trans - player.speed <= -55:
                player.x_trans = -54
            print('player speed', player.speed)
            print('x_trans', player.x_trans)
    glutPostRedisplay()
    return


def special_keyboard(key, x, y):

    global move_key_up
    if key == GLUT_KEY_RIGHT:
        move_key_up = False
        move_player('right')
    elif key == GLUT_KEY_LEFT:
        move_key_up = False
        move_player('left')
    return


def special_up_keyboard(key, x, y):
    global acceleration_time
    global move_key_up
    if key == GLUT_KEY_RIGHT or key == GLUT_KEY_LEFT:
        # print("glut key up")
        move_key_up = True
        player.speed = 1
        player.acceleration = 0.2
        acceleration_time = 0
    return


def draw_road():
    global scene_dict
    glColor3ub(105, 105, 105)
    glLineWidth(5)

    glBegin(GL_LINE_STRIP)
    for i in range(0, 11):
        # print(str(road_x_points[i]) + '/' + str(road_y_points[i]))
        if scene_dict.get('fog') and i <= 5:
            glColor3ub(0, 0, 0)
        glVertex2f(-road_x_points[i], road_y_points[i])
    glEnd()

    glBegin(GL_LINE_STRIP)
    for i in range(0, 11):
        # print(road_x_points[i])
        if scene_dict.get('fog') and i <= 5:
            glColor3ub(0, 0, 0)
        glVertex2f(road_x_points[i], road_y_points[i])
    glEnd()


def draw_info_area():

    # info area
    glColor3ub(0, 0, 0)
    glBegin(GL_QUAD_STRIP)
    glVertex2f(-100, -80)
    glVertex2f(100, -80)
    glVertex2f(-100, -100)
    glVertex2f(100, -100)
    glEnd()
    return


def draw_mountains():

    # mountains
    glColor3ub(150, 70, 60)

    glBegin(GL_TRIANGLES)
    glVertex2i(-20, 35)
    glVertex2i(-40, 35)
    glVertex2i(-30, 45)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2i(-35, 35)
    glVertex2i(-55, 35)
    glVertex2i(-45, 55)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2i(-50, 35)
    glVertex2i(-75, 35)
    glVertex2i(-65, 55)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2i(20, 35)
    glVertex2i(40, 35)
    glVertex2i(30, 55)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2i(35, 35)
    glVertex2i(55, 35)
    glVertex2i(45, 45)
    glEnd()
    return


def draw_scenery():
    global scene_dict

    draw_info_area()

    if not scene_dict.get('fog'):
        draw_mountains()
    glFlush()
    return


def draw_on_screen():

    draw_background()
    draw_road()
    draw_scenery()

    # add_player()
    glPushMatrix()
    glRotatef(anglep, 0, 0, 1)
    glScalef(player.x_scale, player.y_scale, 1)
    glTranslated(player.x_trans, player.y_trans, 0)
    player.draw_body()
    glPopMatrix()

    glPushMatrix()
    glRotatef(anglep, 0, 0, 1)
    glTranslated(enemy_01.x_trans, enemy_01.y_trans, 0)
    glScalef(enemy_01.x_scale, enemy_01.y_scale, 1)
    enemy_01.draw_body()
    glPopMatrix()

    glPushMatrix()
    glRotatef(anglep, 0, 0, 1)
    glTranslated(enemy_02.x_trans, enemy_02.y_trans, 0)
    glScalef(enemy_02.x_scale, enemy_02.y_scale, 1)
    enemy_02.draw_body()
    glPopMatrix()

    glPushMatrix()
    glRotatef(anglep, 0, 0, 1)
    glTranslated(enemy_03.x_trans, enemy_03.y_trans, 0)
    glScalef(enemy_03.x_scale, enemy_03.y_scale, 1)
    enemy_03.draw_body()
    glPopMatrix()

    glutSwapBuffers()
    return


def check_collision():
    if enemy

    if player.y_trans >= enemy_01.y_trans:
        enemy_01.y_trans += 10
        glutPostRedisplay()
    if player.y_trans >= enemy_02.y_trans:
        enemy_02.y_trans += 10
        glutPostRedisplay()
    if player.y_trans >= enemy_03.y_trans:
        enemy_03.y_trans += 10
        glutPostRedisplay()

def timer(value):
    check_collision()
    enemy_01.animate_car()

    enemy_02.animate_car()

    enemy_03.animate_car()

    glutPostRedisplay()
    glutTimerFunc(100, timer, 1)
    return


def initialize():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    return


if __name__ == "__main__":

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(112, 84)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Enduro")
    glutDisplayFunc(draw_on_screen)
    glutTimerFunc(500, timer, 1)
    initialize()

    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keyboard)
    glutSpecialUpFunc(special_up_keyboard)

    player = Player(1, 0.3, 0, -75, 1, 1, randint(0, 255), randint(0, 255), randint(0, 255))
    enemy_01 = Player(0.8, 1, 10, 35, 0.1, 0.1, randint(0, 255), randint(0, 255), randint(0, 255))
    enemy_02 = Player(1.1, 1, -10, 35, 0.1, 0.1, randint(0, 255), randint(0, 255), randint(0, 255))
    enemy_03 = Player(0.95, 1, -0, 35, 0.1, 0.1, randint(0, 255), randint(0, 255), randint(0, 255))
    check_collision()
    glutMainLoop()
