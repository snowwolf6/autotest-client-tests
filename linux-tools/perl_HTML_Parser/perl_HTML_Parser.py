#!/bin/python
import os, subprocess
import logging

from autotest.client import test
from autotest.client.shared import error

class perl_HTML_Parser(test.test):

    """
    Autotest module for testing basic functionality
    of perl_HTML_Parser

    @author Basheer Khadarsabgari <bkhadars@in.ibm.com>                               ##
    """
    version = 1
    nfail = 0
    path = ''

    def initialize(self):
        """
        Sets the overall failure counter for the test.
        """
        self.nfail = 0
        logging.info('\n Test initialize successfully')

    def run_once(self, test_path=''):
        """
        Trigger test run
        """
        try:
            os.environ["LTPBIN"] = "%s/shared" %(test_path)
            ret_val = subprocess.call(test_path + '/perl_HTML_Parser' + '/perl-HTML-Parser.sh', shell=True)
            if ret_val != 0:
                self.nfail += 1

        except error.CmdError, e:
            self.nfail += 1
            logging.error("Test Failed: %s", e)

    def postprocess(self):
        if self.nfail != 0:
            logging.info('\n nfails is non-zero')
            raise error.TestError('\nTest failed')
        else:
            logging.info('\n Test completed successfully ')

