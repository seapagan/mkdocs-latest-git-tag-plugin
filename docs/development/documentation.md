# Documentation Website

## Development

The documentation for this project is created using
[MkDocs](https://www.mkdocs.org/){:target="_blank"} with the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}
theme.

For this project, the docs website is served using [GitHub
Pages](https://pages.github.com/){:target="_blank"}, though since it is just
HTML and CSS you can host it from any provider you choose.

Source for this is stored in the `docs` folder off the root of the project, and
consists of Markdown files. The main control file is `mkdocs.yml` in the root.

To help with documentation development you can run a docs server on
<http://localhost:9000> using the below command :

```console
$ mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.89 seconds
INFO     -  [12:55:29] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [12:55:29] Serving on http://127.0.0.1:9000/
```

If you want the site to be opened to your local network (ie to test on a
mobile or another local device), then you can use the below command :

```console
poe docs:serve
```

This will run the `mkdocs serve` command, but will also open the site on your
local network. You can then access the site on your other device using the IP
address of your machine, and the port number shown in the output of the command.

## Build the Documentation

You can create a production-ready version of the site by using the `build`
command:

```console
$ poe docs:build
INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: /home/seapagan/data/work/own/mkdocs-latest-git-tag-plugin/site
INFO     -  Documentation built in 0.34 seconds
```

This will create a static website in the `site` folder which you can then upload
to the hosting provider of your choice. See the next section if you are using
GitHub Pages.

## Publish to GitHub Pages

When you are happy with the docs, they can be published automatically to [GitHub
Pages](https://pages.github.com/){:target="_blank"} using the below command :

```console
poe docs:publish
```

This command will automatically build the docs, and then push the `site` folder
to GitHub

Note that only someone with **WRITE** access to the repository can do this.
