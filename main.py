from PyPDF2 import PdfFileMerger, PdfFileReader
from os import listdir
from os.path import isfile, join

pathToPdfs = 'pdfs'
onlyfiles = [f for f in listdir(pathToPdfs) if isfile(join(pathToPdfs, f))]

fileNumbers = []
for filePath in onlyfiles:
    filePath = filePath.split('.', 1)
    #print(filePath[0])
    fileNumbers.append(int(filePath[0]));

fileNumbers.sort()

""" for n in fileNumbers:
    print(n) """

# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
# I had 116 files in the folder that had to be merged into a single document
# Loop through all of them and append their pages
for fileNumber in fileNumbers:
    mergedObject.append(PdfFileReader('pdfs/'+ str(fileNumber)+ '.pdf', 'rb'))
    #mergedObject.append(PdfFileReader('6_yuddhakanda_' + str(fileNumber)+ '.pdf', 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write("output.pdf")