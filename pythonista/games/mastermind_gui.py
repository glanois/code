from scene import *
import random
import math
    
''' Returns True if the two points are within the distance specified. '''
def near(x0, y0, x1, y1, d):
    distance = math.sqrt(math.pow(x1-x0, 2) + math.pow(y1-y0, 2))
    return True if distance <= d else False


class MastermindGame(Scene):
    ''' Constructor '''
    def __init__(self):
        self.palette = {
            'Red'    : { 'R' : 1, 'G' : 0, 'B' : 0 },
            'Green'  : { 'R' : 0, 'G' : 1, 'B' : 0 },
            'Blue'   : { 'R' : 0, 'G' : 0, 'B' : 1 },
            'White'  : { 'R' : 1, 'G' : 1, 'B' : 1 },
            'Yellow' : { 'R' : 1, 'G' : 1, 'B' : 0 },
            'Orange' : { 'R' : 1, 'G' : 0.8, 'B' : 0 },
            'Brown'  : { 'R' : 0.5, 'G' : 0.3, 'B' : 0.1 },
            'LightBrown'  : { 'R' : 0.6, 'G' : 0.4, 'B' : 0.2 }
        }
        self.Menu   = [ 
            { 'color' : 'Red',    'x' : 0 },
            { 'color' : 'Green',  'x' : 0 }, 
            { 'color' : 'Blue',   'x' : 0 }, 
            { 'color' : 'White',  'x' : 0 }, 
            { 'color' : 'Yellow', 'x' : 0 }, 
            { 'color' : 'Orange', 'x' : 0 }]

        self.yMenu = 50
        self.xEdge = 50
        self.yBase = self.yMenu + self.xEdge
        self.Size  = 30
        self.Span  = self.Size + 20
        x = self.xEdge
        for p in self.Menu:
            p['x'] = x
            x = x + self.Span

        self.colors = {
            0 : 'Red',
            1 : 'Blue',
            2 : 'Green',
            3 : 'White',
            4 : 'Yellow',
            5 : 'Orange' }
            
        self.resetBoard()
        
    ''' New game. '''
    def resetBoard(self):
        self.Board = [ ['Brown']*4 for x in xrange(10) ]
        self.Hints = [ ['Brown']*4 for x in xrange(10) ]
        self.choice = 0
        self.guesses = 0
        self.won = False
        self.lost = False
        
        # Generate the code.
        self.code = []
        for i in range(4):
            self.code.append(self.colors[int(random.random() * 6.0)])

    ''' This will be called before the first frame is drawn. '''
    def setup(self):
        stroke(0,0,0)    # line color
        stroke_weight(2) # line thickness

    def drawCircle(self, x, y, color, r):
        fill(
            self.palette[color]['R'], 
            self.palette[color]['G'], 
            self.palette[color]['B'])
        ellipse(x, y, r, r)

    def drawPeg(self, row, col, color):
        self.drawCircle(
            self.xEdge+col*self.Span, 
            self.yBase+row*self.Span, 
            color,
            self.Size)

    def drawHints(self, row):
        x = self.xEdge + 4 * self.Span
        y = self.yBase + row * self.Span
        self.drawCircle(
            x, 
            y,
            self.Hints[row][0], 
            self.Size/2)
        self.drawCircle(
            x + self.Span/2, 
            y,
            self.Hints[row][1], 
            self.Size/2)
        self.drawCircle(
            x + self.Span/2,
            y + self.Span/2, 
            self.Hints[row][2], 
            self.Size/2)
        self.drawCircle(
            x,
            y + self.Span/2, 
            self.Hints[row][3], 
            self.Size/2)         

    ''' This draws the current contents of the board. '''
    def draw(self):
        background(
            self.palette['LightBrown']['R'],
            self.palette['LightBrown']['G'],
            self.palette['LightBrown']['B'])
        
        # Draw the "menu" of peg colors available.
        for p in self.Menu:
            self.drawCircle(
                p['x'], 
                self.yMenu, 
                p['color'],
                self.Size)
            
        # Draw each guess and the hints for each guess.
        for r in xrange(0, 10):
            for c in xrange(0, 4):
                self.drawPeg(r, c, self.Board[r][c])
            self.drawHints(r)
        
        if self.lost:    
            # Draw the code.
            for c in range(4):
                self.drawPeg(10, c, self.code[c])

    ''' Scene function called for every touch. '''
    def touch_began(self, touch):
        if self.won == True or self.lost == True:
            self.resetBoard()
        else:
            tx = int(touch.location.x)
            ty = int(touch.location.y)
            for p in self.Menu:
                if near(tx, ty, p['x'], self.yMenu, self.Size):
                    # Record their choice.
                    self.Board[self.guesses][self.choice] = p['color']
                    self.choice += 1
                
                    # Once they make 4 choices, score it, and compute hints.
                    if self.choice == 4:
                        guess = []
                        for i in range(4):
                            guess.append(self.Board[self.guesses][i])
                    
                        # Score their guess.
                        red = 0
                        white = 0
                        counted = [False]*4

                        # Look for correct color in correct position.
                        # Mark any matches as already counted.
                        h = 0
                        for i in range(4):
                            if guess[i] == self.code[i]:
                                red += 1
                                counted[i] = True
                                self.Hints[self.guesses][h] = 'Red'
                                h += 1

                        # Look for correct color in wrong position
                        # (and not already counted in the right position.
                        for i in range(4):
                            if self.code[i] in guess and not counted[i]:
                                white += 1
                                self.Hints[self.guesses][h] = 'White'
                                h += 1
                    
                        # Start accumulating next choices into next guess.        
                        self.choice = 0
                    
                        # Detect victory.
                        if red == 4:
                            self.won = True
                        else:
                            if self.guesses < 10:
                                # Count this guess.
                                self.guesses += 1
                        
                            # Detect defeat.
                            if self.guesses == 10:          
                                self.lost = True
     
run(MastermindGame())
