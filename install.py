import os

try:

    os.system('pip install tercuz')
    os.system('pip install --upgrade tercuz')
    from tercuz import Colors, Terminal, Animations
    Animations.Slide_Colors(string="Tercuz Installed !!!")

except Exception as e:
    print(e)
    print("Sorry unable to install tercuz.")
