'''
6.2 std mods
python - lib of std mods, some built into the interp
    - ex. winreg module is only on windows
    - sys universal
    - sys.path = list of strs that determines the interpreter's search path 4 mods
        - init to default path called 

dir() f(x):
    - used to find out which name a mod defines
    - returns li of strs

6.4 Pkgs *** this is important prof says
a way of structing python's module namespace
ex: module name A.B
    submodule B in pkg A
    - __init__.py files - treat dirs containing this as pkgs
    - import submod ref w/ full name
        import.sound.effects.echo     sound, effects = pkgs; echo.py = module
    - import submod ref w/o its pkg prefix
        import.sound.effects import echo
    - import only f(x)
        import.sound.effects.echo import echofilter
    - * everything gets imported frm pkg
        - can take long time importing all, some unwanted s/e
            - provide explicit idx of pkg

intra-pkg refs:
absolute imports: use complete reference submods of sibling pkgs
    - from sound.effects import echo
relative imports: use leading dots to indicate curr pkg pos
    - from . import echo    # curr
    - from .. import formats    # parent
    - from ..filters import equalizer   # specific 

pkgs in multiple dirs:
 __path__: special attri that pkgs support
    - can b modified
    - init to be li containing the dir that holds the pkg's __init__.py


'''