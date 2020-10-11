from store import TriangleStore
from calculate import TriangleCalc


class Triangle:
	def doit(self):
		tc = TriangleCalc()
		area = tc.getArea()
		periphery = tc.getPeriphery()

		TriangleStore().storeAreaData(area)
		TriangelStore().storePeripheryData(periphery)



triangle = Triangle()
triangel.doit()
