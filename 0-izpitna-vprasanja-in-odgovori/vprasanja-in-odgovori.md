# Izpitna vprašanja in odgovori

### Najpogostejši tipi v OCamlu

- cela števila (int)
- števila s plavajočo vejico (float)
- nizi (string)
- znaki (char)
- logične vrednosti (bool)
- seznami (list)
- nabori
- funkcije (fun)
- unit

### Primerjava med statičnimi in dinamičnimi tipi

- Statični tipi se preverijo preden se program zažene, medtem ko se dinamičnim po potrebi spreminja tip.

### Repni klici in repna rekurzija

- Klic funkcije je repen, če se izvede zadnji.
- Računlnik lahko pri repnem klicu delo opravi sproti, zato mu ga ni treba shranjevati.
- Funkcija je repno rekurzivna funkcija, če so vsi njeni rekurzivni tipi repni.

### Parametrični tipi in polimorfne funkcije

- parametrični tipi: vrednosti, ki imajo v tipih spremenljivke ('a, 'a list)

### Funkcije višjega reda in anonimne funkcije

- funkcije višjega reda: funkcije, ki za argumente sprejmejo druge funkcije
- anonimne funkcije: nepoimenovane funkcije (fun x -> ...)

### Delno uporabljene funkcije in curryiranje

- delno uporabljene funkcije: če funkciji dveh argumentov podamo en argument, dobimo funkcijo, enega argumenta, ki deluje na podanem
- curryirana funkcija: funkcija enega argumenta (prvega), ki vrne funckcijo enega argumenta (drugega) (fun x y = fun x -> fun y -> ...) (f x y = (f x) y)
- curryiranje: postopek, pri katerem funkcijo para spremenimo v curryirano funkcijo (f (x, y) -> f x y)

### Osnovne funkcije za delo na seznamih

- map: uporabi funkcijo na danem seznamu; v svoji osnovi je enaka funkciji fold_right
- fold_right: 
    let rec zlozi_desno f lst z = match lst with [] -> z | x :: xs -> f x (zlozi_desno f xs z)
- fold_left: ¸
    let rec zlozi_levo f z lst = match lst with [] -> z | x :: xs -> zlozi_levo f (f z x) xs

### Bonus

- Python je proceduralni in imperativni jezik
- OCaml je funkcijski in deklarativni jezik
