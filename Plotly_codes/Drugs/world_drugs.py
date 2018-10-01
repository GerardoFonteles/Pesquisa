import plotly.plotly as py
import plotly
import pandas as pd

df = pd.read_csv('metadadosdrogasposicaogeografica2.csv', encoding = "ISO-8859-1", sep=';')
df.head()

df['text'] = df['sample_name'] + '' + df['location'] + ', ' + 'Lat: ' + df['Latitude'].astype(str) + ', ' + 'Long: ' + df['Longitude'].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [ dict(
        type = 'scattergeo',
        #locationmode = 'USA-states',
        lon = df['Longitude'],
        lat = df['Latitude'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            )
            # ,
            # colorscale = scl,
            # cmin = df['Nome'].min(),
            # color = df['Nome'],
            # cmax = df['Nome'].max(),
            # colorbar=dict(
                # title="Names"
            # )
        ))]

layout = dict(
        title = 'Drugs in the world',
        colorbar = True,
        geo = dict(
            #scope='usa',
            #projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

fig = dict( data=data, layout=layout )
plotly.offline.plot(fig, validate=False, filename='drugs_in_the_world.html')