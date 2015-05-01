#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
# Imports the NDB data modeling API
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class ShowQuiz(webapp2.RequestHandler):     #display the selected quiz to the user
    def get(self, testname): 
        quizname = testname #testname is all the remaining url after '/test/' e.g. the sample test url is '/test/three-sample-questions'
        try:
            loadedtests = ["Numeracy-Set-A1",
                           "Numeracy-Set-A2",
                           "Numeracy-Set-B1",
                           "Numeracy-Set-B2",
                           "Numeracy-Set-C1",
                           "Numeracy-Set-C2",
                           "Numeracy-Set-D1",
                           "Numeracy-Set-D2",
                           "Spelling-Set-A1",
                           "Spelling-Set-A2",
                           "Spelling-Set-B1",
                           "Spelling-Set-B2",
                           "Spelling-Set-C1",
                           "Spelling-Set-C2",
                           "Spelling-Set-D1",
                           "Spelling-Set-D2",
                           "Grammar-Set-A1",
                           "Grammar-Set-A2",
                           "Grammar-Set-B1",
                           "Grammar-Set-B2",
                           "Grammar-Set-C1",
                           "Grammar-Set-C2",
                           "Grammar-Set-D1",
                           "Grammar-Set-D2"]
            loadedtests.index(quizname) #throw an error if quizname is not a loaded test
        except: #if the loaded test is not found then just show the under construction quiz
            quizname = "UnderConstruction"
        
        template_values = {
            'quizname':quizname,
            }
        #return the quiz start page containing the test corresponding to the test/quizname folder
        #path = os.path.join(os.path.dirname(__file__), 'test_index.html')
        #self.response.out.write(template.render(path, template_values))

        #use jinja2 templates instead
        template = jinja_environment.get_template('test_index.html')
        self.response.out.write(template.render(template_values))   

        #self.response.out.write('Hello world!')
#        self.response.write('Hello world!')     
                
#application = webapp.WSGIApplication( 
#                                     [('/results', ProcessResults),
#                                      (r'/test/(.*)', ShowQuiz)],
#                                     debug=True) 

#process xml formatted quiz results and store in datastore
#note: ensure to account for namespaces correctly when using elementtree 
#http://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree


class Results(ndb.Model):
    someinfo = ndb.StringProperty(indexed=False)

class DevPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'barry': 'dataname',
        }
        template = jinja_environment.get_template('test_indexDEV.html')
        self.response.out.write(template.render(template_values))   

class ResultResponse(webapp2.RequestHandler):
    def post(self):
        #datafromquiz = self.request.get('VARIABLE_1')
        #results = Results(someinfo=datafromquiz)
        #results.put()
        #self.response.write('barry was here')
        #self.response.write('barry and nigel were here')
        #LC return a report populated with template values
        username = "jesus"
        template_values = {
            'username': username,
        }
        template = jinja_environment.get_template( 'results.html')
        self.response.out.write(template.render(template_values))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class lcisannoyed(webapp2.RequestHandler):
    def get(self):
        mycustomstuffing = "jesus"
        template_values = {
            'username': mycustomstuffing,
        }
        template = jinja_environment.get_template('results.html')
        self.response.out.write(template.render(template_values))   

class GimmeTheAnswers(webapp2.RequestHandler):
    def post(self):
        logging.info('these are the arguments')
        logging.info(self.request.arguments())
        logging.info(self.request.get('USER_NAME'))  # should return BARRY BARTOFSKY from the ocelot quiz
        logging.info('GimmeTheAnswers was requested')
        self.response.out.write("NOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!")


app = webapp2.WSGIApplication([
    ('/hello', MainHandler),
    ('/lc', lcisannoyed),
    ('/testresults', GimmeTheAnswers),
    ('/devlink', DevPage),
    ('/ajaxurl', AjaxResponse),    
    ('/report', ResultResponse),    
    (r'/test/(.*)', ShowQuiz)
], debug=True)