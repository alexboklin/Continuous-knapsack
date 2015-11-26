Given n segments, provide a minimal set of points such that each segment contains at least one of these points. 


The first input line contains <i>l</i> &le; <i>n</i> &le; 10<sup>3</sup> items and 
capacity <i>o</i> &le; <i>W</i> &le; 10<sup>6</sup>.



Each successive input line (n lines total) contains two numbers  0 &le; <i>l</i> &le; <i>r</i> &le; 10<sup>9</sup> -- segment's endpoints.



Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака 0≤W≤2⋅106. 
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106 предмета (n, W, ci, wi — целые числа). 
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, 
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, 
с точностью не менее трёх знаков после запятой.
