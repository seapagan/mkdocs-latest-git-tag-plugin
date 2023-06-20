"""Main Class for this Plugin."""
import re
from typing import Literal

from git.repo import Repo
from mkdocs.plugins import BasePlugin


class LatestGitTagPlugin(BasePlugin):
    """Class for the 'mkdocs-latest-git-tag-plugin'."""

    PLUGIN_TAG = "latest-git-tag"

    def get_repo(self, file_path) -> Repo:
        """Find the repository root directory for specified 'file_path'.

        Returns a 'git.Repo' object.
        """
        return Repo(path=file_path, search_parent_directories=True)

    def on_startup(
        self, command: Literal["build", "gh-deploy", "serve"], **kwargs
    ):
        """Use new mkdocs 1.4 plugin system.

        The presence of an on_startup method (even if empty) migrates the plugin
        to the new system where the plugin object is kept across builds within
        one mkdocs serve.
        """

    def on_page_markdown(self, markdown: str, page, **kwargs) -> str | None:
        """Modify the markdown if our tag is present."""
        this_repo = self.get_repo(page.file.abs_src_path)

        try:
            last_tag = this_repo.tags[0].name
        except IndexError:
            last_tag = "No tags found"

        markdown = re.sub(
            rf"{{{{(\s)*{self.PLUGIN_TAG}(\s)*}}}}",
            last_tag,
            markdown,
            flags=re.IGNORECASE,
        )

        return markdown
