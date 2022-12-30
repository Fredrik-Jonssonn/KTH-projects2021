# Kamratgranskning
Jag har granskat Tindras (github: tindrah) P-uppgift 168: minroj. Väldigt snabbt och översiktigt 
bygger hennes lösning på minröj-spelet sig i att lagra information om spelfältets rutor i listor
som t.ex spelplan_matrix som lagrar spelplanets format och hur många angränsande minor en ruta har och om rutan har en
mina på sig, koordinater_minor som lagrar minornas koordinater och spelplan_oppnade_rutor_matrix som lagrar
koordinater på rutorna som blivit öppnade av användaren. Listornas innehåll är det som bestämmer hur spelplanen ser
ut och då vad som kommer ritas upp för användaren.

Jag hade problem att testa den grafiska versionen av Tindras uppgift på linux och windows, den verkar bara funka på mac.

## Struktur
Jag anser att koden uppfyller detta krav eftersom att koden är tydligt uppdelat i klasser, metoder och funktioner utan
globala anrop. Uppdelningen är väldigt tydlig i den mening att t.ex
allt som påverkar spelplanen finns i spelplans klassen osv. Men jag undrar över syftet i uppdelningen på vissa
ställen i koden. T.ex vad syftet är med att göra topplistan till en klass kontra att ha den klassens metoder
självständigt som funktioner istället. Men eftersom kravet bara säger att koden ska
vara uppdelad i klasser, metoder och funktioner uppfyller koden kravet.
## Lagom stora
Vad som är lagom är så klart väldigt svårtolkat, men jag anser att koden har brister när det kommer
till funktioner/metoder/klassers storlek i vissa fall. Ett slående exempel på detta är 
spela_terminal funktionen som tar upp ungefär 130 rader där det finns en hel del utrymme att dela 
upp koden i mindre funktioner med mer entydiga syften. T.ex menyn som kommer upp efter spelet är över och hanteringen
av att lagra highscores skulle kunna vara sina egna funktioner. Även spelplan_skapa metoden är väldigt stor och
kan delas upp. T.ex så att en metod hanterar användarens inmatningar, en placerar minor, en räknar ut hur många
angränsande minor som finns. Jag tycker inte att koden helt uppfyller detta krav.
## Dokumenterad
Jag anser att koden uppfyller detta krav till 99%. Dokumentationen som finns är detaljerad och lättförståelig.
Kommentarerna gör ett bra jobb med att förklara funktionens/metodens syfte, parametrar och returvärden.
Det enda som saknas är dokumentation för programmets klasser.
## Undvik globala variabler
Koden uppfyller detta krav då den inte innehåller några globala variabler. 
## Undvik onödig kodupprepning
Jag anser att koden uppfyller detta krav. Jag hittar inget exempel av onödig kodupprepning i koden eller något ställe
där massa if satser används där det är uppenbart att en for loop ska användas. Inte heller en for loop istället
för ett matematiskt uttryck. 
## Undvik hårdkodning
Koden uppfyller detta krav då den inte innehåller några hårdkodade element. Vissa restriktioner placeras på användaren
som t.ex antal rader, kolumner, platser på topplistan mm. Men detta är enligt instruktion och inte pga hårdkodning.
Koden skulle kunna mycket enkelt kunna utvidgas till att skapa fler rader, kolumner och platser på topplistan osv.
## Utskrifterna
Koden uppfyller detta krav och jag anser att programmet har väldigt bra och detaljerade utskrifter. Spelinstruktionerna
är väldigt detaljerade och förståeliga. Alla felmeddelanden berättar exakt vad användaren gjort för fel och jag stötte
inte på ett enda tekniskt felmeddelande. Mycket kraft har lagts ned på detta vilket ger denna punkt ett stort + från mig. 
## Namn på variabler, funktioner, metoder och klasser
Koden uppfyller detta krav eftersom att alla namn är beskrivande och lättförståeliga. Listan som lagrar minors
koordinater heter just koordinater_minor, funktionen som ritar upp spelplanen i terminalen heter
just rita_upp_spelplan_terminal osv. Så här är det för alla namn i koden. Vissa namn kan jag tycka nästan är
för långa som t.ex funktionen kolla_om_alla_minor_flaggats_exklusivt. Den skulle kanske kunna heta
kolla_exklusiv_flaggning utan att minska förståeligheten. Men det påverkar inte om kravet uppfylls eftersom
kravet enbart var att namnen skulle vara beskrivande och lättförståeliga, vilket även kolla_om_alla_minor_flaggats_exklusivt
är. 



