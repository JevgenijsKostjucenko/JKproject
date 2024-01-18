# QuickFilmRater

QuickFilmRater projekts tika izveidots, lai atvieglotu filmu vērtēšanas un atlases procesu no saraksta, kuru var izveidot, pamatojoties uz draugu ieteikumiem. Bieži vien draugi dalās ar daudzām viņu ieteiktajām filmām, un var būt ļoti nogurdinoši manuāli uzzināt par katru filmu.

"QuickFilmRater" ļauj ātri iegūt katras filmas vērtējumu no saraksta, ko var ātri izveidot, un ļauj lietotājam viegli salīdzināt filmas pēc reitinga, lai pieņemtu pārdomātāku lēmumu par to, kuras filmas ir vērts veltīt laiku, lai skatītos vai uzzinātu vairāk. par.

Projekta ideja ir vienkāršot un paātrināt no dažādiem avotiem savākto filmu vērtēšanas procesu. Projektā tiek izmantota automatizācija un integrācija ar reitingu vietnēm, lai ātri iegūtu vērtējumus, un lietotājam tiek nodrošināts ērts veids, kā salīdzināt filmas pēc reitingiem, lai izvēlētos tās, kas vislabāk atbilst viņu vēlmēm.

# "QuickFilmRater" priekšrocības:

Efektīvi: katras filmas vērtējuma novērtēšana aizņem tikai dažas sekundes.
Apzināts lēmums: lietotājs var viegli salīdzināt vērtējumus un atlasīt filmas ar augstākiem vērtējumiem.
Ērtības: projekts nodrošina vienkāršu un intuitīvu saskarni filmu ievadīšanai un vērtējumu iegūšanai.
"QuickFilmRater" darbojas, izmantojot automatizāciju, izmantojot Selēnu, lai mijiedarbotos ar vērtēšanas vietņu tīmekļa lapām. Šis process padara vērtējumu iegūšanu vienkāršāku, ātrāku un lietotājam draudzīgāku.

# Bibliotēkas:

Selēns: lai automatizētu mijiedarbību ar vērtēšanas vietņu tīmekļa lapām. Selēns ļauj programmatiski atvērt pārlūkprogrammu, ievadīt datus, meklēt un izgūt informāciju no tīmekļa lapām.

Chrome WebDriver: lai kontrolētu pārlūku Chrome no Python vides. Šis rīks tiek izmantots kopā ar Selēna bibliotēku, lai veiktu automatizētas darbības tīmekļa lapās.

re: izmanto, lai apstrādātu teksta informāciju, kas saņemta no tīmekļa lapām. Regulārās izteiksmes palīdz iegūt atbilstošus datus, piemēram, filmu vērtējumus.

time: lai izveidotu laika aizkavi.

# Programmatūras QuickFilmRater izmantošanas process ietver šādas darbības:

Lietojumprogrammas palaišana: lietotājs palaiž lietojumprogrammu un mijiedarbojas ar saskarni, izmantojot konsoles ievadi.

Filmas ievade: lietotājs ievada to filmu nosaukumus, kuras vēlas novērtēt. Ievade notiek no konsoles, un katrai ievadei tiek pievienota automātiska vērtējuma saņemšana no atbilstošās vērtēšanas vietnes.

Automatizēta vērtējumu meklēšana: programma izmanto Selenium un Chrome WebDriver, lai automātiski meklētu filmu vērtējumus filmaffinity vietnē. Lietotājs ievada tik daudz filmu, cik vēlas, un, kad visas filmas ir ievadītas, lietotājs pabeidz meklēšanu un saņem vērtējumus.

Vērtējumu salīdzinājums: iegūtie vērtējumi tiek parādīti lietotājam ērtā formātā, ļaujot viņam salīdzināt dažādu filmu vērtējumus.
