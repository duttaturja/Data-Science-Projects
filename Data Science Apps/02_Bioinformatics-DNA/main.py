#importing libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#getting the image
image = Image.open('DNA.jpg') 

#showing the image
st.image(image, use_column_width=True)

#app starts here
st.write("""
# DNA Nucleotides Count App
This app counts the nucleotide composition of query DNA!
***
""")

#input
st.sidebar.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
#user input
sequence = st.sidebar.text_area("Sequence input", sequence_input, height=150)
sequence = sequence.splitlines() #splits lines
sequence = sequence[1:] #skips the sequence name (first line)
sequence = ''.join(sequence) #concatenates list of strings

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

#output starts here
st.header('OUTPUT (DNA Nucleotide Count)')

#showing the result as a dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_value = list(X.values())

X

#showing the result as a plain text 
st.subheader('2. Print text')
st.write ("There are " + str(X["A"]) + " adenine (A)")
st.write ("There are " + str(X["T"]) + " thymine (T)")
st.write ("There are " + str(X["G"]) + " guanine (G)")
st.write ("There are " + str(X["C"]) + " cytosine (C)")


#showing the result as a table
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index': 'nucleotide'})
st.write(df)


#showing the result as a bar chart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='Count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar. defaults to 31
)
st.altair_chart(p, use_container_width=True)