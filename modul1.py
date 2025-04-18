import streamlit as st

st.write('Kelompok 3')
st.write('Dila')
st.write('Wulan')
st.write('Zahra')

st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""This is our Subheader""")
st.caption("""This is our caption""")

#Displaying Latex
st.latex(r'''cos2\theta = 1 -2 sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + 2ab""")
st.latex(r'''
\frac{\partial^2 u}{\partial t^2} = h^2 \left( 
\frac{\partial^2 u}{\partial x^2} + 
\frac{\partial^2 u}{\partial y^2} + 
\frac{\partial^2 u}{\partial z^2} 
\right)
''')


#Displaying Python code
st.subheader("""Python Code""")
code = ''' def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')

#Displaying Java code
st.subheader("""Java Code""")
st.code("""public class CFG {
    public static void main(String[] args)
    {
        System.out.println("Hello, World!");
    }
}""", language='javascript')
st.subheader("""JavaScript Code""")
st.code(""" <p id="demo></p><script>
        try {
        document.getElementById("demo").innerHTML = "err.message";
        }</script""")

