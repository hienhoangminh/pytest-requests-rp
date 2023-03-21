from config import SOAP_CALCULATOR_URL
from assertpy import assert_that
from lxml import etree
import requests
import logging
import json

LOGGER = logging.getLogger(__name__)

def test_divide_two_number():
    operator = 'Divide'
    args = {'divisor': 10, 'dividend': 5}
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': f'http://tempuri.org/{operator}'
    }
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Divide xmlns="http://tempuri.org/">
      <intA>{args['divisor']}</intA>
      <intB>{args['dividend']}</intB>
    </Divide>
  </soap:Body>
</soap:Envelope>
   """
    LOGGER.debug(f'URL: {SOAP_CALCULATOR_URL}')
    LOGGER.debug('Headers: ' + json.dumps(headers))
    LOGGER.debug('Payload: ' + payload)
    response = requests.post(url=SOAP_CALCULATOR_URL,data=payload,headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_xml = response.text
    tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
    result = tree.xpath("//*[local-name()='DivideResult']")[0].text
    assert_that(result).is_equal_to('2')
    
def test_multiply_two_number():
    operator = 'Multiply'
    args = {'first': 8, 'second': 4}
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': f'http://tempuri.org/{operator}'
    }
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Multiply xmlns="http://tempuri.org/">
      <intA>{args['first']}</intA>
      <intB>{args['second']}</intB>
    </Multiply>
  </soap:Body>
</soap:Envelope>
   """
    LOGGER.debug(f'URL: {SOAP_CALCULATOR_URL}')
    LOGGER.debug('Headers: ' + json.dumps(headers))
    LOGGER.debug('Payload: ' + payload)
    response = requests.post(url=SOAP_CALCULATOR_URL,data=payload,headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_xml = response.text
    tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
    result = tree.xpath("//*[local-name()='MultiplyResult']")[0].text
    assert_that(result).is_equal_to('32')   