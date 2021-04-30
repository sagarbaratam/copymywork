import logging

class logger:
    def log(self,msg):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger.info(msg)

#logit = logger()
#usage
#logit.log('info')
#logger().log('info')



    

    
