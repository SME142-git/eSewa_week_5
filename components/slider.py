from dash import dcc
from data.load_data import DataLoader

data = DataLoader().get_data()

start_year = data.Year.min()
end_year = data.Year.max()


year_slider = dcc.Slider(
        id='year-slider',
        min=start_year,
        max=end_year,
        step=1,
        value=start_year,
        marks={year: str(year) for year in range(start_year, end_year + 1, 1)},
    )