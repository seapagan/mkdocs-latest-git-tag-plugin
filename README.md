# MkDocs Plugin : `latest-git-tag`

This is a simple [MkDocs](https://www.mkdocs.org/) plugin that just gets the
most recent `Tag` from the local Git repository and makes it available as a
markdown tag in the template.

The Tag is just returned as a string with no formatting applied. If none is
found, it returns "No Tags found"

## Installation

Install the package with pip:

```bash
pip install mkdocs-latest-git-tag-plugin
```

or, if you are using [Poetry](https://python-poetry.org):

```bash
poetry add mkdocs-latest-git-tag-plugin --group dev
```

## Usage

Activate the plugin in your `mkdocs.yml`:

```yaml
plugins:
  - latest-git-tag
```

 > If you have no `plugins` entry in your config file yet, you'll likely also
want to add the `search` plugin. MkDocs enables it by default if  here is no
`plugins` entry set.

Then, in your template, you can use the `{{ latest_git_tag }}` variable:

```markdown
# My Project

Version: {{ latest_git_tag }}
```

The spaces around the tag are optional and it is case insensitive.
