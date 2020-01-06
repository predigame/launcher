from idlelib.pyshell import main, ModifiedInterpreter
from idlelib.runscript import ScriptBinding
import predigame
import os, sys

def openidle(file):
    from idlelib.runscript import ScriptBinding
    import predigame
    import os, sys
    from idlelib.pyshell import main, ModifiedInterpreter

    def pg_run_module_event(self, event):
        filename = self.getfilename()
        dirname = os.path.dirname(filename)
        code = self.checksyntax(filename)
        if not code:
            return 'break'
        if not self.tabnanny(filename):
            return 'break'
        interp = self.shell.interp
        interp.restart_subprocess(with_cwd=False)

        interp.runcommand(f"""if 1:
            __file__ = {filename!r}
            import predigame, sys, os
            sys.argv = ['pred', __file__]
            os.chdir({dirname!r})
            predigame.bootstrap()
            \n""")

    ScriptBinding.run_module_event = pg_run_module_event
    sys.argv = ['idle', file]
    main()

if __name__ == '__main__':
    file = sys.argv[1]
    openidle(file)
