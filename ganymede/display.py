"""Display additional data in cell output frames."""

from IPython.display import display, HTML


def display_title(text):
    """Display a cell output frame title."""
    display(HTML("""
    <script id="{script_id}" type="text/javascript">
        (($, notebook, temple) => {{
            $script = $('#{script_id}');

            $cell = $script.parents('.cell');
            index = notebook.get_cell_elements().index($cell);

            metadata = notebook.get_cell(index).metadata;
            metadata = (metadata.ganymede = metadata.ganymede || {{}});
            metadata = (metadata.output = metadata.output || {{}});
            metadata.title = "{title}";

            temple.console.updateOutputs();

            $script.remove();
        }})(window.jQuery, window.Jupyter.notebook, window.Ganymede.temple);
    </script>
    """.format(script_id='ganymede-cell-output-title-script', title=text)))
