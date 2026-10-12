# Brown-corpus

I built the count files from the Brown corpus and added <s> and </s> to every sentence. They use Norvig’s layout: one n-gram per line, a tab, then the count, sorted from highest to lowest count.

brown_count_1w.txt has 49,817 types, which includes the two markers.
brown_count_2w.txt has 434,952 bigram types.

The corpus has 57,340 sentences. There are 1.28 M tokens in total, including the markers.

I lower-cased all words and kept punctuation as separate tokens, as Brown tokenises it. Because of that, . is followed by </s> almost every time. 
