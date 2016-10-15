def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    a = dict()
    split_s = s.split()
    for sp in split_s:
        a[sp] = a.get(sp,0) + 1
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    tup = [(v[0],v[1]) for v in sorted(a.iteritems(), key=lambda(k, v): (-v, k))]
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    #top_n = tup[:n]
    return tup


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
