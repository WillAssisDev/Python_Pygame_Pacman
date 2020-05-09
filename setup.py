import cx_Freeze
executables = [cx_Freeze.Executable('jogo.py')]
cx_Freeze.setup(
    name="Pacman",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": []}},
    executables=executables
)
#Build: python setup.py build