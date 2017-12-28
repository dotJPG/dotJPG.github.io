import bs4, csv, pandas
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np




class successFail(object):

	resultsCSV = ''
	indexHTML = ''
	statisticsCSV = ''
	imagePath = ''
	failCount = 0
	
	
	
	def __init__(self, resultsCSV, indexHTML, statisticsCSV, imagePath):
		self.resultsCSV = resultsCSV
		self.indexHTML = indexHTML
		self.statisticsCSV = statisticsCSV
		self.imagePath = imagePath
				
	def checkFailures(self):
		with open(self.resultsCSV) as resultsFile:
			reader = csv.reader(resultsFile, delimiter = ',')
			for row in reader:
				if "FAILURE" == row[2]:
					self.failCount += 1
				if "ERROR" == row[2]:
					self.failCount += 1
					
	def areFails(self):
		if self.failCount > 0:
			return True
		else:
			return False 
		
		
	def count(self):
		return self.failCount
	
	
	def setButton(self, button):
		with open(self.indexHTML, "r") as index:
			txt = index.read()
			soup = bs4.BeautifulSoup(txt)
			failButton = soup.find('a')
			failButton['class'] = button
			
		with open(self.indexHTML, "w") as out:
			out.write(str(soup))
			
	def updateStatistics(self):
	
		lines = []
		with open(self.statisticsCSV, "r") as stats:
			reader = csv.reader(stats, delimiter= ',')
			for row in reader:
				lines.append(row)

		for line in lines:
			print (line)
			
		lines.pop(1)
		lines.append([datetime.strftime(datetime.now(), '%b %d'), str(self.count())])
			

		for line in lines:
			print (line)
			
			
		with open(self.statisticsCSV, "w") as statsout:
			writer = csv.writer(statsout, dialect='excel', lineterminator = '\n')
			for line in lines:
				writer.writerow(line)
						

	def drawGraph(self):
		colnames = ['Date', 'Errors']
		data = pandas.read_csv(self.statisticsCSV, header=None, names=colnames)

		dates = data.Date.tolist()

		errors = data.Errors.tolist()
	
		y_pos = range(len(dates) - 1)


		plt.bar(y_pos, errors[1:], align='center', color='#f09100')
		plt.xticks(y_pos, dates[1:])
		plt.ylim([0,5])
		plt.xlabel('Day')
		plt.ylabel('Errors & Failures')
		plt.title('Site Link Performance')
		plt.savefig(self.imagePath)
				
						
				
		