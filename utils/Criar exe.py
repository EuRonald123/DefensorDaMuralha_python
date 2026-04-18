import subprocess
import sys
import os
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"])
#"--icon", "utils/icons/icone.ico",

for pasta in ["build", "dist", "executavel"]:
    if os.path.exists(pasta):
        shutil.rmtree(pasta)

comando = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--windowed",
    "--clean",
    "--name", "Defensor da Muralha",
    "--version-file", "secrets/version_info.txt",
    "--icon", "assets/icons/icone.ico",
    "--add-data", "assets/backgrounds;assets/backgrounds",
    "--add-data", "assets/audios;assets/audios",
    "--add-data", "assets/vida;assets/vida",
    "--add-data", "assets/icons;assets/icons",
    "Game.py"
]

resultado = subprocess.run(comando)

if resultado.returncode == 0:
    dist_dir = os.path.join(os.getcwd(), "dist")
    for pasta in ["assets/backgrounds", "assets/vida", "assets/audios", "assets/soldados", "assets/munitions", "assets/icons"]:
        src = os.path.join(os.getcwd(), pasta)
        dst = os.path.join(dist_dir, pasta)
        if os.path.exists(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    
    # Renomear pasta dist para executavel
    if os.path.exists("executavel"):
        shutil.rmtree("executavel")
    os.rename("dist", "executavel")
    
    print("✅ Executável criado em: executavel/Defensores da Muralha.exe")
else:
    print("❌ Erro ao criar executável")