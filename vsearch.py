
def search4vowels(phrase:str)->set:
    """Return any voweels' founf in 'phrase.'"""
    vowels= set('aieou')
    return  vowels.intersection(set(phrase))


def search4letters(phrase:str,letters:str='aeiou')->set:
    """Return set of the 'letters' founf in 'phrase.'"""
    return set(letters).intersection(set(phrase))
