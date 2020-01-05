
import pdb
from pdb import Pdb
import sys

# NOTE https://stackoverflow.com/questions/1140194/in-python-how-do-i-obtain-the-current-frame
class MPdb(Pdb,object):

    def trace_dispatch(self, frame, event, arg):
        print "trace_dispatch",frame,event,arg
        if self.quitting:
            return # None
        if event == 'line':
            return self.dispatch_line(frame)
        if event == 'call':
            return self.dispatch_call(frame, arg)
        if event == 'return':
            return self.dispatch_return(frame, arg)
        if event == 'exception':
            return self.dispatch_exception(frame, arg)
        if event == 'c_call':
            return self.trace_dispatch
        if event == 'c_exception':
            return self.trace_dispatch
        if event == 'c_return':
            return self.trace_dispatch
        print 'bdb.Bdb.dispatch: unknown debugging event:', repr(event)
        return self.trace_dispatch

    def set_trace(self, frame=None):
        """Start debugging from `frame`.

        If frame is not specified, debugging starts from caller's frame.
        """
        if frame is None:
            frame = sys._getframe().f_back
        self.reset()
        while frame:
            frame.f_trace = self.trace_dispatch
            self.botframe = frame
            frame = frame.f_back
        self.set_step()
        sys.settrace(self.trace_dispatch)

        # NOTE sys.settrace https://stackoverflow.com/questions/1692866/what-cool-hacks-can-be-done-using-sys-settrace
    
    def user_line(self, frame):
        print "user_line",frame
        super(MPdb,self).user_line(frame)

debug = MPdb()

debug.set_trace()

print "test"
# debug.do_l('')

print "done"
