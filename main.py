"""
Created by Damian Young

This is a simple chess game built with
the intention of learning the inner workings
of pygame

This is also my first attempt at building a large
scale game with advanced logic
"""

# Imports
import pygame
import os

# Constants
RED = (222, 79, 47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (222, 152, 47)
WINDOW_SIZE = [445, 445]

# Load image for pieces
WHITEROOK = pygame.image.load('imgs/WhiteRook.png')
WHITEPAWN = pygame.image.load('imgs/WhitePawn.png')
WHITEKNIGHT = pygame.image.load('imgs/WhiteKnight.png')
WHITEBISHOP = pygame.image.load('imgs/WhiteBishop.png')
WHITEQUEEN = pygame.image.load('imgs/WhiteQueen.png')
WHITEKING = pygame.image.load('imgs/WhiteKing.png')

# This sets the WIDTH and HEIGHT of each grid
WIDTH = 50
HEIGHT = 50
MARGIN = 5

# Class Definition for each Piece


class Piece():
    def __init__(self, x, y, column, row, name, color, img):
        self.x = x
        self.y = y
        self.column = column
        self.row = row
        self.name = name
        self.color = color
        self.img = img

    def draw(self):
        screen.blit(self.img, (int(self.x + MARGIN), int(self.y + MARGIN)))


class Pawn(Piece):
    def __init__(self, x, y, column, row, name, color, img):
        super().__init__(x, y, column, row, name, color, img)

    def show_valid_moves(self):
        if self.color == "white":
            pygame.draw.rect(screen, (255, 0, 0), [
                             self.x, self.y - 50, 50, 50])
            col = int(self.x // (WIDTH + MARGIN))
            row = ((self.y - 50) // (HEIGHT + MARGIN))
            return row, col
        elif self.color == "black":
            pygame.draw.rect(screen, (255, 0, 0), [
                             self.x, self.y + 50, 50, 50])


class Rook(Piece):
    def __init__(self, x, y, column, row, name, color, img):
        super().__init__(x, y, column, row, name, color, img)

    def show_valid_moves(self):
        for y in range(WINDOW_SIZE[0], 0, -55):
            pygame.draw.rect(screen, (255, 0, 0), [self.x, y, 50, 50])
            pygame.draw.rect(screen, (255, 0, 0), [y, self.y + 5, 50, 50])


class Bishop(Piece):
    def __init__(self, x, y, column, row, name, color, img):
        super().__init__(x, y, column, row, name, color, img)


class Knight(Piece):
    def __init__(self, x, y, column, row, name, color, img):
        super().__init__(x, y, column, row, name, color, img)

    def show_valid_moves(self):
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column + 1) * 55) + 5, ((self.row - 2) * 55) + 5, 50, 50])
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column - 1) * 55) + 5, ((self.row - 2) * 55) + 5, 50, 50])
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column + 2) * 55) + 5, ((self.row - 1) * 55) + 5, 50, 50])
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column - 2) * 55) + 5, ((self.row - 1) * 55) + 5, 50, 50])

        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column + 1) * 55) + 5, ((self.row + 2) * 55) + 5, 50, 50])
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column - 1) * 55) + 5, ((self.row + 2) * 55) + 5, 50, 50])
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column + 2) * 55) + 5, ((self.row + 1) * 55) + 5, 50, 50])
        pygame.draw.rect(screen, (255, 0, 0), [
                         ((self.column - 2) * 55) + 5, ((self.row + 1) * 55) + 5, 50, 50])


class Queen(Piece):
    def __init__(self, x, y, column, row, name, color, img):
        super().__init__(x, y, column, row, name, color, img)


class King(Piece):
    def __init__(self, x, y, column, row, name, color, img):
        super().__init__(x, y, column, row, name, color, img)


# Create a 2 dimensional array
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

# Initialize game window size and text
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Chess")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Used to monitor when user hits close button
done = False

# Initialize White Pieces
whitepawn1 = Pawn(5, 330, 0, 6, "pawn", "white", WHITEPAWN)
whitepawn2 = Pawn(60, 330, 1, 6, "pawn", "white", WHITEPAWN)
whitepawn3 = Pawn(115, 330, 2, 6, "pawn", "white", WHITEPAWN)
whitepawn4 = Pawn(170, 330, 3, 6, "pawn", "white", WHITEPAWN)
whitepawn5 = Pawn(225, 330, 4, 6, "pawn", "white", WHITEPAWN)
whitepawn6 = Pawn(280, 330, 5, 6, "pawn", "white", WHITEPAWN)
whitepawn7 = Pawn(335, 330, 6, 6, "pawn", "white", WHITEPAWN)
whitepawn8 = Pawn(390, 330, 7, 6, "pawn", "white", WHITEPAWN)

whiterook1 = Rook(5, 385, 0, 7, "rook", "white", WHITEROOK)
whiterook2 = Rook(390, 385, 7, 7, "rook", "white", WHITEROOK)

whiteknight1 = Knight(60, 385, 1, 7, "knight", "white", WHITEKNIGHT)
whiteknight2 = Knight(335, 385, 6, 7, "knight", "white", WHITEKNIGHT)

whitebishop1 = Bishop(115, 385, 2, 7, "bishop", "white", WHITEBISHOP)
whitebishop2 = Bishop(280, 385, 5, 7, "bishop", "white", WHITEBISHOP)

whitequeen = Queen(170, 385, 3, 7, "queen", "white", WHITEQUEEN)

whiteking = King(225, 385, 4, 7, "king", "white", WHITEKING)

# Initialize Black Pieces
blackpawn1 = Pawn(5, 55, 0, 1, "pawn", "black", WHITEPAWN)
blackpawn2 = Pawn(60, 55, 1, 1, "pawn", "black", WHITEPAWN)


def init_whitepieces():
    whitepieces = []
    whitepieces.append(whitepawn1)
    whitepieces.append(whitepawn2)
    whitepieces.append(whitepawn3)
    whitepieces.append(whitepawn4)
    whitepieces.append(whitepawn5)
    whitepieces.append(whitepawn6)
    whitepieces.append(whitepawn7)
    whitepieces.append(whitepawn8)

    whitepieces.append(whiterook1)
    whitepieces.append(whiterook2)

    whitepieces.append(whiteknight1)
    whitepieces.append(whiteknight2)

    whitepieces.append(whitebishop1)
    whitepieces.append(whitebishop2)

    whitepieces.append(whitequeen)

    whitepieces.append(whiteking)
    return whitepieces


def init_blackpieces():
    blackpieces = []
    blackpieces.append(blackpawn1)
    blackpieces.append(blackpawn2)
    return blackpieces


def draw_whitepieces(whitepieces):
    for x in whitepieces:
        x.draw()


def draw_blackpieces(blackpieces):
    for x in blackpieces:
        x.draw()


whitepieces = init_whitepieces()
blackpieces = init_blackpieces()

# Temp
clickedpos = None
selectedpiece = None

# Main Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            clickedpos = pygame.mouse.get_pos()
            column = int(clickedpos[0] // (WIDTH + MARGIN))
            row = int(clickedpos[1] // (HEIGHT + MARGIN))
            print("Click ", clickedpos, "Grid coordinates: ", row, column)
            # Check what space is clicked and if a piece is in that row/column
            for x in blackpieces:
                if x.row == row and x.column == column:
                    selectedpiece = x
                    break
                else:
                    selectedpiece = None

            for y in whitepieces:
                if y.row == row and y.column == column:
                    selectedpiece = y
                    break
                else:
                    selectedpiece = None

        # Check when mouse button is released, update piece selected
        # to that position
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            column = int(pos[0] // (WIDTH + MARGIN))
            row = int(pos[1] // (HEIGHT + MARGIN))
            print("Release ", pos, "Grid coordinates: ", row, column)

            validrow, validcol = selectedpiece.show_valid_moves()
            print(validrow, validcol)
            if selectedpiece is not None and validcol == column and validrow == row:
                selectedpiece.column = column
                selectedpiece.row = row
                selectedpiece.x = (MARGIN + WIDTH) * column + MARGIN
                selectedpiece.y = ((MARGIN + HEIGHT) * row + MARGIN) - 5

            selectedpiece = None

    # Game Logic
    screen.fill(BLACK)

    # Draw Items in Game
    COUNT = 0
    for row in range(0, 10):
        COUNT += 1
        for column in range(0, 10):
            if COUNT % 2:
                color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                     WIDTH,
                                     HEIGHT])
            else:
                color = BROWN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                     WIDTH,
                                     HEIGHT])
            COUNT += 1
    # Draw Pieces on Board
    draw_whitepieces(whitepieces)
    draw_blackpieces(blackpieces)

    if selectedpiece is not None:
        selectedpiece.show_valid_moves()

    # Limit to 60 frames per second
    clock.tick(60)

    # Display to screen
    pygame.display.flip()

pygame.quit()
