
import pdb
from pdb import Pdb
import sys

# NOTE https://stackoverflow.com/questions/1140194/in-python-how-do-i-obtain-the-current-frame
class MPdb(Pdb,object):

    def trace_dispatch(self, frame, event, arg):
        print "trace_dispatch",frame,event,arg
        super(MPdb,self).trace_dispatch(frame, event, arg)
        # if self.quitting:
        #     return # None
        # if event == 'line':
        #     return self.dispatch_line(frame)
        # if event == 'call':
        #     return self.dispatch_call(frame, arg)
        # if event == 'return':
        #     return self.dispatch_return(frame, arg)
        # if event == 'exception':
        #     return self.dispatch_exception(frame, arg)
        # if event == 'c_call':
        #     return self.trace_dispatch
        # if event == 'c_exception':
        #     return self.trace_dispatch
        # if event == 'c_return':
        #     return self.trace_dispatch
        # print 'bdb.Bdb.dispatch: unknown debugging event:', repr(event)
        # return self.trace_dispatch

    def set_trace(self, frame=None):
        super(MPdb,self).set_trace(frame=frame)
        # """Start debugging from `frame`.

        # If frame is not specified, debugging starts from caller's frame.
        # """
        # if frame is None:
        #     frame = sys._getframe().f_back
        # self.reset()
        # while frame:
        #     frame.f_trace = self.trace_dispatch
        #     self.botframe = frame
        #     frame = frame.f_back
        # self.set_step()
        # sys.settrace(self.trace_dispatch)

        # NOTE sys.settrace https://stackoverflow.com/questions/1692866/what-cool-hacks-can-be-done-using-sys-settrace
    
    def dispatch_line(self, frame):
        print "dispatch_line"
        super(MPdb,self).dispatch_line(frame)
        # if self.stop_here(frame) or self.break_here(frame):
        #     self.user_line(frame)
        #     if self.quitting: raise BdbQuit
        # return self.trace_dispatch

    def user_line(self, frame):
        print "user_line",frame
        super(MPdb,self).user_line(frame)
        # """This function is called when we stop or break at this line."""
        # if self._wait_for_mainpyfile:
        #     if (self.mainpyfile != self.canonic(frame.f_code.co_filename)
        #         or frame.f_lineno<= 0):
        #         return
        #     self._wait_for_mainpyfile = 0
        # if self.bp_commands(frame):
        #     self.interaction(frame, None)
    
    def interaction(self, frame, traceback):
        # NOTE cmdloop https://www.cnblogs.com/r00tuser/p/7515136.html
        # super(MPdb,self).interaction(frame, traceback)
        self.setup(frame, traceback)
        self.print_stack_entry(self.stack[self.curindex])
        self.cmdloop()
        # self.do_list('')
        self.forget()

    def dispatch_return(self, frame, arg):
        super(MPdb,self).dispatch_return(frame, arg)
        # if self.stop_here(frame) or frame == self.returnframe:
        #     try:
        #         self.frame_returning = frame
        #         self.user_return(frame, arg)
        #     finally:
        #         self.frame_returning = None
        #     if self.quitting: raise BdbQuit
        # return self.trace_dispatch

    def precmd(self, line):
        print "precmd",line
        return super(MPdb,self).precmd(line)

    def postcmd(self, stop, line):
        print "postcmd",stop,line
        return super(MPdb,self).postcmd(stop, line)
        
    def do_list(self, arg):
        print "do_list!!!!!!!!!!!!!!!!!",[arg]
        return super(MPdb,self).do_list(arg)

if __name__ == "__main__":
    pass
    debug = MPdb()

    debug.set_trace()
    print "breakpoint"

    print "done"
