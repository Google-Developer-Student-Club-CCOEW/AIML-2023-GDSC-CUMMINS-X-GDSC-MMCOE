# defining context free grammar rules

# terminals are the words used in the sentence
# "|" represents "or"
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# non-terminals are the words used to define the grammer rules
NONTERMINALS = """
S -> NP VP | VP NP | S Conj S
PP -> P NP
AP -> Adj | Adj AP
NP -> N | Det N | NP PP | Det AP N
VP -> V | Adv V | V Adv | V NP | V PP | Adv VP | VP Adv
"""