import unittest
import sfcsvimport as sdi
import uuid
import os
import string
import random

class TestSFCsvImport(unittest.TestCase):
    def tearDown(self):
        for root, dirs, files in os.walk(self.tempDir):
            for f in files:
                os.remove(os.path.join(root, f))
                
        os.removedirs(self.tempDir)

    def setUp(self):
        self.tempDir = uuid.uuid4().hex
        if not os.path.isdir(self.tempDir):
            os.mkdir(self.tempDir)

    def test_makeItPrintable(self):
        #random string for test
        testContent = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))

        #add unprintable escape char
        testContent += chr(27)

        #more random string
        testContent += ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
        
        #also we want to keep new lines
        testContent += "\n"

        #much more random string
        testContent += ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))

        result = sdi.makeItPrintable(testContent)
        self.assertNotIn(chr(27), result)
        self.assertIn('\n', result)
        
    
    def test_getFileContent(self):
        #temporary file to run test with random string
        testContent = ''.join(random.choices(string.ascii_uppercase + string.digits, k=500))
        testFileName = os.path.join(self.tempDir,uuid.uuid4().hex)
        testFile = open(testFileName, "w")
        testFile.write(testContent)
        testFile.close()
        
        result = sdi.getFileContent(testFileName)
        self.assertEqual(result,testContent)

if __name__ == '__main__':
    unittest.main()

        