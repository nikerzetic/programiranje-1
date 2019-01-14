from functools import lru_cache

"""
 Na nagradni igri ste zadeli kupon, ki vam omogoča, da v Mercatorju kupite
 poljubne izdelke, katerih skupna masa ne presega [max_w] kilogramov. Napišite
 funkcijo [best_value articles max_w], ki poišče največjo skupno ceno, ki jo
 lahko odnesemo iz trgovine, kjer lahko vsak izdelek vzamemo večkrat, nato pa
 še funkcijo [best_value_uniques articles max_w], kjer lahko vsak izdelek
 vzamemo kvečjemu enkrat.

 Namig: Modul [Array] ponuja funkcije kot so [map], [fold_left], [copy] in
 podobno, kot alternativa uporabi zank.
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 # best_value articles 1.;;
 - : float = 10.95
 # best_value_unique articles 1.;;
- : float = 7.66
"""
  

# (* Articles are of form (name, price, weight) *)
articles = [
	("yoghurt", 0.39, 0.18),
	("milk", 0.89, 1.03),
    ("coffee", 2.19, 0.2),
    ("butter", 1.49, 0.25),
    ("yeast", 0.22, 0.042),
    ("eggs", 2.39, 0.69),
    ("sausage", 3.76, 0.50),
    ("bread", 2.99, 1.0),
    ("Nutella", 4.99, 0.75),
    ("juice", 1.15, 2.0)
]

def best_value(articles, max_w):

    @lru_cache(maxsize=None) #memorizacija
    def best_val(w):
        options = []

        for item in articles:
            (name, price, weight) = item
            if w - weight >= 0:
                option = best_val(w - weight) + price
                options.append(option)
        
        if options:
            return max(options)
        else:
            return 0
    
    return best_val(max_w)

def best_value_uniques(articles, max_w):

    @lru_cache(maxsize=None) #memoizacija
    def best_val(w, taken):
        options = []

        for i, item in enumerate(articles):
            (name, price, weight) = item
            if w - weight >= 0 and taken[i] == '0':
                new_taken = taken[:i] + '1' + taken[i+1:]
                option = best_val(w - weight, new_taken) + price
                options.append(option)
        
        if options:
            return max(options)
        else:
            return 0
    
    return best_val(max_w, '0' * len(articles))

test1 = best_value(articles, 1.)
test2 = best_value_uniques(articles, 1.)