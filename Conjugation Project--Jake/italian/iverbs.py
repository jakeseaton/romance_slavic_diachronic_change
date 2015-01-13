# write a function that takes the third form and makes it the third, fourth, and fifth. 
pronouns = ["io", "tu", "lei", "lui", "Lei", "noi", "voi", "loro"]
imperfect_endings = ["vo", "vi","va","vamo","vate","vano"]

essere = {
	"indicative":["sono","sai","e","e","e", "siamo", "siete","sono"],
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["ero","eri","era","era","era", "eravamo", "eravate", "erano"]
}
avere = {
	"indicative":["ho","hai","ha","ha","ha", "abbiamo", "avete","hanno"],
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings]
}
stare = {
	"indicative":["sto","stai","sta","sta","sta", "stiamo", "state","stanno"],
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["a" + x for x in imperfect_endings]
}
fare = {
	"indicative":["faccio","fai","fa","fa","fa", "facciamo", "fate","fanno"],
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["a" + x for x in imperfect_endings]
}
andare = {
	"indicative":["vade","vai","va","va","va", "andiamo","andate","vanno"],
	"past participle": ("ato" for x in xrange(len(pronouns))),
	"imperfect" : ["a" + x for x in imperfect_endings]
}
uscire = {
	"indicative":["esco","esci","esce","esce","esce", "usciamo", "uscite","escono"],
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["i" + x for x in imperfect_endings]
}
dare = {
	"indicative":["do","dai","da","da","da", "diamo", "date","danno"],
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["a" + x for x in imperfect_endings]
}
sapere = {
	"indicative":["so","sai","sa","sa","sa", "sappiamo", "sapete","sanno"],	
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings]
}
bere = {
	"indicative":["bevo","bevi","beve","beve","beve", "beviamo", "bevete","bevono"],	
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["derpe" + x for x in imperfect_endings]
}
dire = {
	"indicative":["dico","dici","dice","dice","dice", "diciamo", "dite","dicono"],	
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["i" + x for x in imperfect_endings]
}
tenere = {
	"indicative":["tengo","tieni","tiene","tiene","tiene", "teniamo", "tenete","tengono"],		
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings]
}
volere = {
	"indicative":["voglio","vuoi","vuole","vuole","vuole", "vogliamo", "volete","vogliono"],		
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings]
}
potere = {
	"indicative":["posso","puoi","puo","puo","puo", "possiamo", "potete","possono"],			
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings]
}
#fix
dovere = {
	"indicative":["devo","devi","deve","deve","deve", "dobbiamo", "dovete","devono"],			
	"past participle": ("derp" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings]
}
verbs = {
	"be":essere, 
	"have":avere, 
	"be":stare, 
	"do":fare, 
	"go":andare, 
	"go out":uscire, 
	"give":dire, 
	"know":sapere, 
	"drink":bere, 
	"say":dire,
	"keep":tenere,
	"desire":volere,
	"able to":potere,
	"need":dovere
}
def conjugate(verb, tense):
		return (dict(zip(pronouns, (verb.get(tense)))))

"""
Irregulars in past participle are on pg 151
"""
