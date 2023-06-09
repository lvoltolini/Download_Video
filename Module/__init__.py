# Required Packages:

## This program checks if the machine has the required packages: 

# English 
fatal_message_en = 'The program encountered a fatal error and cannot continue. Press any key to exit the program: '

# Italian 
fatal_message_it = 'Il programma ha riscontrato un errore fatale e non può continuare. Premere un tasto qualsiasi per uscire dal programma: '


# Questa funzione termina il programma.

def fatal_error():
    input(fatal_message_en)
    quit()
    
# Dizionario con i pacchetti da scaricare.

packages_install_names = {
    'os' : 'os',
    'sys' : 'sys',
    'pytube' : 'pytube',
    'moviepy.video.io.VideoFileClip' : 'moviepy',
    'Python_image_rc' : 'Python_image_rc',
}


# Funzione per controllare i pacchetti

## Verifica se importlib è installato

try: import importlib
except: fatal_error

## Questa funzione controlla i pacchetti necessari.

def check_packages(packages):
    cont = 0
    for package in packages:
        try: importlib.import_module(package)
        except: 
            cont += 1
            print(f'Error: The package {packages[package]} is not installed. Try installing it using the command "pip3 install {package}" or check if it is a missing .py file')
        else: print(f'Successfully imported package {package}.')
    return cont

# Ora controlliamo se ci sono errori in qualche pacchetto:

if check_packages(packages_install_names) > 0:
    fatal_error()

## Importazione dei pacchetti

## Prima di tutto, definiamo i pacchetti ed i loro alias.

## Dizionario dei pacchetti:

packages_import_names = {
    'os' : 'os',
    'sys' : 'sys',
    'pytube' : 'pytube',
    'moviepy.video.io.VideoFileClip.VideoFileClip' : 'VideoFileClip',
    'Python_image_rc' : 'Python_image_rc',
}

## Funzione per importare i pacchetti:

def import_packs(packages):
    for package, alias in packages.items():
        globals()[alias] = importlib.import_module(package)
        print(f'Successfully imported {package} as {alias}.')
        

"--------------------------------------------------------------------------------"
"Loop per l'importazione:"
"--------------------------------------------------------------------------------"

# print(80*'-')
# import_packs(packages_import_names)

if __name__ == '__main__':
    for i in packages_import_names.values():
        print(i)

