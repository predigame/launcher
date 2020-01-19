from idlelib.pyshell import main, ModifiedInterpreter
from idlelib.runscript import ScriptBinding
from idlelib.editor import EditorWindow
from idlelib import macosx
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

    def pg_overrideRootMenu(root, flist):
        from idlelib import mainmenu
        mainmenu.menudefs = [
         # underscore prefixes character to underscore
         ('file', [
           ('_Close', '<<close-window>>'),
           ('E_xit', '<<close-all-windows>>'),
           ]),
         ('run', [
           ('R_un Module', '<<run-module>>'),
           ]),
         ('options', [
           ('Configure _IDLE', '<<open-config-dialog>>'),
           None,
           ('Show _Code Context', '<<toggle-code-context>>'),
           ('Show _Line Numbers', '<<toggle-line-numbers>>'),
           ('_Zoom Height', '<<zoom-height>>'),
           ]),
         ('help', [
           ('Python _Docs', '<<python-docs>>'),
           ]),
        ]


    #EditorWindow.menu_specs = [
    #        ("file", "_File"),
    #        ("run", "_Run"),
    #        ("help", "_Help"),
    #]

    ScriptBinding.run_module_event = pg_run_module_event
    #macosx.overrideRootMenu = pg_overrideRootMenu
    sys.argv = ['idle', file]
    main()

if __name__ == '__main__':
    file = sys.argv[1]
    openidle(file)
