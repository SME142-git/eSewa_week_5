from dash import Output, Input
from data.load_data import DataLoader
import plotly.express as px
import plotly.graph_objects as go

data = DataLoader().get_data()

def register_graph_callbacks(app):
    @app.callback(
        Output('proportion-per-category-per-year', 'figure'),
        Input('year-slider', 'value')
    )
    def show_pie_year(year):
        category_data = data[data.Year == year].groupby('Category')['Amount'].sum().reset_index()

        # Create pie chart
        fig = px.pie(
            category_data,
            names='Category',
            values='Amount',
            title=f'Spending per Category in {year}'
        )

        # Optional: update layout
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(
            title_font_size=20,
            legend_title_text='Category',
            legend=dict(font=dict(size=12))
        )
        return fig

    @app.callback(
        Output('spending-per-category-per-year', 'figure'),
        Input('year-slider', 'value')
    )
    def show_bar_chart_year(year):
        # Sample aggregation: mean Amount per Category
        mean_df = data[data.Year == year].groupby('Category', as_index=False)['Amount'].sum()

        # Create the bar chart
        fig = go.Figure(
            data=go.Bar(
                x=mean_df['Category'],
                y=mean_df['Amount'],
                marker=dict(color='pink', line=dict(color='black', width=0.5)),
            )
        )

        # Update layout for aesthetics
        fig.update_layout(
            title=f'Spending per Category in {year}',
            xaxis_title='Category',
            yaxis_title='Mean Amount',
            xaxis_tickangle=75,
            plot_bgcolor='white',
            margin=dict(l=20, r=20, t=40, b=80),
        )

        # Add gridlines like matplotlib
        fig.update_xaxes(showgrid=True, gridcolor='lightgrey', gridwidth=0.5)
        fig.update_yaxes(showgrid=True, gridcolor='lightgrey', gridwidth=0.5)

        # Show the figure
        return fig

    @app.callback(
        Output('spending-per-year', 'figure'),
        Input('year-slider', 'value')
    )
    def show_line_year(year):

        # Resample: Weekly sum of 'Amount'
        df_weekly = data[data.Year==year].resample('W')['Amount'].sum().fillna(0).reset_index()

        # Plotly line plot
        fig = px.line(df_weekly, x='Date', y='Amount', labels={'index': 'Week', 'Amount': 'Amount'})
        fig.update_layout(title='Weekly Amount Sum', yaxis_title='Amount', xaxis_title='Date')

        return fig


