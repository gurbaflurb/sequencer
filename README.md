# Sequencer
To answer this question when posed to my brain which likes to see practical examples side by side theory.

## Source
Taken from this twitter post: https://twitter.com/littmath/status/1769044719034647001

In case it's deleted see the below question:
Flip a fair coin 100 times—it gives a sequence of heads (H) and tails (T). For each HH in the sequence of flips, Alice gets a point; for each HT, Bob does, so e.g. for the sequence THHHT Alice gets 2 points and Bob gets 1 point. Who is most likely to win?

## According to Twitter:
Poll results are (as of 1735 UTC 17 MARCH 2024):
- Alice wins - 26.3% of people voted
- Bob wins - 10.2% of people voted
- Equally Likely - 42.8% of people voted
- See results - 20.7% of people voted

## According to Reddit:
https://www.reddit.com/r/theydidthemath/comments/1bgnbnt/comment/kv8x4lu/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
- Tl;dr Bob will end with more points than Alice on average. 

## Conclusion
Running many tests, it would appear that Bob, generally, over many, many, many rounds, wins slightly more than Alice.

Seeds used:
- 35tm9fSLfSjrKBAxA80hYw==
- U8N/tZPzaIDc5GndaxwhQQ==
- 45mcfKVQN7enjVjU46MCqg==
- yZ1nrZNY8hFP0J6+JJ0+eg==

Rounds used: 10000

In general, if you run a long enough sequence, Bob will eventually win by a hair. Smaller sequences, appear to be more 50/50. Even at 1000 rounds of 1000 coin flips each, the results still appeared to be 50/50. It wasn't until after the 10,000 rounds  
