
import vocab
import random
"""from threading import Timer
import time
import timer"""

# Verbal?
print "Welcome to Verble!"

# Mode
ask_for = "Italian"

# fill a dictionary with the words to be practiced
words = {}
for x in vocab.all_vocab:
	words.update(x)
# account for English mode
if (ask_for == "English"):
	print "true"
	words = dict (zip(words.values(), words.keys()))

# calculate the objective, the number of words to be learned
objective = len(words)
print "Enter the correct %s. There are %s vocab words to learn." % (ask_for, objective)

# initialize the score
score = 0
scale = 1
num_right = 0
# initialize funny business
funny_business = 1

# initialize the words that have been seen
seen = {}

# create a timer
"""def end():
    print "Game over"
    # raise SystemExit
t = Timer(5, end)
t.start()"""

# main
while(True):
	# if there are words
	if words:
		# get the next word
		word = random.choice(words.keys())
		right_answer = words.get(word)
		print "Next: %s" % word
		# get input
		user_answer = raw_input()
		# insert into seen, remove from words
		seen[word] = right_answer
		del words[word]
		# if they got it right
		if user_answer == right_answer:
			del seen[word]
			num_right += 1
			score += 1 * (scale ** 2)
			scale += 1
			print "~~Correct! Score: %s. Words left: %s~~" % (score, (objective-num_right))
		else:
			if user_answer == "non lo so":
				print "Ha. Clever. Here, have 10 points"
				score += 10
			scale = 1
			print "The correct answer is:"
			print right_answer
			correction = raw_input()
			correction = raw_input("One more time. per *%s* se dice " % word)
			while not(correction == right_answer):
				print "Keep trying!"
				correction = raw_input()
	# check if they won
	elif not(seen):
			print "You win! Final score: %s" % score
			raise SystemExit
	# cycle the missed ones through
	else:
		# score - 10?
		print "--------Starting over-------"
		score -= 25
		words = seen
		seen = {}
