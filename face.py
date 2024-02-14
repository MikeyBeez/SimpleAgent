''' This module can be used to give an agent emotions.  It's very basic, and has bugs, but it's a good start.  If you are wwriting an agent for kids, this should be especially helpful.  I hope it helps someone.'''   

import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Emotion Face")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Face properties
face_center = (screen_width // 2, screen_height // 2)
face_radius = 100
eye_y = face_center[1] - 40

# Function to draw eyes
def draw_eyes():
    eye_size = 20
    eye_offset = 40
    left_eye_center = (face_center[0] - eye_offset, face_center[1] - eye_offset)
    right_eye_center = (face_center[0] + eye_offset, face_center[1] - eye_offset)
    pygame.draw.circle(screen, WHITE, left_eye_center, eye_size)
    pygame.draw.circle(screen, WHITE, right_eye_center, eye_size)

# Function to draw mouth based on emotion
def draw_mouth(emotion):
    mouth_y = face_center[1] + 50
    if emotion == "happy":
        pygame.draw.arc(screen, WHITE, (face_center[0] - 50, mouth_y - 20, 100, 40), 3.14, 6.28, 4)  # Smile
    elif emotion == "sad":
        pygame.draw.arc(screen, WHITE, (face_center[0] - 50, mouth_y, 100, 40), 0, 3.14, 4)  # Frown
    elif emotion == "angry":
        pygame.draw.line(screen, WHITE, (face_center[0] - 50, mouth_y), (face_center[0] + 50, mouth_y), 4)  # Straight line
    elif emotion == "surprised":
        pygame.draw.circle(screen, WHITE, (face_center[0], mouth_y), 20)  # Open circle
    elif emotion == "quizzical":
        pygame.draw.line(screen, WHITE, (face_center[0] - 30, mouth_y), (face_center[0], mouth_y + 20), 4)  # Slight tilt

def draw_eyebrows(emotion):
    brow_y_offset = eye_y - 30  # Position above the eyes
    brow_length = 40

    if emotion == "happy":
        pass  # No eyebrows for happy
    elif emotion == "sad":
        pygame.draw.line(screen, WHITE, (face_center[0] - brow_length // 2, brow_y_offset), (face_center[0] + brow_length // 2, brow_y_offset - 20), 4)  # Left eyebrow
        pygame.draw.line(screen, WHITE, (face_center[0] + brow_length // 2, brow_y_offset), (face_center[0] - brow_length // 2, brow_y_offset - 20), 4)  # Right eyebrow
    elif emotion == "angry":
        pygame.draw.line(screen, WHITE, (face_center[0] - brow_length // 2, brow_y_offset - 20), (face_center[0] + brow_length // 2, brow_y_offset), 4)
        pygame.draw.line(screen, WHITE, (face_center[0] + brow_length // 2, brow_y_offset - 20), (face_center[0] - brow_length // 2, brow_y_offset), 4)
    elif emotion == "surprised":
        pygame.draw.arc(screen, WHITE, (face_center[0] - brow_length // 2, brow_y_offset - 20, brow_length, 20), 0, 3.14, 4)  # Left eyebrow
        pygame.draw.arc(screen, WHITE, (face_center[0] + brow_length // 2 - brow_length, brow_y_offset - 20, brow_length, 20), 0, 3.14, 4)  # Right eyebrow
    elif emotion == "quizzical":
        pygame.draw.line(screen, WHITE, (face_center[0] - brow_length // 2, brow_y_offset), (face_center[0], brow_y_offset - 20), 4)  # Left eyebrow
        pygame.draw.line(screen, WHITE, (face_center[0] + brow_length // 2, brow_y_offset), (face_center[0] + brow_length // 2, brow_y_offset), 4)  # Right eyebrow (no change)

# Start with a default emotion
current_emotion = "happy"

# Main game loop (see next comment for the rest)
# Main game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_emotion = "happy"
            elif event.key == pygame.K_2:
                current_emotion = "sad"
            elif event.key == pygame.K_3:
                current_emotion = "angry"
            elif event.key == pygame.K_4:
                current_emotion = "surprised"
            elif event.key == pygame.K_5:
                current_emotion = "quizzical"

    # Clear the screen
    screen.fill(BLACK)

    # Draw the face
    pygame.draw.circle(screen, BLACK, face_center, face_radius)
    draw_eyes()
    draw_mouth(current_emotion)
    draw_eyebrows(current_emotion)

    # Update the display
    pygame.display.flip()

pygame.quit()

