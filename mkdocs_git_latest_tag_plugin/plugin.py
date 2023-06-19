"""Main Class for this Plugin."""
import re
from typing import Literal

from mkdocs.plugins import BasePlugin


class GitLatestTagPlugin(BasePlugin):
    """GitLatestTagPlugin."""

    PLUGIN_TAG = "git-latest-tag"

    def on_startup(
        self, command: Literal["build", "gh-deploy", "serve"], **kwargs
    ):
        """Use new mkdocs 1.4 plugin system.

        The presence of an on_startup method (even if empty) migrates the plugin
        to the new system where the plugin object is kept across builds within
        one mkdocs serve.
        """

    def on_page_markdown(self, markdown: str, **kwargs) -> str | None:
        """Modify the markdown if our tag is present."""
        markdown = re.sub(
            rf"{{{{(\s)*{self.PLUGIN_TAG}(\s)*}}}}",
            "This text is from the plugin.",
            markdown,
            flags=re.IGNORECASE,
        )

        return markdown
