# coding=Latin-1

pronouns = ["yo","tu","el","ella","usted","nosotros","ellos","ellas","ustedes"]
present_haber = ["he","has","ha","hemos","han"]
# a function that when passed the five forms returns a list expanded to all 9 pronouns
def expand(endings):
		singular = [endings[2]]
		plural = [endings[4]]
		split1 = endings[0:2]
		split2 = endings[2:4]
		return (split1 + singular + singular + split2 + plural + plural)

class verb: 
	conjucations = {}
	def __init__(self, infinitive):
		stem_length = len(infinitive) - 3
		self.stem = infinitive[:stem_length]
	def conjugate(self, tense):
		endings = expand(self.conjugations.get(tense))
		if tense == "future" or tense == "conditional":
			raise SystemExit
		if tense == ("present participle" or "past participle") :
			raise SystemExit
		return (dict(zip(pronouns, ([self.stem + x for x in endings]))))

class ar(verb):
	conjugations = {
	"indicative" : ["o","as","a","amos","an"],
	"preterite" : [u"é", "aste","o","amos","aron"],
	"imperfect" : ["aba","abas","aba",u"ábamos","aban"],
	"present participle" : ("ando" for x in xrange(len(pronouns) - 4)),
	"past participle" : ("ado" for x in xrange(len(pronouns) - 4)),
	"future" : [u"é",u"ás",u"á","emos",u"án"],
	"conditional" : [u"ía",u"ías",u"ía",u"íamos",u"ían"],
	"present subjunctive" : ["e","es","e","emos","en"],
	"imperfect subjunctive" : ["ara","aras","ara",u"áramos","aran",],
	"affirmative command" : ["o","a","e","emos","en"],
	"negative command" : ["o","es","e","emos","en"],
	}
class er(verb):
	conjugations = {
	"indicative" : ["o","es","e","emos","en"],
	"preterite" : [u"í", "iste",u"ió", "imos","ieron"],
	"imperfect" : [u"ía","ías","ía","íamos","ían"],
	"past participle" : ("ido" for x in xrange(len(pronouns)-4)),
	"present participle" :("iendo" for x in xrange(len(pronouns) - 4)),
	"future" : [u"é",u"ás",u"á","emos",u"án"],
	"conditional"  : [u"ía",u"ías",u"ía",u"íamos",u"ían"],
	"present subjunctive" : ["a","as","a","amos","an"],
	"imperfect subjunctive" : ["iera","ieras","iera",u"iéramos","ieran"],
	"affirmative command" : ["o","as","a","amos","an"],
	"negative command" : ["o","as","a","amos","an"]
	
	}
class ir(verb):
	conjugations = {
	"indicative" : ["o","es","e","imos","en"],
	"preterite" : [u'í', "iste",u"ió", "imos","ieron"],
	"imperfect" : [u"ía","íass","ía","ímosamos","ían"],
	"past participle" :("ido" for x in xrange(len(pronouns)-4)),
	"present participle" : ("iendo" for x in xrange(len(pronouns) - 4)),
	"future" : [u"é",u"ás",u"á","emos",u"án"],
	"conditional" : [u"ía",u"ía",u"ía",u"ía",u"ía"],
	"present subjunctive" : ["a","as","a","amos","an"],
	"imperfect subjunctive" : ["iera","ieras","iera",u"iéramos","ieran"],
	"affirmative command" : ["o","es","a","amos","an"],
	"negative command" : ["o","as","a","amos","an"],
	}
	
