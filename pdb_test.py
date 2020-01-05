from pdb import Pdb
class TestPdb(Pdb,object):
    def interaction(self, frame, traceback):
        self.setup(frame, traceback)
        self.print_stack_entry(self.stack[self.curindex])
        # self.cmdloop()
        arg = 'l'
        self.precmd(arg)
        self.onecmd(arg)

        self.forget()

if __name__ == "__main__":

    def combine(s1,s2):      # define subroutine combine, which... 
        s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ... 
        s3 = '"' + s3 +'"'   # encloses it in double quotes,... 
        return s3            # and returns it. 
    a = "aaa"
    b = "bbb"
    TestPdb().set_trace() 
    final = combine(a,b) 
    print final