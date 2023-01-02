# TI7
Strona na zaliczenie Technologii Internetowych
 
Wykorzystane technologie:
+ Python (Framework Flask)
+ Silnik wzorców HTML Jinja2
+ HTML, CSS(Bootstrap5), JavaScript (pakiet vis-timeline.js)
+ Baza danych SQLite
 
## Opis typów jachtów

Informacje na temat typu jachtów są zaciągane z bazy danych a strona jest generowana przy użyciu silnika Jinja2. Do aktualizacji zawartości strony wystarczy dodać nowy rekord do bazy danych.

![](screenshoty/Screenshot%20from%202023-01-02%2022-46-38.png)

## Tabela wypożyczeń

Do wizualizacji terminów wypożyczeń poszczególnych jednostek wykorzystano bibliotekę vis-timeline.js. Ponownie, wszystkie informacje są pobierane z bazy danych.

![](screenshoty/Screenshot%20from%202023-01-02%2022-47-06.png)

## Formularz kontaktowy

Stworzyłem formularz kontaktowy z walidacją zawartości przy użyciu biblioteki Bootstrap5.

![](screenshoty/Screenshot%20from%202023-01-02%2022-47-40.png)

## Responsywność

Całość wykorzystanych styli pochodzi z biblioteki Bootstrap5.

![](screenshoty/Screenshot%20from%202023-01-02%2022-50-43.png)

# Jak uruchomić

Do uruchomienia servera odpowiedzialnego za renderowanie strony potrzeba języka Python z zainstalowanym pakietem Flask. Serwer urucamia się następującą komendą:

```{shell}
flask --app yachs_webpage run
```
