# order_scheduler_kucoin (PL version below)

## About program
A simple program designed to create 'Buy Limit' orders on the Kucoin exchange at a time specified by the user.
With just a few parameters, the user can generate an 'Buy Limit' order at time he prefers to.
The user is able to create order from python terminal. 
User has to enter all parameters in script before running the program except api_passphrase (the user will be asked for passphrase in terminal).



#### KuCoin API

    1. Go to https://www.kucoin.com/pl/account/sub and click 'Create Subaccount'
    2. Enter subaccount name, choose all permissions, set a password and save.
    3. Click transfer, transfer funds from master to subaccount - USDT transaction account (the amount you want) and confirm.
    4. In API section, click "Display"
    5. Click "Create API"
    6. Enter any API name, set API password (will be needed every time the bot is running), check 'trade', check 'no', constant validity, click 'next'.
    7. Approve changes with your trading password and google authenticator/sms.
    8. Save API data in a secure location.

#### GIT PROGRAM INSTALLATION

    1. Download and install the GIT program from https://git-scm.com/downloads - leave default settings in each step except the ones listed below.
    2. During installation (step 3), also select 'Add a Git Bash Profile to Windows Terminal'.
    3. In the fifth step of installation, select 'Use Notepad as Git's default editor'.
    4. In the seventh step of installation, select 'Use Git and optional Unix tools from the Command Prompt'.
    5. In the Configuring experimental options step, select 'Enable experimental support for pseudo consoles'.

#### PYTHON INSTALLATION

    1. Download and install Python from https://www.python.org/downloads/
    2. During installation, select "Add python.exe to PATH".

#### INSTALLING OUR BOT (all commands are entered without “”)

    1. Search for the previously installed Git Bash program on your computer and run it.
    2. In the terminal, type the command "cd Desktop" and enter.
    3. In the terminal, type the command "git" and enter.
    4. Type "git clone https://github.com/KBogielMiko/order_scheduler_kucoin.git" and enter.
    5. Type "cd order_scheduler_kucoin" and enter.
    6. Type "winpty python.exe -m pip install -r requirements.txt" and enter.
    7. Type "winpty python.exe main.py" and enter.
    8. Do not enter a password, close the Git Bash program.

#### PROGRAM CONFIGURATION

    1. Open the 'main.py' file in the order_scheduler_kucoin directory (right click and open with Notepad).
    2. api_key = 'HERE' enter your API key.
    3. api_secret = 'HERE' enter your API secret key.
    4. Save changes

#### PROGRAM STARTUP

    1. Open the 'main.py' file in the order_scheduler_kucoin directory (right click and open with Notepad).
    2. ticker = 'HERE' enter the trading pair you want to buy, e.g. BTC-USDT (no spaces).
    3. price = 'HERE' enter the price at which you want to buy, e.g 16057.45 (use a dot, comma does not work).
    4. amount = 'HERE' enter the amount you want to buy, e.g 0.51 (use a dot, comma does not work).




# PL Version


## O programie
Prosty program zaprojektowany do tworzenia zleceń "Buy Limit" na giełdzie Kucoin o wyznaczonym przez użytkownika czasie.
Używając kilku prostych parametrów, użytkownik może wygenerować zlecenie "Buy Limit" o wybranej przez siebie porze. Zlecenie można złożyć z poziomu terminala w python. Użytkownik musi wprowadzić wszystkie wymagane parametry przed włączeniem programu z wyjątkiem parametru api_passphrase (użytkownik zostanie zapytany o ten parametr w terminalu).


#### API KUCOIN
    1. Wejdź na stronę https://www.kucoin.com/pl/account/sub i kliknij w 'Utwórz subkonto'
    2. Podaj nazwę subkonta, wybierz wszystkie uprawnienia, ustal hasło i zapisz.
    3. Kliknij przelew - przelej z konta master na subkonto - Konto transakcyjne USDT (ilość która Cie interesuje) i kliknij potwierdź
    4. W sekcji API kliknij 'Wyświetl'
    5. Kliknij 'Utwórz API'
    6. Wpisz dowolną nazwę API, ustal hasło API (będzie nam potrzebne przy każdym odpaleniu bota), zaznacz handluj, zaznacz nie, okres ważności stały, kliknij 'dalej'
    7. Zatwierdź zmiany Twoim hasłem i google authenticator/sms
    8. Zapisz dane API w bezpiecznym miejscu

#### INSTALACJA PROGRAMU GIT
    1. Pobierz i zainstaluj program GIT ze strony: https://git-scm.com/downloads - w każdym kroku zostaw domyślne ustawienia oprócz niżej wymienionych
    2. Podczas instalacji (w 3 kroku) zaznacz dodatkowo 'Add a Git Bash Profile to Windows Terminal'
    3. W piątym kroku instalacji wybierz 'Use Notepad as Git's default editor'
    4. W siódmym kroku instalacji wybierz 'Use Git and optional Unix tools from the Command Prompt'
    5. W kroku Configuring experimental options wybierz 'Enable experimental support for pseudo consoles'

#### INSTALACJA PYTHON
    1. Pobierz i zainstaluj python ze strony: https://www.python.org/downloads/
    2. Podczas instalacji zaznacz 'Add python.exe to PATH'

#### INSTALACJA NASZEGO BOTA (wszystkie komendy wpisujemy bez "")
    1. Wyszukaj na komputerze wcześniej zainstalowany program Git Bash i uruchom go
    2. W terminalu wpisz komende "cd Desktop" i enter
    3. W terminalu wpisz komendę "git" i enter
    4. Wpisz "git clone https://github.com/KBogielMiko/order_scheduler_kucoin.git" i enter
    5. Wpisz "cd order_scheduler_kucoin" i enter
    6. Wpisz "winpty python.exe -m pip install -r requirements.txt" i enter
    7. Wpisz "winpty python.exe main.py"
    8. Nie wpisuj hasła, wyłącz program Git Bash

#### KONFIGURACJA PROGRAMU
    1. Otwórz plik main.py z katalogu order_scheduler_kucoin (prawym i otwórz za pomocą Notatnik)
    2. api_key = 'TUTAJ' Wpisz swój klucz API
    3. api_secret = 'TUTAJ' Wpisz swój secret API klucz
    4. Zapisz zmiany

#### URUCHOMIENIE PROGRAMU
    1. Otwórz plik main.py z katalogu order_scheduler_kucoin (prawym i otwórz za pomocą Notatnik)
    2. ticker = 'TUTAJ' wpisz parę handlową, którą chcesz kupić np. BTC-USDT (bez spacji)
    3. price = 'TUTAJ' wpisz cenę, po której chcesz kupić (używamy kropki, przecinek nie działa)
    4. amount = 'TUTAJ' wpisz ilość, jaką chcesz kupić (używamy kropki, przecinek nie działa)
    5. date = 'TUTAJ' wpisz dokładną datę i godzinę o której ma być złożona oferta w formacie 2023-01-06 20:03:00.500
    6. Zapisz zmiany
    7. Włącz Git Bash
    8. W terminalu wpisz komendę "cd Desktop" i enter
    9. Wpisz "cd order_scheduler_kucoin" i enter
    10. Wpisz "winpty python.exe main.py" i enter
    11. Podaj hasło do API i wciśnij enter (hasło nie będzie widoczne przy wpisywaniu, miej pewność, że wpisujesz je poprawnie)
    12. Czekamy do czasu z punktu 5 na zakończenie pracy programu
