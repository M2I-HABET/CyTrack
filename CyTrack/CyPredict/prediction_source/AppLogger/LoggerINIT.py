'''
Created on Dec 17, 2016

@author: matth
'''

import logging
import logging.config
import Configuration.config as conf

        
dictLogConfig = {
    "version":1,
    "handlers":{
                "fileHandler":{
                    "class":"logging.FileHandler",
                    "formatter":"myFormatter",
                    "filename":"appLog.log"
                    }
                },        
    "loggers":{
        conf.appname:{
            "handlers":["fileHandler"],
            "level":"INFO",
            }
        },

    "formatters":{
        "myFormatter":{
            "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }     
     
def initialize_Logger():
    
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger(conf.appname)
    logger.info("Logging started")