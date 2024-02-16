import graphviz

src = graphviz.Source(
    'digraph "graph" {rankdir=LR;\
     {rank=same; a[label="A"];b[label="B"];const1[label="1"];}\
     {rank=same; d[label="OR"];e[label="~AND"];const2[label="1"];}\
     {rank=same; g[label="AND"];h[label="C"];const3[label="1"];}\
     {rank=same; i[label="OR"];j[label="~AND"];const4[label="1"];}\
     k[label="AND"];\
     const1 -> d[label="-0.5"];const1 -> e[label="1.5"];const1 -> a[style="invis"];\
     a -> d[label="1"];a -> e[label="-1"];a -> b[style="invis"];\
     b -> d[label="1"];b -> e[label="-1"];\
     const2 -> g[label="-1.5"];const2 -> d[style="invis"];\
     d -> g[label="1"]; d -> e[style="invis"];\
     e -> g[label="1"];\
     const3 -> i[label="-0.5"];const3 -> j[label="1.5"]; const3 -> g[style="invis"];\
     g -> i[label="1"];g -> j[label="-1"];g -> h[style="invis"];\
     h -> i[label="1"];h -> j[label="-1"];\
     const4 -> k[label="-1.5"];const4 -> i[style="invis"];\
     i -> k[label="1"];i -> j[style="invis"];\
     j -> k[label="1"];\
     }'
)
src.render(filename='network2.gv', directory='saved_graphs/')
