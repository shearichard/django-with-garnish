# Documentation Notes
## Summary
Documentation is created using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/getting-started/), which allow text files written in [Markdown](https://www.markdownguide.org/cheat-sheet/) to be able to be built into a set of HTML output files which can be served by any suitable means.

The theme used is [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

## Distributing documentation
MKDocs allows the markdown files that make up the documentation to be built into HTML files and this is the form the documentation will be distributed. Various options exist to export the documentation to PDF format but that process is outside the scope of this document.

## Building documentation
To build MkDoc derived output, or to use the prototype server the Python 'pipenv', 'django-with-garnish', virtual environment must be enabled as follows.

```
pipenv shell
```

After that `cd` into `djwg-docs`

```
cd djwg-docs
```

Now you may either build a HTML representation of the markdown files

```
mkdocs build
```

or launch a propotype server to allow changes to be made to the Markdown files in `docs` and the results to be seen immediately in a web browser.

```
mkdocs server
```

