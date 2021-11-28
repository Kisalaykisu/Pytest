from pytest import mark 

##Smoke Testing :-- Smoking testing is a software testing technique performed post software 
##build to verify that
##the critical functionalities of software are working fine. It is executed before any detailed 
#functional or regression tests are executed. The main purpose of smoke testing is 
##to reject a software application with defects so that QA 
##team does not waste time testing broken software application.

@mark.ui
@mark.entertainment

def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('http://www.siriusxm.com/')
    assert True