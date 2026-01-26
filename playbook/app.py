import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng
st.set_page_config(layout="wide")

df = pd.read_csv('./playbook/actions.csv')

def filter_multiple(value_lst,filter_lst):
    return bool(set(value_lst) & set(filter_lst))

with st.sidebar:
    trait_options = ["Reliability", "Safe", "Value-Driven", "Transparent", "Secure"]
    trait_selection = st.pills("Directions", trait_options, selection_mode="multi")
    
    focus_area_options = ["Culture", "Governance", "Platform", "Security", "Observability"]
    focus_area_selection = st.pills("Focus Areas", focus_area_options, selection_mode="multi")
    
if trait_selection and not focus_area_selection:
    filtered_df = df[df['Trait'].apply(lambda x: filter_multiple(x.split(","), trait_selection))]

if focus_area_selection and not trait_selection:
    filtered_df = df[df['Focus Area'].isin(focus_area_selection)] 

if trait_selection and focus_area_selection:
    filtered_df = df[df['Trait'].apply(lambda x: filter_multiple(x.split(","), trait_selection)) & df['Focus Area'].isin(focus_area_selection)]

if not trait_selection and not focus_area_selection:
    filtered_df = df

sub_category_options = ["Active Awareness","Purpose","Roles & Responsibility",
                        "AI Risk Management","Artefact Inventory","Change Management",
                        "Standards and Policies ","Define and Instrument ","Evaluate and Measure ",
                        "Monitor and Action","Automation","Integration and Collaboration ",
                        "Resilience","Access Control","Data Classification and Controls","Guardrails"]

st.write(f"Total Records: {filtered_df.shape[0]}")

st.dataframe(filtered_df, 
             column_config=
                   {
                        "Trait": st.column_config.MultiselectColumn(
                            "Trait",
                            options=trait_options,
                            color=["#0a53a8", "#ffe5a0", "#11734b", "#5a3286", "#b10202"],
                            format_func=lambda x: x.capitalize(),
                            width=100, 
                        ),
                        "Focus Area": st.column_config.MultiselectColumn(
                            "Focus Area",
                            options=focus_area_options,
                            color=["#e6e6e6", "#ffcfc9", "#bfe1f6", "#b10202", "#d4edbc"],
                            format_func=lambda x: x.capitalize(),
                            width=100, 
                        ),
                        "Sub Category": st.column_config.MultiselectColumn(
                            "Sub Category",
                            options=sub_category_options,
                            color=("blue," * len(sub_category_options)).split(','),
                            format_func=lambda x: x.capitalize(),
                            width=100, 
                        ),
                         "Section Header": None,
                         "RMF Pillar": None,
                         "RMF Pillar Description": None,
                         "Status": None,
                         "Suggested Action": st.column_config.TextColumn(
                             "Suggested Action",
                             width=500, 
                             pinned=True
                         )
                   },  
                   row_height=100,
                   height = 4000, width = 1000,
                   hide_index = True
            )

