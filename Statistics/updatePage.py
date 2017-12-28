import successFail


resultOrganizer = successFail.successFail('Serenity/results.csv', 'index.html', 'statistics/weekPerformance.csv', 'img/barGraph.png')

resultOrganizer.checkFailures()

if resultOrganizer.areFails():
	resultOrganizer.setButton('btn btn-danger btn-lg')
else:
	resultOrganizer.setButton('btn btn-success btn-lg')

resultOrganizer.updateStatistics()
resultOrganizer.drawGraph()