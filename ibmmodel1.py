import collections

def _constant_factory(value):
    return lambda: value

def _train(corpus, loop_count=1000):
    f_keys = set()
    for (es, fs) in corpus:
        for f in fs:
            f_keys.add(f)
    t = collections.defaultdict(_constant_factory(1.0/len(f_keys)))

    for i in range(loop_count):
        count = collections.defaultdict(float)
        total = collections.defaultdict(float)
        s_total = collections.defaultdict(float)
        for (es, fs) in corpus:
            for e in es:
                s_total[e] = float()
                for f in fs:
                    s_total[e] += t[(e, f)]
            for e in es:
                for f in fs:
                    count[(e, f)] += t[(e, f)] / s_total[e]
                    total[f] += t[(e, f)] / s_total[e]
        for (e, f) in count.keys():
            t[(e, f)] = count[(e, f)] / total[f]
    return t

def train(sentences, loop_count=1000):
    corpus = [(es.split(), fs.split()) for (es, fs) in sentences]
    return _train(corpus, loop_count)

def tmap(t):
    mx = collections.defaultdict(float)
    mp = {}
    for (e,f), val in t.items():
        (mp[e], mx[e]) = (f, val) if val > mx[e] else (mp[e], mx[e])
    return mp

def translate(qs, mp):
    rs = [mp[q] if q in mp.keys() else q for q in qs]
    return rs

def test_train():
    sent_pairs = [("the house", "Haus das"),
                  ("the book", "das Buch"),
                  ("a book", "ein Buch"),]
    query = ["book","house"]
    t = train(sent_pairs, loop_count=50)
    mp = tmap(t)
    print mp
    print translate(query,mp)


if __name__ == '__main__':
    test_train()
