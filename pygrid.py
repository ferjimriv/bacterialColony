"""
====================================================================

PYGRID ENGINE 1.1
Copyright (C) <2014>  <Ericson Willians.>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

====================================================================
Engine written by Ericson Willians, a brazilian composer and programmer.

CONTACT: ericsonwrp@gmail.com
AS A COMPOSER: https://soundcloud.com/r-p-ericson-willians
YOUTUBE CHANNEL: http://www.youtube.com/user/poisonewein

====================================================================
"""

__author__ = 'EricsonWillians'

import pygame

class Grid():

    """
    A Pygrid Grid is a tessellation of n-dimensional Euclidean space by congruent bricks.
    """

    def __init__(self, wh, rwh):

        """
        The Grid constructor defines its size in width and height by elements.
        Every element is a grid rectangle, with a x and y position and fixed size.
        Both (wh) and (rwh) arguments are list objects of two indexes.

        self refers to each individual grid instance.
        The wh argument expects a list with two indexes (One for the width, one for the height).
        the rwh argument expects a list with two indexes (One for the fixed width of each rectangle, one for the fixed height of each rectangle)

        The keys list has two indexes.
        keys[0] is the width of the grid in elements.
        keys[1] is the height of the grid in elements.

        The x dictionary has keys[0] number of keys.
        Each key[0] key in x dictionary has an equivalent int value in pixels.
        The same applies to the y dictionary.

        Colors dictionary has basic colors as values of capitalized color-name string keys..
        """

        self.gridRectWidth = rwh[0]
        self.gridRectHeight = rwh[1]
        self.gridWidth = wh[0]
        self.gridHeight = wh[1]
        self.gridWidthInPixels = rwh[0]*wh[0]
        self.gridHeightInPixels = rwh[1]*wh[1]
        self.keys = [[x for x in range(self.gridWidth)], [x for x in range(self.gridHeight)]]
        self.x = dict(zip([x for x in self.keys[0]], [x for x in range(0, self.gridWidthInPixels, self.gridRectWidth)]))
        self.y = dict(zip([x for x in self.keys[1]], [x for x in range(0, self.gridHeightInPixels, self.gridRectHeight)]))
        self.colors = {"BLACK": (0,0,0), "WHITE": (255,255,255), "RED": (255,0,0), "GREEN": (0,255,0), "BLUE": (0,0,255)}

    def getX(self, key):

        """
        The getX() method expects a x-key as an argument. It returns its equivalent value in pixels.
        """

        return self.x.get(key)

    def getY(self, key):

        """
        The getY() method expects a y-key as an argument. It returns its equivalent value in pixels.
        """

        return self.y.get(key)

class Grect():

    """
    A Pygrid Grect is a grid rectangle.
    """

    def __init__(self, grid, x, y, color, isBackground):

        """
        The Grect constructor defines its position on the specified grid and its color.

        The grect x position in pixels is the specified x-key.
        The grect y position in pixels is the specified y-key.
        The grect width and height are grid-fixed (But they can be altered).
        The grect color is the specified color.
        The boolean defines if it shall be used as a background for the whole grid.
        """

        self.grid = grid
        self.x = grid.getX(x)
        self.y = grid.getY(y)
        self.w = grid.gridRectWidth
        self.h = grid.gridRectHeight
        self.color = color
        self.isBackground = isBackground

    def changeColor(self, color):

        """
        The changeColor() method expects a new color as an argument (A RGB-tuple with 3 indexes).
        """

        self.color = color

    def draw(self, surface):

        """
        The draw() method draws the grect in its current x and y positions.
        If the grect position is offset within the grid limits, it raises a TypeError.
        If it is a background, then it draws the grect of the size of the whole grid.
        """

        if self.isBackground == False:
            try:
                pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.h))
            except:
                pass
        elif self.isBackground == True:
            try:
                pygame.draw.rect(surface, self.color, (0, 0, self.grid.gridWidthInPixels, self.grid.gridHeightInPixels))
            except:
                pass

    def getGrid(self):

        """
        Returns the associated grid instance.
        """

        return self.grid

    def getColor(self):

        """
        Returns the grect RGB color (Tuple).
        """

        return self.color

    def isBackground(self):

        """
        Returns the isBackground boolean.
        """

        return self.isBackground

class GrectArray():

    """
    A Pygrid GrectArray is a sequence of grid rectangles.
    """

    def __init__(self, grid, isBackground):

        """
        The constructor defines to the GrectArray instance its own list and a boolean indicating if it is used as a background.
        """

        self.grid = grid
        self.array = []
        self.isBackground = isBackground

    def add(self, grect):

        """
        The add() method adds to the GrectArray instance a specified grect.
        """

        self.array.append(grect)

    def remove(self, grect):

        """
        The remove() method removes from the GrectArray the specified grect instance (If it exists).
        """

        if len(self.array) > 0:
            for i in self.array:
                if i == grect:
                    self.array.remove(grect)

    def addBackground(self, color):

        """
        The addBackground() method adds to the GrectArray a full-filling width and height sequence of grects in the specified color.
        Not recommended with large grids (Slow performance).
        """

        for i in range(self.grid.gridHeight):
            for j in range(self.grid.gridWidth):
                self.array.append(list())
                self.array[i].append(Grect(self.grid, j, i, color, False))

    def draw(self, surface):

        """
        The draw() method draws the sequence of grects.
        It loops through the sequence and draws each grect in their own x and y positions.
        If the position of a grect is offset within the grid limits, it raises a TypeError.

        If the background boolean is false, it draws it as just a simple sequence.
        If the background boolean is true, it draws it as a full-filling background.

        """

        if self.isBackground == False:
            try:
                if len(self.array) > 0:
                    for i in self.array:
                        pygame.draw.rect(surface, i.color, (i.x, i.y, self.grid.gridRectWidth, self.grid.gridRectHeight))
            except:
                pass

        elif self.isBackground == True:
            try:
                if len(self.array) > 0:
                    for i in self.array:
                        for j in i:
                            pygame.draw.rect(surface, j.color, (j.x, j.y, self.grid.gridRectWidth, self.grid.gridRectHeight))
            except:
                pass

    def getGrid(self):

        """
        Returns the associated grid instance.
        """

        return self.grid

    def isBackground(self):

        """
        Returns the isBackground boolean.
        """

        return self.isBackground

class Controller():

    """
    A Pygrid controller alters the positions of grects.
    """

    def __init__(self, grid, isArray, isWarper):

        """
        The constructor defines four basic directions, and a boolean indicating if the controlled target is a sequence or not.
        The isWarper boolean indicates if the Controller shall allow screen-warping.
        """

        self.grid = grid
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3
        self.isArray = isArray
        self.isWarper = isWarper

    def control(self, target, direction, step):

        """
        The control() method moves the specified grect or grect sequence target in a specified direction, by specified step and in the controller's grid.
        """

        if self.isArray == False:
            if direction == 0:
                try:
                    target.y -= self.grid.getY(step)
                except:
                    pass
                if self.isWarper == True:
                    if target.y < self.grid.getY(0):
                        target.y = self.grid.getY(self.grid.gridHeight-1)
            elif direction == 1:
                try:
                    target.y += self.grid.getY(step)
                except:
                    pass
                if self.isWarper == True:
                    if target.y > self.grid.getY(self.grid.gridHeight-1):
                        target.y = self.grid.getY(0)
            elif direction == 2:
                try:
                    target.x -= self.grid.getX(step)
                except:
                    pass
                if self.isWarper == True:
                    if target.x < self.grid.getX(0):
                        target.x = self.grid.getX(self.grid.gridWidth-1)
            elif direction == 3:
                try:
                    target.x += self.grid.getX(step)
                except:
                    pass
                if self.isWarper == True:
                    if target.x > self.grid.getX(self.grid.gridWidth-1):
                        target.x = self.grid.getX(0)

        elif self.isArray == True:
            if len(target.array) > 0:
                for i in target.array:
                    if direction == 0:
                        try:
                            i.y -= self.grid.getY(step)
                        except:
                            pass
                        if self.isWarper == True:
                            if i.y < self.grid.getY(0):
                                i.y = self.grid.getY(self.grid.gridHeight-1)
                    elif direction == 1:
                        try:
                            i.y += self.grid.getY(step)
                        except:
                            pass
                        if self.isWarper == True:
                            if i.y > self.grid.getY(self.grid.gridHeight-1):
                                i.y = self.grid.getY(0)
                    elif direction == 2:
                        try:
                            i.x -= self.grid.getX(step)
                        except:
                            pass
                        if self.isWarper == True:
                            if i.x < self.grid.getX(0):
                                i.x = self.grid.getX(self.grid.gridWidth-1)
                    elif direction == 3:
                        try:
                            i.x += self.grid.getX(step)
                        except:
                            pass
                        if self.isWarper == True:
                            if i.x > self.grid.getX(self.grid.gridWidth-1):
                                i.x = self.grid.getX(0)

    def getGrid(self):

        """
        Returns the associated grid instance.
        """

        return self.grid

    def isArray(self):

        """
        Returns the isArray boolean.
        """

        return self.isArray

    def isWarper(self):

        """
        Returns the isWarper boolean.
        """

        return self.isWarper