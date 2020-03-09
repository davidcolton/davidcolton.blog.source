Author: David Colton
Date: 2020-03-09 20:05
Category: blogging
Tags: pelican, python, blogging, jupyter
Title: Adding support for Jupyter Notebooks 
Slug: ipynb_support

# Adding support for Jupyter Notebooks

In addition to adding code blocks I also want to include support for Jupyter Notebooks. Why you ask. Sometimes adding a code block is not enough, you also want to show the output of you Python. The are other options, like capturing the session from a `REPL` but I've been using Jupyter Notebooks now for many years. I was using them long before they were called Jupyter Notebooks and were, instead, known as IPython Notebooks. Anyhow, here goes.

## Installing the Plugin

When installing this plugin the instructions suggestion adding the entire pelican-plugins repository as a sub-module of my source tree. Not something I wanted to do, primarily as I don't understand Git enough to know exactly what this means. Instead I cloned the entire plugins repository, but in it's own right, and I then just copied the 'pelican-ipynb.markup' plugin into the plugins folder. My Pelican config was then updated:

    :::python
    PLUGIN_PATHS = ["plugins/"]
    PLUGINS = [
        "pelican-bootstrapify",
        "i18n_subsites",
        "pelican-ipynb.markup",
        "render_math",
    ]

## Configuring the Plugin

Before using the `'pelican-ipynb.markup' a little bit of housework is required. You you need to add '.ipynb' to the markup extensions variable, if not already defined, and you need to ignore the ever annoying '.ipynb_checkpoints' folder to the ignore file variable. If these variables don't already exist just create them:

    :::python
    MARKUP = ('md', 'ipynb')
    IGNORE_FILES = [".ipynb_checkpoints"]

# What about the Pelican Metadata

As you should know every Pelican markdown file has several metadata lines at the top of each file to tell Pelican about the article. There are a couple of option but my preference it to add them in the first cell of the Jupyter Notebook. So one more variable to add:

    :::python
    IPYNB_USE_METACELL = True

You can now just add the metadata in the first notebook cell in markdown mode like this:

    :::text
    - Author: David Colton
    - Date: 2020-03-09 20:05
    - Category: blogging
    - Tags: pelican, python, blogging, jupyter
    - Title: Adding support for Jupyter Notebooks 
    - Slug: ipynb_support

You can find [My First Jupyter Notebook]({filename}/articles/20200309_sample_ipynb.ipynb) here. You may think, hmmm, this doesn't look like a Jupyter Notebook. What's with the black cells. I've kept the sample code block CSS style from the rest of the site by setting this variable:

    :::python
    IPYNB_SKIP_CSS = True

A small inconvenience for now maybe. Another issue is that if I put Headings in the markdown it add a nasty looking link in the rendered HTML. I'd like to fix that.  

## Final Notes

Before I forget you'll need to install Jupyter.

    :::text
    pip install jupyter