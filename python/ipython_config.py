
# sample ipython_config.py

# Copied from http://ipython.org/ipython-doc/dev/config/ipython.html
# and modified to automatically import Iplotclaw when ipython is started.

# You can modify this further if desired and then place in your directory
# IPYTHON_DIR/profile_default/
# See http://ipython.org/ipython-doc/dev/config/ipython.html
# for instructions on how to create and initialize this directory.

c = get_config()

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 20
c.InteractiveShellApp.extensions = [ ]
c.InteractiveShellApp.exec_lines = [
    'from pyclaw.plotters.Iplotclaw import Iplotclaw',
]
c.InteractiveShellApp.exec_files = [ 
    'pyclaw.plotters.Iplotclaw_help.py'
]
c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.deep_reload = True
c.InteractiveShell.editor = 'nano'
c.InteractiveShell.xmode = 'Context'

c.PromptManager.in_template  = 'In [\#]: '
c.PromptManager.in2_template = '   .\D.: '
c.PromptManager.out_template = 'Out[\#]: '
c.PromptManager.justify = True

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
 ('la', 'ls -al'),
 ('vi', 'vi')
]

