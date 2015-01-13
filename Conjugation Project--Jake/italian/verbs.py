# coding=utf-8
# now you can add all the accents
# added the are tense for everything for future
pronouns = ["io", "tu", "lei", "lui", "Lei", "noi", "voi", "loro"]
imperfect_endings = ["vo", "vi","va","vamo","vate","vano"]
def expand(endings):
	to_duplicate = [endings[2]]
	split1 = endings[0:2]
	split2 = endings[2:5]
	return (split1 + to_duplicate + to_duplicate + split2)	

class verb:
	conjugations = {}
	def __init__(self, infinitive):
		stem_length = len(infinitive) - 3
		self.stem = infinitive[:stem_length]
	def conjugate(self, tense):
		endings = expand(self.conjugations.get(tense))
		return (dict(zip(pronouns, ([self.stem + x for x in endings]))))
class are(verb):
	conjugations = {
	"indicative" : ["o","ai","a","iamo","ate","ano"],
	"past participle" : ("ata" for x in xrange(len(pronouns))),
	"imperfect" : ["a" + x for x in imperfect_endings],
	"future" : ["ero", "erai", "era", "eremo", "erete", "eranno"]
	}
class gc_are(are):
	conjugations = {
	"indicative":["o", "hi", "a","hiamo", "ate" ],
	"past participle" : ("ata" for x in xrange(len(pronouns))),
	"imperfect" : ["a" + x for x in imperfect_endings],
	"future" : ["ero", "erai", "era", "eremo", "erete", "eranno"]
	}
class ere(verb):
	conjugations = {
	"indicative" : ["o", "i", "e", "iamo", "ete", "ono"],
	"past participle" : ("ata" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings],
	"future" : ["ero", "erai", "era", "eremo", "erete", "eranno"]
	}
class go(ere):
	conjugations = {
	"indicative" : ["go","i","e","iamo","ete","gono"],
	"past participle" : ("uto" for x in xrange(len(pronouns))),
	"imperfect" : ["e" + x for x in imperfect_endings],
	"future" : ["ero", "erai", "era", "eremo", "erete", "eranno"]
	}
class ire(verb):
	conjugations = {
	"indicative" : ["o", "i", "e", "iamo", "ite", "ono"],
	"past participle" : ("ito" for x in xrange(len(pronouns))),
	"imperfect" : ["i" + x for x in imperfect_endings],
	"future" : ["ero", "erai", "era", "eremo", "erete", "eranno"]
	}
class isc(ire):
	conjugations = {
	"indicative" : ["isco", "isci", "isce","iamo", "ite", "iscono"],
	"past participle" : ("ito" for x in xrange(len(pronouns))),
	"imperfect" : ["i" + x for x in imperfect_endings],
	"future" : ["ero", "erai", "era", "eremo", "erete", "eranno"]
	}

regulare_are = {
	"abitare":"live", 
	"giocare":"play", 
	"guardare":"watch", 
	"ascoltare":"listen", 
	"imparare":"learn", 
	"studiare":"study", 
	"sottolineare": "underline",
	"completare":"complete",
	"domandare":"ask",
	"insegnare":"teach",
	"sbagliare":"make a mistake",
	"frequentare":"attend a school",
	"arrovare":"arrive",
	"ascoltare":"listen (to)",
	"aspettare":"wait (for)",
	"ballare":"dance",
	"camminare":"walk",
	"cantare":"sing",
	"comprare":"buy",
	"desiderare":"desire, want",
	"domandare":"ask",
	"guardare":"look (at)",
	"imparare":"learn",
	"incontrare":"meet",
	"insegnare":"teach",
	"lasciare":"leave",
	"lavorare":"work",
	"mangiare":"eat",
	"parlare":"speak",
	"passare":"spend (time)",
	"pensare":"think",
	"sciare":"ski",
	"studiare":"study",
	"trovare":"find",
	"viaggiare":"travel",
	"visitare":"visit"

}
go_verbs = {
	"rimanere":"to remain",
}

gare_care = {
	"pagare":"pay for",
	"cercare":"look for"
}

regulare_ere = {
	"correre":"run", 
	"chiudere":"ask", 
	"scrivere":"write",
	"ripetere":"repeat",
	"prendere":"take (notes)",
	"crescere":"grow",
	"decidere":"decide",
	"discutere":"discuss",
	"dividere":"divide",
	"mettere":"put",
	"prendere":"take",
	"ridere":"laugh",
	"rispondere":"respond",
	"rompere":"break",
	"scendere":"descend",
	"spendere":"spend",
	"vedere":"see",
	"vivere":"live"
}

regulare_ire = {
	"dormire":"sleep", 
	"aprire":"open",
	"venire":"come",
	"offrire":"offer",
	"partire":"leave",
	"scoprire":"discover",
	"seguire":"follow",
	"servire":"serve"
}

regulare_isc = {
	"capire":"understand",
	"finire":"finish",
	"preferire":"prefer",
	"spedire":"send",
	"pulire":"clean"
}

#regulare_isc, regulare_ere, regulare_ire, regulare_are, gare_care, 
tipos = [regulare_isc, regulare_ere, regulare_ire, regulare_are, gare_care, go_verbs]