"""
A sample showing how to have a NAOqi service as a Python app.
"""

__version__ = "0.0.3"

__copyright__ = "Copyright 2015, Aldebaran Robotics"
__author__ = 'Anas Mazouni'
__email__ = 'anas.mazouni@stormix.co'


import qi

import stk.runner
import stk.events
import stk.services
import stk.logging

import cv2

class DetermineUserAction(object):
    "NAOqi service example (set/get on a simple value)."
    APP_ID = "com.aldebaran.DetermineUserAction"
    def __init__(self, qiapp):
        # generic activity boilerplate
        self.qiapp = qiapp
        self.events = stk.events.EventHelper(qiapp.session)
        self.s = stk.services.ServiceCache(qiapp.session)
        self.logger = stk.logging.get_logger(qiapp.session, self.APP_ID)
        # Internal variables
        self.level = 0

    @qi.bind(returnType=qi.Void, paramsType=[qi.Int8])
    def set(self, level):
        "Set level"
        self.level = level * 2

    def determinedAction(self):
        return "Rock"
    
    @qi.bind(returnType=qi.String, paramsType=[])
    def getAction(self):
        "Get level"
        return self.determinedAction()

    @qi.bind(returnType=qi.Void, paramsType=[])
    def reset(self):
        "Reset level to default value"
        return self.set(0)

    @qi.bind(returnType=qi.Void, paramsType=[])
    def stop(self):
        "Stop the service."
        self.logger.info("DetermineUserAction stopped by user request.")
        self.qiapp.stop()

    @qi.nobind
    def on_stop(self):
        "Cleanup (add yours if needed)"
        self.logger.info("DetermineUserAction finished.")

####################
# Setup and Run
####################

if __name__ == "__main__":
    stk.runner.run_service(DetermineUserAction)

