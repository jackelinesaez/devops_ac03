def verificapar(num):
    resto = num % 2
    if resto == 0:
        return 'É par'
    else:
        return 'Nao e par'

def test_par():
    assert verificapar(4) == 'É par'
    
def test_naopar():
    assert verificapar(5) == 'Nao e par'