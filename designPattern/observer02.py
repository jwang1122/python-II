class Event(object):
    def __repr__(self) -> str:
        return "::".join((self.type, str(self.percent)))        
    def getPercentage(self):
        return self.percent

class Observable(object):
    def __init__(self):
        self.callbacks = []
    def subscribe(self, callback):
        self.callbacks.append(callback)
    def fire(self, **attrs):
        e = Event()
        e.source = self
        for k, v in attrs.items():
            setattr(e, k, v)
        for fn in self.callbacks:
            fn(e)

class Job(Observable):
    def stateChanges(self, changes):
        self.changes = changes
        self.fire(type='progress', percent=self.changes)

job = Job()
def callback(e):
    if not e.getPercentage()>=100:
        print(e)
        return None
    print("Job complete")
    
job.subscribe(callback)
job.stateChanges(20)
job.stateChanges(50)
job.stateChanges(100)
