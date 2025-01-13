# Python Series: Class 43 - Introduction to PyGame

## Overview

In this class, we will learn the basics of game development using the **PyGame** library. PyGame is a set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be easy to use for beginners. In this class, we'll cover creating a simple game window, handling user input, and drawing objects on the screen.

---

### What You'll Learn:
1. **Introduction to PyGame**
2. **Installing PyGame**
3. **Setting Up the Game Window**
4. **Handling User Input**
5. **Drawing Objects on the Screen**
6. **Game Loop and Frame Rate**
7. **Adding Sound and Music (Optional)**

---

## 1. Introduction to PyGame

**PyGame** is a Python library that is used to create 2D games and multimedia applications. It provides functionality for handling game objects, images, sounds, and much more. It's great for beginners who want to create simple games and learn the concepts behind game development.

Some of the key features of PyGame include:
- Handling graphics, sound, and music.
- Detecting user input (keyboard, mouse).
- Collision detection.
- Sprites and animations.
- Creating game loops and managing frame rates.

---

## 2. Installing PyGame

To get started, you'll need to install the **PyGame** library. You can do so using `pip`:

```bash
pip install pygame
```

---

## 3. Setting Up the Game Window

The first step in creating any PyGame application is to set up the game window. This is the area where all the game content will be displayed.

### Example Code:

```python
import pygame

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Example")

# Game loop
running = True
while running:
    # Handle events (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB format)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()
```

In this example:
- We initialize PyGame using `pygame.init()`.
- We create a window with a resolution of 800x600 using `pygame.display.set_mode()`.
- We enter the game loop where we constantly check for events (e.g., closing the window).
- We fill the window with a black color and update the display using `pygame.display.update()`.

---

## 4. Handling User Input

PyGame makes it easy to handle keyboard and mouse input. You can detect when a key is pressed or a mouse button is clicked.

### Example Code (Handling Keyboard Input):

```python
import pygame

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Keyboard Input Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
    
    screen.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
```

In this example:
- We use `pygame.KEYDOWN` to detect when a key is pressed.
- We check for specific keys (left and right arrows) using `event.key`.

### Example Code (Handling Mouse Input):

```python
import pygame

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Mouse Input Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                print(f"Mouse clicked at {event.pos}")
    
    screen.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
```

In this example:
- We use `pygame.MOUSEBUTTONDOWN` to detect when a mouse button is pressed.
- We check for the left mouse button (`event.button == 1`).

---

## 5. Drawing Objects on the Screen

PyGame allows you to draw simple shapes like rectangles, circles, and lines on the screen.

### Example Code (Drawing a Rectangle):

```python
import pygame

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Drawing Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    
    # Draw a red rectangle (position, width, height)
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
    
    # Update the display
    pygame.display.update()

pygame.quit()
```

In this example:
- We use `pygame.draw.rect()` to draw a red rectangle at the specified coordinates `(100, 100)` with width `200` and height `150`.

### Example Code (Drawing a Circle):

```python
import pygame

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Circle Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    
    # Draw a green circle (center, radius)
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 100)
    
    # Update the display
    pygame.display.update()

pygame.quit()
```

In this example:
- We use `pygame.draw.circle()` to draw a green circle at the center `(400, 300)` with a radius of `100`.

---

## 6. Game Loop and Frame Rate

A game loop is the core of any game, where the game continuously updates and renders frames. The game loop runs until the user closes the window. To ensure that the game runs at a consistent speed, we control the frame rate.

### Example Code (Setting Frame Rate):

```python
import pygame

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Frame Rate Example")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    
    # Draw a red rectangle
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
    
    # Update the display
    pygame.display.update()
    
    # Set the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
```

In this example:
- We create a `pygame.time.Clock()` object to control the frame rate.
- The `clock.tick(60)` method limits the frame rate to 60 frames per second (FPS).

---

## 7. Adding Sound and Music (Optional)

PyGame also supports adding sounds and background music to your game. You can use `pygame.mixer` for sound effects and background music.

### Example Code (Playing Sound):

```python
import pygame

# Initialize PyGame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init()

# Load a sound
sound = pygame.mixer.Sound('sound.wav')

# Play the sound
sound.play()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

In this example:
- We use `pygame.mixer.Sound()` to load a sound file and play it with `sound.play()`.

---

## Task

1. **Create a game window with a background color and a rectangle that moves with arrow keys.**
2. **Add mouse interaction to your game where a click changes the color of the rectangle.**
3. **Create a simple game loop where the player controls a circle, and the goal is to catch a randomly appearing square.**

---