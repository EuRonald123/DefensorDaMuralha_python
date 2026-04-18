import cx_Freeze

executables = [cx_Freeze.Executable('jogo quase pronto.py')]

cx_Freeze.setup(
    name ="Jogo teste",
    options = {'build_exe': {'packages':['pygame'],
                            'include_files':['audios','Background','municoes','naves modelos','soldados','Vida']}},


    executables=executables
)
