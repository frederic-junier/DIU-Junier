
# coding: utf-8

# In[2]:


# %%
from functools import wraps, reduce, lru_cache
import time

###############################################################################
# TP : pratique de la programmation fonctionnelle en Python
#
# Cette feuille de TP a pour but de vous familiariser avec la programmation fonctionnelle.
# Il est composé des parties suivantes :
# 1. une mise en bouche avec des versions itératives de Fibonacci et la factorielle
# 2. une variation sur le thème de la fonction "forall" 
#qui teste si tous les éléments d'une liste satisfont un prédicat
#   * vous utiliserez à cette occasion les briques standard de la programmation fonctionnelle 
# disponible dans la bibliothèque standard de Python
# 3. un introduction aux décorateurs, des fonctions "qui modifient le comportement d'autres fonction"
# 4. la découverte des fonctionnalités spécifique des décorateurs en Python 
# qui doit vous amener à une application utile en classe avec les élèves
###############################################################################

# %%
###############################################################################
# INTRODUCTION : VERSION ITÉRATIVES ET RÉCURSIVES D'UN MÊME ALGORITHME
###############################################################################


# In[3]:


def gen_examples(f, n=10):
    """Pour générer les (n + 1) premiers termes f(0), f(1), ..., f(n)"""
    return [f(i) for i in range(0, n)]


# ## Exercice 1 : différentes implémentations de la suite de `fibonacci`

# In[4]:


# On donne la fonction fibo_rec (suite de Fibonacci) suivante


def fibo_rec(n):
    """Suite de Fibonacci, version récursive"""
    if n <= 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
    
    
def fibo_rec_acc(n, acc = [0, 1]):
    if n <= 1:
        return acc[n]
    return fibo_rec_acc(n - 1, [acc[1], acc[0] + acc[1]])

########################################
# EXERCICE : donner une version itérative de fibo_rec
########################################

def fibo_iter(n):
    """TODO Suite de Fibonacci, version itérative"""
    u, v = 0, 1
    for k in range(1, n + 1):
        u, v = v, u  + v
    return u


print("Les premiers termes de fibonacci")
print(f"fibo_rec  = {gen_examples(fibo_rec)}")
print(f"fibo_rec_acc  = {gen_examples(fibo_rec_acc)}")
print(f"fibo_iter = {gen_examples(fibo_iter)}")


# ## Exercice 2 : différentes implémentations de `factorielle`

# In[5]:


# On donne la fonction factorielle suivante :
def fact_iter(n):
    """Factorielle, version itérative"""
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

########################################
# EXERCICE :  donner une version recursive de fact_iter
########################################

def fact_rec(n):
    """TODO factorielle, version récursive"""
    return n * fact_rec(n - 1) if n > 1 else 1


print("Les premiers termes de la factorielle")
print(f"fact_iter = {gen_examples(fact_iter)}")
print(f"fact_rec  = {gen_examples(fact_rec)}")


# ## Exercice 3 : différentes implémentations de `all`

# In[6]:


###############################################################################
# PROGRAMMATION FONCTIONNELLE AVEC DES VARIANTES DE FORALL
###############################################################################

# On va définir la fonction suivante forall, de plusieurs façons différentes
# La fonction forall prend en paramètres
#   * une fonction pred (appellée prédicat)
#   * une liste l
# forall retourne True ssi tous les x dans l sont tels que pred(x)==True

ex1 = [4, 4, 2, 0, 1]
ex2 = []
ex3 = [4, 4, 2, 0, 8]
def pair(x): return x % 2 == 0

########################################
# EXERCICE :  définir forall (version boucle for)
########################################

def forall_for(pred, l):
    """TODO : une version de forall avec une boucle for """
    for x in l:
        if not pred(x):
            return False
    return True

print(f"forall_for(pair, ex1)={forall_for(pair, ex1)}")
print(f"forall_for(pair, ex2)={forall_for(pair, ex2)}")
print(f"forall_for(pair, ex3)={forall_for(pair, ex3)}")


# In[7]:


# Pour un style plus fonctionnel, on se dote des fonctions suivantes


def empty(l):
    """Retourne True ssi la liste est vide"""
    return len(l) == 0


def head(l):
    """Retourne la tête de la liste, son 1er élément, et None si la liste est vide"""
    if empty(l):
        return None
    return l[0]


def tail(l):
    """Retourne la liste privée de son 1er élément, et None si la liste est vide"""
    if empty(l):
        return None
    return l[1:]

########################################
# EXERCICE :  définir forall (version récursive avec les listes)
########################################

def forall_funct(pred, l):
    """TODO : une version résursive de forall, plus fonctionnelle,
    utilisant UNIQUEMENT empty, head et tail sans boucle for ni affectation.
    La fonction sera récursive"""
    if empty(l):
        return True
    return pred(head(l)) and forall_funct(pred, tail(l))


print(f"forall_funct(pair, ex1)={forall_funct(pair, ex1)}")
print(f"forall_funct(pair, ex2)={forall_funct(pair, ex2)}")
print(f"forall_funct(pair, ex3)={forall_funct(pair, ex3)}")


# In[8]:


########################################
# EXERCICE :  définir forall (version avec map)
########################################

def forall_map_all(pred, l):
    """TODO : une version de forall utilisant les fonctions map 
    et all de la bibliothèque standard
    voir https://docs.python.org/3/library/functions.html"""
    return all(map(pred, l))


print(f"forall_map_all(pair, ex1)={forall_map_all(pair, ex1)}")
print(f"forall_map_all(pair, ex2)={forall_map_all(pair, ex2)}")
print(f"forall_map_all(pair, ex3)={forall_map_all(pair, ex3)}")


# In[9]:


########################################
# EXERCICE :  définir forall (version avec filter)
########################################

def forall_filter(pred, l):
    """TODO : une version de forall utilisant les fonctions standards filter et len. 
    On pourra avoir besoin de transformer le résultat interméidiaire avec list()"""
    return len(list(filter(pred, l))) == len(l)


print(f"forall_filter(pair, ex1)={forall_filter(pair, ex1)}")
print(f"forall_filter(pair, ex2)={forall_filter(pair, ex2)}")
print(f"forall_filter(pair, ex3)={forall_filter(pair, ex3)}")


# In[10]:


list(filter(pair, ex1))


# In[11]:


# La fonction standard reduce du module functools (appellée aussi fold) prend trois paramètre
#    * une fonction f  de type A * B -> A
#    * une liste l de type [A]
#    * une valeur initialize de type A
# Pour l = [x1, x2, ..., xn], reduce(f, l, x0) calcule
# f(...(f(f(x0, x1), x2)...), xn)
# Par exemple, reduce(lambda acc, x : acc * x, range(1,6), 1) calcule
# ((((((1*1)*2)*3)*4)*5)*6) = 6! = 120

# https://docs.python.org/3/library/functools.html#functools.reduce


########################################
# EXERCICE :  définir forall (version avec reduce)
########################################

def forall_reduce(pred, l):
    """TODO : une version de forall utilisant UNIQUEMENT la fonction standard functools.reduce
    """
    return reduce(lambda a, b : a and pred(b), l, True)


print(f"forall_reduce(pair, ex1)={forall_reduce(pair, ex1)}")
print(f"forall_reduce(pair, ex2)={forall_reduce(pair, ex2)}")
print(f"forall_reduce(pair, ex3)={forall_reduce(pair, ex3)}")


# ## Décorateurs en Python

# * Voir l'article [https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6](https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6)
# 
# * Voir aussi Python Fluent

# In[12]:


###############################################################################
# LES DÉCORATEURS EN PYTHON
###############################################################################

# Un décorateur est une fonction qui modifie le comportement d'une autre fonction.
# Plus précisément, c'est une fonction d qui prend une fonction f (unaire) en argument, telle que d(f) est la fonction f dont le comportement est modifié. La fonction d est donc une fonction d'ordre supérieur qui prend une fonction en argument et en renvoie une.

# Un exemple, le décorateur qui loggue le temps d'exécution. On ne gère que le cas où f est unaire


def timer(f):
    """Calcule et affiche la durée d'exécution d'une fonction unaire"""
    def wrapped(x):
        start = time.time()
        value = f(x)
        end = time.time()
        print(f"Durée {end - start}  secs")
        return value
    return wrapped


# On peut se servir pour chronométrer une des fonctions précédent, par exemple fibo_rec(32) qui prend un temps sensible (~1sec sur ma machine)
print(timer(fibo_rec)(32))


# ## Exercice 4 : décorateurs `maybe`

# In[13]:


# %%
########################################
# EXERCICE : définir le décorateur maybe
########################################

def maybe(f, v):
    """Appelle f et si f renvoie None, 
    alors renvoie v à la place. 
    Autrement dit, maybe(f, v) fait la même chose que f sauf pour les cas où f est indéfinie"""
    def wrapped(*args, **kwargs):
        value = f(*args, **kwargs)
        if value is None:
            return v
        return value
    return wrapped


def positive_or_none(n):
    if n < 0:
        return None
    return n


positive_or_zero = maybe(positive_or_none, 0)

print(f"positive_or_none(42)={positive_or_none(42)}")
print(f"positive_or_none(-1)={positive_or_none(-1)}")

print(f"positive_or_zero(42)={positive_or_zero(42)}")
print(f"positive_or_zero(-1)={positive_or_zero(-1)}")


# Remarque sur les fonctions `lambda` :
# 
# * si la fonction est pure, on peut la remplacer par une fonction `lambda`
# * si la fonction comporte une boucle c'est plus compliqué (ou on ne peut pas)
# 
# Le `lambda calcul` est équivalent à la machine de Turing, il est apparu dans les années 30 puis il est tombé dans l'oubli et il revenu à la mode dans les années 60.

# In[14]:


# Même question que précédemment, mais écrire maybe UNIQUEMENT avec des lambdas et
# un expression conditionnelle (dit aussi if ternaire)
# https://docs.python.org/3/reference/expressions.html#conditional-expressions

########################################
# EXERCICE : définir le décorateur maybe avec des lambda fonctions uniquement
########################################


maybe_lambda = lambda f,v : lambda x : v  if f(x) is None else f(x)


positive_or_zero_lambda = maybe_lambda(positive_or_none, 0)

print(f"positive_or_zero_lambda(42)={positive_or_zero_lambda(42)}")
print(f"positive_or_zero_lambda(-1)={positive_or_zero_lambda(-1)}")


# In[15]:


########################################
# EXERCICE (POUR ALLER PLUS LOIN)
########################################

# même chose que précédement un décorateur uniquement avec des lambdas 
#mais en faisant attention à n'appeler f QU'UNE SEULE FOIS


#On peut essayer de le faire sans fonction lambda puis avec des fonction lambda
#C'est intéressant si la fonction f a un effet de bord (par exemple avec un print)


def maybe_lambda0(f, v):
    def f2(x):
        def f3(v):
            return v if value is None else value
        return f3(f(x))
    return f2

#Tout en lambda

maybe_lambda_better = lambda f,v : lambda x : (lambda value : v if value is None else value)(f(x))      

positive_or_zero_lambda_better0 = maybe_lambda0(positive_or_none, 0)

positive_or_zero_lambda_better = maybe_lambda(positive_or_none, 0)

print(
    f"positive_or_zero_lambda_better(42)={positive_or_zero_lambda_better(42)}")
print(
    f"positive_or_zero_lambda_better(-1)={positive_or_zero_lambda_better(-1)}")

print(
    f"positive_or_zero_lambda_better0(42)={positive_or_zero_lambda_better(42)}")
print(
    f"positive_or_zero_lambda_better0(-1)={positive_or_zero_lambda_better(-1)}")
# ATTENDU
# ATTENDU
# positive_or_zero_lambda_better(42)=42
# positive_or_zero_lambda_better(-1)=0


# In[16]:


########################################
# EXERCICE (POUR ALLER PLUS LOIN)
########################################

# même chose que précédement un décorateur uniquement avec des lambdas 
#mais en faisant attention à n'appeler f QU'UNE SEULE FOIS

maybe_lambda = lambda f,v : lambda x : (lambda y=f(x) :  v if y is None else y)()  

positive_or_zero_lambda_better = maybe_lambda(positive_or_none, 0)

print(
    f"positive_or_zero_lambda_better(42)={positive_or_zero_lambda_better(42)}")
print(
    f"positive_or_zero_lambda_better(-1)={positive_or_zero_lambda_better(-1)}")
# ATTENDU
# positive_or_zero_lambda_better(42)=42
# positive_or_zero_lambda_better(-1)=0


# In[17]:


########################################
# EXERCICE (POUR ALLER PLUS LOIN) : maybe n-aire
########################################

# même question qu'au début, mais dans le cas général où f est une fonction n-aire
# utiliser pour cela https://book.pythontips.com/en/latest/args_and_kwargs.html


def maybe_nary(f, v):
    """Appelle f et si f renvoie None, alors renvoie v à la place. 
    Autrement dit, maybe(f, v) fait la même chose que f sauf pour les cas où f est indéfinie"""
    def wrapped(*args, **kwargs):
        value = f(*args, **kwargs)
        if value is None:
            return v
        return value
    return wrapped


def any_positive_or_none(*args):
    """Return None if any argument is negative and the list of its argument otherwise"""
    for arg in args:
        if arg < 0:
            return None
    return list(args)


any_positive_or_zero = maybe_nary(any_positive_or_none, [])

# renvoie [42]
print(f"any_positive_or_zero(42)={any_positive_or_zero(42)}")
# renvoie []
print(f"any_positive_or_zero(-1)={any_positive_or_zero(-1)}")
# renvoie []
print(f"any_positive_or_zero(1,2,3,-1)={any_positive_or_zero(1,2,3,-1)}")
# renvoie [1, 2, 3]
print(f"any_positive_or_zero(1,2,3)={any_positive_or_zero(1,2,3)}")


# ## Exercice 5 : décorateur `memoize`

# In[18]:


# %%
########################################
# EXERCICE : définir le décorateur memoize
########################################


def memoize(f):
    """memoize permet de mémoriser les appels de f : 
    si memoize(f) a déjà été appelée avec le même argument,
    alors memoize(f) renvoie directement (sans rappeler relancer le calcul de f) 
    la valeur retournée précédemment par f pour cet argument. 
    On supposera f unaire et on utilisera un dictionnaire pour mémoriser les valeurs calculées"""
    memo = dict()
    def wraped(x):
        if x in memo:
            return memo[x]
        value = memo[x] = f(x)
        return value
    return wraped


def memoize2(f):
    """memoize permet de mémoriser les appels de f : 
    si memoize(f) a déjà été appelée avec le même argument,
    alors memoize(f) renvoie directement (sans rappeler relancer le calcul de f) 
    la valeur retournée précédemment par f pour cet argument. 
    On supposera f unaire et on utilisera un dictionnaire pour mémoriser les valeurs calculées"""
    memo = dict()
    def wraped(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return wraped


def fonction_de_test(n):
    print(f"    fonction_de_test appellée avec {n}")
    return n*n


fonction_de_test_memo = memoize(fonction_de_test)
print(f"fonction_de_test_memo(42)={fonction_de_test_memo(42)}")
print(f"fonction_de_test_memo(0)={fonction_de_test_memo(0)}")
print(f"fonction_de_test_memo(42)={fonction_de_test_memo(42)}")
print(f"fonction_de_test_memo(0)={fonction_de_test_memo(0)}")
# ATTENDU : On ne doit voir que 2 fois le print dans la fonction de test (et pas 4 sans memoize)
#     fonction_de_test appellée avec 42
# fonction_de_test_memo(42)=1764
#     fonction_de_test appellée avec 0
# fonction_de_test_memo(0)=0
# fonction_de_test_memo(42)=1764
# fonction_de_test_memo(0)=0


# In[19]:


########################################
# EXERCICE  (POUR ALLER PLUS LOIN) : 
#définir le décorateur memoize qui gère le cas des fonction n-aires
#(sans arguments de type keywords, autrement dit, on gère juste *args, pas **kwargs)
########################################


def memoize_nary(f):
    """Pour cette version, on devra convertir une "liste" de plusieurs paramètres (*args) en
       une structure qui soit hashable pour pouvoir servir de clef dans le dictionnaire
       Les listes ne le sont pas, mais les tuples le sont en revanche."""
    memo = dict()
    def wraped(*args):
        if args in memo:
            return memo[args]
        value = memo[args] = f(*args)
        return value
    return wraped


def fonction_de_test_nary(*args):
    print(f"    fonction_de_test appellée avec {list(args)}")
    return [x*x for x in args]


fonction_de_test_nary_memo = memoize_nary(fonction_de_test_nary)

print(f"fonction_de_test_nary_memo(1,2,3)={fonction_de_test_nary_memo(1,2,3)}")
print(f"fonction_de_test_nary_memo(0,1,2)={fonction_de_test_nary_memo(0,1,2)}")
print(f"fonction_de_test_nary_memo(1,2,3)={fonction_de_test_nary_memo(1,2,3)}")
print(f"fonction_de_test_nary_memo(0,1,2)={fonction_de_test_nary_memo(0,1,2)}")
# ATTENDU : on ne doit voir que 2 fois le print dans la fonction de test (et pas 4 sans memoize
#     fonction_de_test appellée avec [1, 2, 3]
# fonction_de_test_nary_memo(1,2,3)=[1, 4, 9]
#     fonction_de_test appellée avec [0, 1, 2]
# fonction_de_test_nary_memo(0,1,2)=[0, 1, 4]
# fonction_de_test_nary_memo(1,2,3)=[1, 4, 9]
# fonction_de_test_nary_memo(0,1,2)=[0, 1, 4]


# # LES DÉCORATEURS PYTHON DANS LA BIBLIOTHÈQUE STANDARD : UNE APPLICATION POUR LA CLASSE
# 
# * À ce sujet voir [https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6](https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6)
# * Décorateurs de la bibliothèque standard : [https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html)   ou   Python Fluent page 226  : deux sont utilisés ci-dessous `@wraps` pour enregistrer la signature de la fonction enveloppée dans la fonction enveloppante  et `@lru_cache` pour mémoizer
# 

# In[20]:



# /!\ Cet exercice vous amène à écrire un décorateur qui peut être très utile en classe pour illustrer la récursivité. Il est issu de discussions avec des étudiants en CAPES NSI qui souhaitaient, dans le cadre de la prépration du projet à présenter pour l'oral 2 du concours, fournir une petite bibliothèque pour aider les élèves à aborder cette notion. Je pense que le décorateur suivant pourrait en faire partie. /!\

# Python propose une syntaxe ad hoc @decorator pour la manipulation des décorateurs. 
#De plus, la bibliothèque standard propose quelques outils 
#pour en faciliter la manipulation ainsi que quelques décorateurs très utiles. Voir :
#
# https://docs.python.org/3/glossary.html#term-decorator
# https://docs.python.org/3/reference/compound_stmts.html#function
# https://book.pythontips.com/en/latest/decorators.html
# https://docs.python.org/3/library/functools.html


# Par exemple, avec le décorateur suivant, on peut tracer les appel à la fonction récursive qui calcule le nieme terme de la suite de Fibonaccu


def tracer(func):
    """Un décorateur qui trace les exécutions"""
    # pour ne pas changer __name__ en 'wrapped' après wrapping, voir functools
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(f'Calling {wrapped.__name__}({args}, {kwargs})')
        return func(*args, **kwargs)
    return wrapped


@tracer
def fibo_tracee(n):
    """Suite de Fibonacci, version récursive avec les appels tracés"""
    if n <= 1:
        return n
    else:
        return fibo_tracee(n-1) + fibo_tracee(n-2)


print(f"fibo_tracee(5)={fibo_tracee(5)}")
# ATTENDU
# Calling fibo_tracee((5,), {})
# Calling fibo_tracee((4,), {})
# Calling fibo_tracee((3,), {})
# Calling fibo_tracee((2,), {})
# Calling fibo_tracee((1,), {})
# Calling fibo_tracee((0,), {})
# Calling fibo_tracee((1,), {})
# Calling fibo_tracee((2,), {})
# Calling fibo_tracee((1,), {})
# Calling fibo_tracee((0,), {})
# Calling fibo_tracee((3,), {})
# Calling fibo_tracee((2,), {})
# Calling fibo_tracee((1,), {})
# Calling fibo_tracee((0,), {})
# Calling fibo_tracee((1,), {})
# fibo_tracee(5)=5


# On remarque immédiatement 2 choses :
# * cette implémentation est sous optimale car elle produit un nombre exponentiel d'appel récursifs
# * la profondeur des appels récursifs n'est pas visible, elle devrait l'être avec une indentation


# ## Exercice : écrire le décorateur @visualise

# In[21]:


########################################
# EXERCICE : écrire le décorateur @visualise
########################################


def visualise(func):
    """Décorateur qui trace les appels comme @tracer mais en indentant à chaque appel récursif"""
    visualise.level = 0
    visualise.preced = float('inf')
    # pour ne pas changer __name__ en 'wrapped' après wrapping, voir functools
    @wraps(func)
    def wrapped(*args, **kwargs):
        if args[0] <= visualise.preced:            
            visualise.level += 1            
        else:
            visualise.level -= abs(args[0] - visualise.preced)
        visualise.preced = args[0]
        print(f'{visualise.level * "  "} Calling {func.__name__}({args}, {kwargs})')       
        return func(*args, **kwargs)        
    return wrapped


@visualise
def fibo_indent(n):
    """Suite de Fibonacci, version récursive avec les appels tracés ET indentés"""
    if n <= 1:
        return n
    else:
        return fibo_indent(n-1) + fibo_indent(n-2)


print(f"fibo_indent(5)={fibo_indent(5)}")

# on doit obtenir quelque chose de semblable à la trace suivante
# fibo_indent((5,), {})
#     fibo_indent((4,), {})
#         fibo_indent((3,), {})
#             fibo_indent((2,), {})
#                 fibo_indent((1,), {})
#                 fibo_indent((0,), {})
#             fibo_indent((1,), {})
#         fibo_indent((2,), {})
#             fibo_indent((1,), {})
#             fibo_indent((0,), {})
#     fibo_indent((3,), {})
#         fibo_indent((2,), {})
#             fibo_indent((1,), {})
#             fibo_indent((0,), {})
#         fibo_indent((1,), {})
# fibo_indent(5)=5


# In[22]:


@memoize
@visualise
def fibo_viz_memo(n):
    """Suite de Fibonacci, version récursive avec les appels tracés, indentés et memoization"""
    if n <= 1:
        return n
    else:
        return fibo_viz_memo(n-1) + fibo_viz_memo(n-2)


print(f"fibo_viz_memo(5)={fibo_viz_memo(5)}")


# In[23]:


@lru_cache(maxsize=32)
@visualise
def fibo_viz_memo(n):
    """Suite de Fibonacci, version récursive avec les appels tracés, indentés et memoization"""
    if n <= 1:
        return n
    else:
        return fibo_viz_memo(n-1) + fibo_viz_memo(n-2)


print(f"fibo_viz_memo(32)={fibo_viz_memo(32)} , {fibo_viz_memo.cache_info()} ")


# In[24]:


@lru_cache(maxsize=2)
@visualise
def fibo_viz_memo(n):
    """Suite de Fibonacci, version récursive avec les appels tracés, indentés et memoization"""
    if n <= 1:
        return n
    else:
        return fibo_viz_memo(n-1) + fibo_viz_memo(n-2)


print(f"fibo_viz_memo(8)={fibo_viz_memo(8)} , {fibo_viz_memo.cache_info()} ")


# In[25]:


# Une autre version de visualise

def visualise(func):
    """Décorateur qui trace les appels comme @tracer mais en indentant à chaque appel récursif"""
    visualise.level = 0
    visualise.preced = float('inf')
    # pour ne pas changer __name__ en 'wrapped' après wrapping, voir functools
    @wraps(func)
    def wrapped(*args, **kwargs):       
        print(f'{visualise.level * "  "} Calling {func.__name__}({args}, {kwargs})')     
        visualise.level += 1
        res = func(*args, **kwargs)  
        visualise.level -= 1
        return res
    return wrapped


@visualise
def fibo_indent(n):
    """Suite de Fibonacci, version récursive avec les appels tracés ET indentés"""
    if n <= 1:
        return n
    else:
        return fibo_indent(n-1) + fibo_indent(n-2)


print(f"fibo_indent(5)={fibo_indent(5)}")

# on doit obtenir quelque chose de semblable à la trace suivante
# fibo_indent((5,), {})
#     fibo_indent((4,), {})
#         fibo_indent((3,), {})
#             fibo_indent((2,), {})
#                 fibo_indent((1,), {})
#                 fibo_indent((0,), {})
#             fibo_indent((1,), {})
#         fibo_indent((2,), {})
#             fibo_indent((1,), {})
#             fibo_indent((0,), {})
#     fibo_indent((3,), {})
#         fibo_indent((2,), {})
#             fibo_indent((1,), {})
#             fibo_indent((0,), {})
#         fibo_indent((1,), {})
# fibo_indent(5)=5


# In[26]:


# Encore une autre version de viusalise
########################################
# EXERCICE : écrire le décorateur @visualise
########################################

def visualise2(func):
    """Décorateur qui trace les appels comme @tracer mais en indentant à chaque appel récursif"""
    visualise2.visualise_level = 1
    # pour ne pas changer __name__ en 'wrapped' après wrapping, voir functools
    @wraps(func)
    def wrapped(*args, **kwargs):        
        print(f'{(visualise2.visualise_level - 1) * "  |"}  ┌ Appel de {func.__name__}({args}, {kwargs})')  
        visualise2.visualise_level += 1
        result = func(*args, **kwargs)
        visualise2.visualise_level -= 1
        print(f'{(visualise2.visualise_level - 1) * "  |"}  └ Résultat de {func.__name__}({args}, {kwargs}), {result}')
        return result        
    return wrapped

#les deux suivantes implémentent un compteur local


def visualise(func):
    """Décorateur qui trace les appels comme @tracer mais en indentant à chaque appel récursif"""
    #avec un attribut de fonction englobante mais le compteur est partagé par toutes les fonctions décorées
    #compteur global, on compte tous les appels à visualise
    visualise_level = 1
    # pour ne pas changer __name__ en 'wrapped' après wrapping, voir functools
    @wraps(func)
    def wrapped(*args, **kwargs):
        nonlocal visualise_level        
        print(f'{(visualise_level - 1) * "  |"}  ┌ Appel de {func.__name__}({args}, {kwargs})')  
        visualise_level += 1
        result = func(*args, **kwargs)
        visualise_level -= 1
        print(f'{(visualise_level - 1) * "  |"}  └ Résultat de {func.__name__}({args}, {kwargs}), {result}')
        return result        
    return wrapped


def visualise3(func):
    """Décorateur qui trace les appels comme @tracer mais en indentant à chaque appel récursif"""
    # pour ne pas changer __name__ en 'wrapped' après wrapping, voir functools
    @wraps(func)
    def wrapped(*args, **kwargs):        
        print(f'{(wrapped.visualise_level - 1) * "  |"}  ┌ Appel de {func.__name__}({args}, {kwargs})')  
        wrapped.visualise_level += 1
        result = func(*args, **kwargs)
        wrapped.visualise_level -= 1
        print(f'{(wrapped.visualise_level - 1) * "  |"}  └ Résultat de {func.__name__}({args}, {kwargs}), {result}')
        return result   
    wrapped.visualise_level = 1
    return wrapped





@visualise2
def fibo_indent(n):
    """Suite de Fibonacci, version récursive avec les appels tracés ET indentés"""
    if n <= 1:
        return n
    else:
        return fibo_indent(n-1) + fibo_indent(n-2)


print(f"fibo_indent(8)={fibo_indent(8)}")

# on doit obtenir quelque chose de semblable à la trace suivante
# fibo_indent((5,), {})
#     fibo_indent((4,), {})
#         fibo_indent((3,), {})
#             fibo_indent((2,), {})
#                 fibo_indent((1,), {})
#                 fibo_indent((0,), {})
#             fibo_indent((1,), {})
#         fibo_indent((2,), {})
#             fibo_indent((1,), {})
#             fibo_indent((0,), {})
#     fibo_indent((3,), {})
#         fibo_indent((2,), {})
#             fibo_indent((1,), {})
#             fibo_indent((0,), {})
#         fibo_indent((1,), {})
# fibo_indent(5)=5


# In[27]:


@memoize
@visualise
def fibo_viz_memo(n):
    """Suite de Fibonacci, version récursive avec les appels tracés, indentés et memoization"""
    if n <= 1:
        return n
    else:
        return fibo_viz_memo(n-1) + fibo_viz_memo(n-2)


print(f"fibo_viz_memo(8)={fibo_viz_memo(8)}")

