from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data.load_data import DataLoader


data = DataLoader().get_data()


monthly_category = data.groupby([pd.Grouper(freq='M'), 'Category'])['Amount'].sum().unstack().fillna(0)

# Create a stacked bar chart using Plotly
fig_stacked_bar_chart_all = go.Figure()

for category in monthly_category.columns:
    fig_stacked_bar_chart_all.add_trace(go.Bar(
        x=monthly_category.index.strftime('%Y-%m'),
        y=monthly_category[category],
        name=category
    ))

# Customize layout
fig_stacked_bar_chart_all.update_layout(
    barmode='stack',
    title='Total Spending per Month by Category',
    xaxis_title='Month',
    yaxis_title='Amount Spent',
    legend_title='Category',
    xaxis_tickangle=-45,
    template='plotly_white',
    margin=dict(t=50, b=50, l=50, r=150)
)


stacked_bar_chart_all = dcc.Graph(id='spending-per-month-by-category', figure=fig_stacked_bar_chart_all)

category_data = data.groupby('Category')['Amount'].sum().reset_index()

# Create pie chart
fig_pie_all = px.pie(
    category_data,
    names='Category',
    values='Amount',
    title='Spending per Category'
)

# Optional: update layout
fig_pie_all.update_traces(textinfo='percent+label')
fig_pie_all.update_layout(
    title_font_size=20,
    legend_title_text='Category',
    legend=dict(font=dict(size=12))
)
pie_all = dcc.Graph(id='proportion-per-category', figure=fig_pie_all)


# Sample aggregation: mean Amount per Category
mean_df = data.groupby('Category', as_index=False)['Amount'].mean()

# Create the bar chart
fig_bar_chart_all = go.Figure(
    data=go.Bar(
        x=mean_df['Category'],
        y=mean_df['Amount'],
        marker=dict(color='skyblue', line=dict(color='black', width=0.5)),
    )
)

# Update layout for aesthetics
fig_bar_chart_all.update_layout(
    title='Mean Amount per Category',
    xaxis_title='Category',
    yaxis_title='Mean Amount',
    xaxis_tickangle=75,
    plot_bgcolor='white',
    margin=dict(l=20, r=20, t=40, b=80),
)

# Add gridlines like matplotlib
fig_bar_chart_all.update_xaxes(showgrid=True, gridcolor='lightgrey', gridwidth=0.5)
fig_bar_chart_all.update_yaxes(showgrid=True, gridcolor='lightgrey', gridwidth=0.5)

# Show the figure

bar_chart_all = dcc.Graph(id='spending-per-category', figure=fig_bar_chart_all)


pie_year = dcc.Graph(id='proportion-per-category-per-year')
bar_chart_year= dcc.Graph(id='spending-per-category-per-year')

line_year = dcc.Graph(id='spending-per-year')




