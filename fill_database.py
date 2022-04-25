import os


pliki = ['asortyment', 'czynnosci', 'pracownicy', 'zarobki', 'zmiany', 'wlasciciele', 'zwierzeta']
for element in pliki:
    os.system('cmd /c "python {}.py"'.format(element))
