import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def init() -> None:
    """Create a new app / project."""
    typer.echo("VibeKit: create a new app / project. Coming soon!")


@app.command()
def acp() -> None:
    """Launch an ACP (Agent Client Protocol) server via stdio."""
    typer.echo("VibeKit: launch an ACP server via stdio. Coming soon!")


def main() -> None:
    app()
