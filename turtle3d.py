from vpython import *
import math


class Turtle3D:
    """
    Classe que representa la tortuga en 3D

    Atributs
    --------
    angH : float
        Angle horitzontal
    angV : float
        Angle vertical
    position : vector
        Posició actual de la tortuga
    pinta : Bool
        Si True, la tortuga deixa rastre
    col : vector
        Color actual de la tortuga
    radi : float
        Radi actual de la tortuga
    """
    def __init__(self):
        """
        Construeix l'escena i inicializta els paràmetres de la tortuga.

        Paràmetres
        ----------
        Cap
        """
        print('Turtle3D in action...')
        scene.height = scene.width = 1000
        scene.autocenter = True
        scene.caption = "Logo3D's turtle"
        self.__angH = 0.0
        self.__angV = 0.0
        self.__position = vector(0, 0, 0)
        self.__pinta = True
        self.__col = vector(1, 0, 0)
        self.__radi = 0.5

    def color(self, R, G, B):
        """
        Modifica el color de la tortuga.

        Paràmetres
        ----------
        R: float
            component R del color
        G: float
            component G del color
        B: float
            component B del color
        """
        self.__col = vector(R, G, B)

    def left(self, ang):
        """
        Fa girar la tortuga cap a l'esquerra cambiant angH.

        Paràmetres
        ----------
        ang : float
            angle del gir
        """
        self.__angH += ang
        if self.__angH >= 360:
            self.__angH -= 360

    def right(self, ang):
        """
        Fa girar la tortuga cap a la dreta cambiant angH.

        Paràmetres
        ----------
        ang : float
            angle del gir
        """
        self.__angH -= ang
        if self.__angH >= 360:
            self.__angH -= 360

    def up(self, ang):
        """
        Fa girar la tortuga cap a dalt cambiant angV.

        Paràmetres
        ----------
        ang : float
            angle del gir
        """
        self.__angV += ang
        if self.__angV >= 360:
            self.__angV -= 360

    def down(self, ang):
        """
        Fa girar la tortuga cap a baix cambiant angV.

        Paràmetres
        ----------
        ang : float
            angle del gir
        """
        self.__angV += ang
        if self.__angV >= 360:
            self.__angV -= 360

    def forward(self, p):
        """
        Mou la tortuga cap endavant

        Paràmetres
        ----------
        p : float
            Unitats de moviment cap endavant
        """
        newposx = (math.sin((self.__angH*math.pi)/180) *
                   math.cos((self.__angV*math.pi)/180) * p)
        newposy = math.sin((self.__angV*math.pi)/180) * p
        newposz = (math.cos((self.__angH*math.pi)/180) *
                   math.cos((self.__angV*math.pi)/180) * p)
        if self.__pinta:
            bola1 = sphere(pos=self.__position, radius=self.__radi, color=self.__col)
            cilindre = cylinder(pos=self.__position,
                                axis=vector(newposx, newposy, newposz),
                                radius=self.__radi, color=self.__col)
            self.__position += vector(newposx, newposy, newposz)
            bola2 = sphere(pos=self.__position, radius=self.__radi, color=self.__col)
        else:
            self.__position += vector(newposx, newposy, newposz)

    def backward(self, p):
        """
        Mou la tortuga cap enrere

        Paràmetres
        ----------
        p : float
            Unitats de moviment cap enrere
        """
        newposx = (math.sin((self.__angH*math.pi)/180) *
                   math.cos((self.__angV*math.pi)/180) * -p)
        newposy = math.sin((self.__angV*math.pi)/180) * -p
        newposz = (math.cos((self.__angH*math.pi)/180) *
                   math.cos((self.__angV*math.pi)/180) * -p)
        if self.__pinta:
            bola1 = sphere(pos=self.__position, radius=self.__radi, color=self.__col)
            cilindre = cylinder(pos=self.__position,
                                axis=vector(newposx, newposy, newposz),
                                radius=self.__radi, color=self.__col)
            self.__position += vector(newposx, newposy, newposz)
            bola2 = sphere(pos=self.__position, radius=self.__radi, color=self.__col)
        else:
            self.__position += vector(newposx, newposy, newposz)

    def hide(self):
        """
        Modifica el atribut 'pinta', fent que la tortuga no deixi rastre.

        Paràmetres
        ----------
        Cap
        """
        self.__pinta = False

    def show(self):
        """
        Modifica el atribut 'pinta', fent que la tortuga deixi rastre.

        Paràmetres
        ----------
        Cap
        """
        self.__pinta = True

    def home(self):
        """
        Torna la tortuga a la posició inicial (0,0,0)

        Paràmetres
        ----------
        Cap
        """
        self.__position = vector(0, 0, 0)

    def radius(self, r):
        """
        Modifica el radi del rastre de la tortuga

        Paràmetres
        ----------
        r : float
            Nou radi
        """
        self.__radi = r
