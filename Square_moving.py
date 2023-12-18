import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():
    glBegin(GL_TRIANGLES)

    # Front face
    glColor3f(1, 0, 0)  # Red
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)

    # Left face
    glColor3f(0, 1, 0)  # Green
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)

    # Right face
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)

    # Back face
    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)

    # Top face
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)

    # Bottom face
    glColor3f(0, 1, 1)  # Cyan
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glEnd()

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_caption("04 Lab 1")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    glEnable(GL_DEPTH_TEST)  

    last_rotation_time = pygame.time.get_ticks()
    rotate_left = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            glTranslatef(0, 0, 0.1)  # Move forward
        if keys[pygame.K_s]:
            glTranslatef(0, 0, -0.1)  # Move backward
        if keys[pygame.K_a]:
            glTranslatef(-0.1, 0, 0)  # Move left
        if keys[pygame.K_d]:
            glTranslatef(0.1, 0, 0)  # Move right

        current_time = pygame.time.get_ticks()
        if current_time - last_rotation_time > 5000:  # Rotate every 5 seconds
            rotate_left = not rotate_left  # Toggle rotation direction
            last_rotation_time = current_time

        if rotate_left:
            glRotatef(1, 0, 1, 0)  # Rotate to the left
        else:
            glRotatef(1, 1, 0, 0)  # Default rotation (right)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_cube()

        pygame.display.flip()
        pygame.time.wait(15)

if __name__ == '__main__':
    main()
