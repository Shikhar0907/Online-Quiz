import requests
import pprint
import unittest

class test_api(unittest.TestCase):

    def GetAPI_test(self):
        URL = "http://localhost:8000/admin/search"
        self.re = requests.get(URL)
        data = self.re.json()
        self.assertEqual(self.re.status_code,200)


    def PostAPI_test(self):
        URL = "http://localhost:8000/admin/create"
        data = {'category':'mat','questions':'ques','choice1':1,'choice2':2,'choice3':3,'choice4':4,'answers':3}
        self.re = requests.post(URL,data = data)

        self.assertEqual(self.re.status_code,201)


    def PutAPI_test(self):
        URL = "http://localhost:8000/admin/18/update/"
        data = {'category':'zat','questions':'ques','choice1':1,'choice2':2,'choice3':3,'choice4':4,'answers':3}
        self.re = requests.put(URL,data=data)
        self.assertEqual(self.re.status_code,200)

#test_api().GetAPI_test()
#test_api().PostAPI_test()
#test_api().PutAPI_test()

if __name__ == '__main__':
    unittest.main()

