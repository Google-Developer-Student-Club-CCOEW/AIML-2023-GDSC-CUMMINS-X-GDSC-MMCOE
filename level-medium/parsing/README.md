# Expected Output Parser
<pre>
Sentence: Holmes sat and lit his pipe
                S
         _______|________
        S       |        S
   _____|___    |     ___|___
  NP        VP  |    VP      NP
  |         |   |    |    ___|___
  N         V  Conj  V  Det      N
  |         |   |    |   |       |
holmes     sat and  lit his     pipe

Noun Phrase Chunks
holmes
his pipe

Sentence: I had a little moist red paint in the palm of my hand
              S
  ____________|____________________
 |                                 VP
 |    _____________________________|____
 |   |                                  NP
 |   |                __________________|___________
 |   |               NP                             PP
 |   |    ___________|_____________      ___________|____
 |   |   |           AP            |    |                NP
 |   |   |     ______|____         |    |        ________|___
 |   |   |    |           AP       |    |       |            PP
 |   |   |    |       ____|___     |    |       |         ___|___
 NP  |   |    |      |        AP   |    |       NP       |       NP
 |   |   |    |      |        |    |    |    ___|___     |    ___|___
 N   V  Det  Adj    Adj      Adj   N    P  Det      N    P  Det      N
 |   |   |    |      |        |    |    |   |       |    |   |       |
 i  had  a  little moist     red paint  in the     palm  of  my     hand

Noun Phrase Chunks
i
a little moist red paint
the palm
my hand
<pre/>
