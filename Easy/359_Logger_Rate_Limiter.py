class Logger:
    def __init__(self):
        self.log = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not message in self.log.keys():
            self.log[message] = [timestamp]
            return True
        else: # already in the log, get the lastest timestamp
            last_time = self.log[message][-1]
            if timestamp < last_time + 10:
                return False
            else:
                self.log[message].append(timestamp)
                return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
