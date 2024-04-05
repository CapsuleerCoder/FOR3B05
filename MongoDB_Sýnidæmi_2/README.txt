
Hægt er að keyra serverinn og hann hleður öllu sem sagt er á chattinu niður 
í safnið messages í gagnagrunninum chatserver2020.

Síðan má skoða skilaboðin í mongoskelinni með því að nota fyrst gagnagrunninn með 
skipuninni use chatserver2020 (þið getið líka alltaf gert show dbs til að sjá þá 
gagnagrunna sem til eru hjá ykkur, ef maður er byrjaður að nota grunn þá má líka gera 
þar show collections til að sjá hvaða söfn/töflur hann á) og gera svo:
db.messages.find() (eða db.messages.find().pretty() ef þið viljið það frekar)


 