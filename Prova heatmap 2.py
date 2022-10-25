from bioinfokit import analys
import holoviews as hv 
import hvplot.pandas # use hvplot directly with pandas
hv.extension('bokeh')  # to generate interactive plots 

# load example gene expression dataset as pandas dataframe
df = analys.get_data('hmap').data
df.head(2)
    Gene         A         B         C        D        E         F
0  B-CHI  4.505700  3.260360 -1.249400  8.89807  8.05955 -0.842803
1   CTL2  3.508560  1.660790 -1.856680 -2.57336 -1.37370  1.196000

# set gene names as index
df = df.set_index(df.columns[0])
df.head(2)
              A         B         C        D        E         F
Gene
B-CHI  4.505700  3.260360 -1.249400  8.89807  8.05955 -0.842803
CTL2   3.508560  1.660790 -1.856680 -2.57336 -1.37370  1.196000

hm=df.hvplot.heatmap(cmap='BrBG', xaxis='top', title='Gene expression heatmap', 
                     width=300, height=400)
hv.save(hm, 'heatmap.html')