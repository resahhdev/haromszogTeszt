# Sallai András

class TriangleStore:
	FileName = 'data.txt'
	def storeAreaData(self, area):
		fp = open(self.FileName, 'a')
		fp.write(str(area) + '\n')
		fp.close()

	def storePeripheryData(self, peripehery):
		fp = open(self.FileName, 'a')
		fp.write(str(peripehery)+'\n')
		fp.close()

if __name__ == __main__:
	st = TriangleStore()
	st.storeAreaData(30)
	st.storePeripheryData(35)


