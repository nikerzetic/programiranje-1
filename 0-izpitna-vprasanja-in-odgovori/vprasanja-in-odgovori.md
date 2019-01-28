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
- :: 
- @
- mem
- merge

### Vsote in induktivni tipi

- vsote: tipi, podani z možnimi variantami (type geometrijski_objekt = Tocka | Krog of float | Pravokotnik of float * float)
- algebrajski/induktivni tipi: rekurzivne vsote/zapisi

### Delovanje z indukcijo na seznamih in drevesih

- indukcija na seznamih: P([])∧(∀x,xs.P(xs)⇒P(x::xs))⟹∀ys.P(ys)
- indukcija na drevesih: P(P)∧(∀x,l,d.P(l)∧P(d)⇒P(S l x d)) ⇒ ∀t.P(t)

### Signature in moduli

- modul: zbirka tipov in vrednosti
- signature: tipi modulov

### Računska zahtevnost

- funkcija O

### Iskalna drevesa in AVL drevesa

- Dvojiško drevo je iskalno, če je koren levega otroka manjši, koren desnega otroka pa večji od korena starša in sta oba otroka iskalni drevesi.
- Iskalno drevo je AVL, če je razlika višin otrok največ 1 in sta oba otroka tudi AVL drevesi.
- leva in desno-leva rotacija

### Spremenljivi in nespremenljivi tipi

- z referencami (let r = ref 20; r := 10; !r)
- reference, array

### Predstavitev podatkov v pomnilniku

- list: verižni seznam; prazen/poln, element, mesto naslednjega elementa
- array: tabela; število elementov, elementi

### Razlika med verižnimi seznami in tabelami

- Pri tabeli je že na začetku določena dolžina, pri verižnem seznamu se ta lahko spremeni. Tabela je spremenljiva podatkovna struktura, medtem ko je seznam statičen tip. 

### Metoda deli in vladaj

- Strategija deli in vladaj ima tri korake: nalogo razdelimo na manjše podnaloge, podnaloge rekurzivno rešimo, dobljene rešitve združimo v rešitev prvotne naloge.

### Algoritmi za urejanje

- merge sort (urejanje z zlivanjem): seznam razbije na dva dela in se rekurzivno kliče na tako dobljenih seznamih, ki jih potem združi, tako da primerja prva elementa v vsakem podseznamu
- quick sort (hitro urejanje): izbere en element za pivot, prešteje število majših in ga postavi na pravo mesto; potem rekurzivno uredi seznama pred in po pivotu (pri štetju hkrati postavlja elemente, manjše od pivota, na začetek)
- random quick sort
- bubble sort: primerja sosednja dva elementa in večjega premakne v desno
- selection sort: poišče najmanjši element in ga postavi na prvo mesto
- insertion sort: vsak element ustavi med večjega in manjšega
- counting sort: prešteje število pojavitev vsakega elementa in nato po vrsti v seznam vrne primerno število kopij
- radix sort: elemente razdeli v kategorije glede na števko na mestu enic in jih vrne v seznam začenši z 0, postopek ponoovi za desetice, stotice, tisočice...

### Dinamično programiranje in memoizacija

- ko se rešitve prekrivajo med sabo
- ponavljanju izognemo na dva načina: rešitve pripravimo v ustreznem vrstnem redu ali si jih zapomnemo ob prvem izračunu (memoizacija)

### Bonus

- Python je proceduralni in imperativni jezik
- OCaml je funkcijski in deklarativni jezik
- Fisher-Yaits
