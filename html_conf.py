from IPython.display import display, HTML
s = """

<style>

.rendered_html {
    font-family: "proxima-nova", helvetica;
    font-size: 40%;
    line-height: 1.;
}

.rendered_html h1 {
    margin: 0.25em 0em 0.5em;
    color: #015C9C;
    text-align: center;
    line-height: 1.; 
    page-break-before: always;
}

.rendered_html h2 {
    margin: 1.1em 0em 0.5em;
    color: #26465D;
    line-height: 1.;
}

.rendered_html h3 {
    margin: 1.1em 0em 0.5em;
    color: #002845;
    line-height: 1.;
}

.rendered_html li {
    line-height: .8; 
}

.prompt {
    font-size: 60%; 
}

.CodeMirror-lines {
    font-size: 60%; 
}

.output_area {
    font-size:60%; 
}

h1.bigtitle {
    margin: 4cm 1cm 4cm 1cm;
    font-size: 200%;
}

h3.point {
    font-size: 100%;
    text-align: center;
    margin: 2em 0em 2em 0em;
    #26465D
}

.logo {
    margin: 20px 0 20px 0;
}

a.anchor-link {
    display: none;
}

h1.title { 
    font-size: 300%;
}

</style>
"""
display(HTML(s))