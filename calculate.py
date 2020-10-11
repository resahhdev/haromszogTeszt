# Rékási József

class TriangleCalc:

    self.area = 0
    self.periphery = 0

    def __init__( self ):
        self.choosing()

    def choosing( self ):
        chose = int( input( "Kerület: [1], Terület: [2]\nVálassz: " ))

        if( chose == 1 ):
            self.calcPeriphery()
        else:
            self.calcArea()

    def getData( self, text ):
        data = float( input( text ))
        return data

    def calcArea( self ):
        sideBase = self.getData( "Alap: " )
        high = self.getData( "Magasság: " )

        self.area = ( sideBase * high ) / 2

    def calcPeriphery( self ):
        sideA = self.getData( "A oldal: " )
        sideB = self.getData( "B oldal: " )
        sideC = self.getData( "C oldal: " )

        self.periphery = sideA + sideB + sideC

    def getArea( self ):
        return self.area

    def getPeriphery( self ):
        return self.periphery
