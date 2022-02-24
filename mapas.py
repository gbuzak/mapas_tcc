import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit

###### BEM-ESTAR ################

HtmlFile1 = open("./Bem_estar_2014.html", 'r',
                 encoding='utf-8')
source_code1 = HtmlFile1.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code1, width=1000, height=450)

HtmlFile2 = open("./Bem_estar_2018.html", 'r',
                 encoding='utf-8')
source_code2 = HtmlFile2.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code2, width=1000, height=450)

###### Oportunidade ###############

HtmlFile3 = open("./Oportunidade_2014.html", 'r',
                 encoding='utf-8')
source_code3 = HtmlFile3.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code3, width=1000, height=450)

HtmlFile4 = open("./Oportunidade_2018.html", 'r',
                 encoding='utf-8')
source_code4 = HtmlFile4.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code4, width=1000, height=450)

###### Seguranca ###############

HtmlFile5 = open("./Seguranca_2014.html", 'r',
                 encoding='utf-8')
source_code5 = HtmlFile5.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code5, width=1000, height=450)

HtmlFile6 = open("./Seguranca_2018.html", 'r',
                 encoding='utf-8')
source_code6 = HtmlFile6.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code6, width=1000, height=450)

###### Acesso ###############

HtmlFile7 = open("./Acesso_2014.html", 'r',
                 encoding='utf-8')
source_code7 = HtmlFile7.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code7, width=1250, height=450)

HtmlFile8 = open("./Acesso_2018.html", 'r',
                 encoding='utf-8')
source_code8 = HtmlFile8.read()

# Render the h1 block, contained in a frame of size 200x200.
components.html(source_code8, width=1250, height=450)
