"""Build unigram and bigram counts from the Brown corpus with <s> and </s>.

Output format matches Norvig's count_1w.txt / count_2w.txt:
one n-gram per line, tab-separated, sorted by descending count.
Tokens are lower-cased; punctuation tokens are kept, as in J&M's BeRP tables.
"""
from collections import Counter
from nltk.corpus import brown

uni, bi = Counter(), Counter()
n_sents = 0
for sent in brown.sents():
    toks = ['<s>'] + [w.lower() for w in sent] + ['</s>']
    uni.update(toks)
    bi.update(zip(toks, toks[1:]))
    n_sents += 1


def write(path, counter, fmt):
    with open(path, 'w', encoding='utf-8') as f:
        for k, c in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
            f.write(f'{fmt(k)}\t{c}\n')


write('brown_count_1w.txt', uni, lambda w: w)
write('brown_count_2w.txt', bi, lambda b: f'{b[0]} {b[1]}')

# Sanity checks
assert uni['<s>'] == uni['</s>'] == n_sents
assert sum(c for (a, _), c in bi.items() if a == '<s>') == n_sents
print(f'sentences      {n_sents:,}')
print(f'tokens (N)     {sum(uni.values()):,}  (incl. markers)')
print(f'types (V)      {len(uni):,}  (incl. markers)')
print(f'bigram types   {len(bi):,}')
print(f"P(i | <s>)     {bi[('<s>', 'i')] / uni['<s>']:.4f}")
print(f"P(the | <s>)   {bi[('<s>', 'the')] / uni['<s>']:.4f}")
print(f"P(</s> | .)    {bi[('.', '</s>')] / uni['.']:.4f}")
