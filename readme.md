# Logo3D

Arxiu que documenta la segona pràctica de l'assignatura LP de l'alumne Joan Domingo Navarro, basada en la la implementació d'un intèrpret del llenguatge
Logo3D que permet pintar en un espai de tres dimensions.

## Part 1: intèrpret de Logo3D

El fitxer logo3d.g conte la gramàtica que l'intèrpret ha de fer servir. El fitxer logo3d.py 
és el programa principal, el que fa la traducció de la gramàtica a l'arbre que el fitxer Visitor.py 
fa servir per executar el que programa en Logo3D demani.

### Gramàtica

Recordem que la gramàtica ha d'acceptar instruccions tipus:
* Assignació: `a := 0`
* Lectura: `>> a`
* Escriptura: `<< a`
* Condicional: `IF a == 0 THEN a := a + 1 ELSE a := a - 1 END`
* Iteració WHILE: `WHILE a < 10 DO a := a + 1 END`
* Iteració FOR: `FOR i FROM 1 TO a*10 DO i := i + a END`
* Crida a un procediment: `suma(a, b)`

També ha de poder executar instruccions de la classe Turtle3D (explicat a la Part 3).

Per tant, logo3d.g permet cada un d'aquests tipus dintre d'un procediment definit com `PROC suma (a, b) IS << a + b END`, sempre suposant que les assignacions i els condicionals es poden expressar com productes, divisions, sumes o restes.

Per últim, també es permeten comentaris, que comencen amb `//` i acaben amb el final de línia `\n`.

### Programa principal

Aquest accepta d'entrada un fitxer amb el programa en Logo3D dins, amb terminació `.l3d`, 
i amb la possibilitat de fer que s'inicii l'execució en un procediment diferent de `main()`.
Junt amb el lexer i el parser de la gramàtica crea l'arbre del programa que s'està executant i crida al Visitor perquè l'executi.

### Visitor

El Visitor.py tracta els nodes de l'arbre que es creen al programa principal. En concret, primer emmagatzema tots els procediments dins del diccionari `self.func` i després inicia
l'execució, calculant les assignacions, simulant els bucles, comprovant els condicionals, permetent l'entrada i la sortida, etc.

La classe té 2 variables pròpies, el diccionari de variables `self.var`, que conté el nom de la variable i el seu valor, i el diccionari de funcions `self.func`, que conté el 
nom de la funció i una llista amb:
* Els paràmetres del procediment
* El node de les instruccions de dins del procediment (que ocupa l'últim espai de la llista).

També té la variable de la classe Turtle3D `self.tortuga` (explicat a la Part 3), que es manté a `None` si no hi ha cap instrucció de Turtle3D, evitant
així que s'iniciï la finestra gràfica si no és necessari.

## Part 2: classe Turtle3D

El fitxer turtle3d.py conte la classe Turtle3D que permet dibuixar en 3D amb la llibreria vpython.

Cada vegada que es crida a les funcions `up(a)`, `down(a)`, `left(a)` o `right(a)` es calcula l'angle horitzontal i el vertical, 
i cada vegada que es crida a `forward(m)` o `backward(m)`, es calcula el vector del moviment
segons els angles, es dibuixa una esfera a l'inici, un cilindre sobre el vector calculat i una esfera al final tots tres amb color `color(R,G,B)`. 

Tot això sempre que estigui `show()` activat i no `hide()`, que farà que res es pinti. També es pot tornar a la posició inicial amb `home()` 
i canviar el radi del traçat amb `radius(r)`.

## Part 3: extensió de l'interpet per usar Turtle3D

La gramàtica s'ha estès per poder acceptar crides a la classe Turtle3D per poder dibuixar 
usant el llenguatge Logo3D

S'afegeix a logo3d.g l'opció d'acceptar les instruccions definides a la Part 2, on només si hi ha alguna instrucció de la classe Turtle3D
s'iniciarà la finestra gràfica que permet dibuixar a Visitor.py.

## Ús dels fitxers

Per usar els fitxers d'aquesta pràctica, s'ha de fer el següent:

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g
python3 logo3d.py programa.l3d
```
La primera comanda permet generar, a partir de la gramàtica logo3d.g, els fitxers 
logo3dLexer.py, logo3dLexer.tokens, logo3dParser.py, logo3d.tokens i logo3dVisitor.py

La segona comanda executa el programa en logo3d programa.l3d

