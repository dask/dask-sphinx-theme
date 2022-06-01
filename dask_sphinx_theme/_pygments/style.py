from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    Error,
    Number,
    Operator,
    Generic,
    Whitespace,
    Punctuation,
    Literal,
    String,
)


class DaskStyle(Style):
    default_style = ""
    background_color = "#ffffff"

    green = "#17955C"
    blue = "#1F5AFF"
    red = "#EF1161"
    purple = "#F61FFF"
    salmon = "#FC6E6B"
    dusty_blue = "#183D72"
    black = "#080815"

    styles = {
        # No corresponding class for the following:
        # Text:                     "", # class:  ''
        Whitespace: "#ffffff",  # class: 'w'
        Error: f"bold {salmon}",  # class: 'err'
        Comment: f"italic {dusty_blue}",  # class: 'c'
        Comment.Multiline: f"italic {dusty_blue}",  # class: 'cm'
        Comment.Preproc: f"italic {dusty_blue}",  # class: 'cp'
        Comment.Single: f"italic {dusty_blue}",  # class: 'c1'
        Comment.Special: f"italic {dusty_blue}",  # class: 'cs'
        Keyword: f"bold {green}",  # class: 'k'
        Keyword.Constant: f"bold {green}",  # class: 'kc'
        Keyword.Declaration: f"bold {green}",  # class: 'kd'
        Keyword.Namespace: f"bold {green}",  # class: 'kn'
        Keyword.Pseudo: f"bold {green}",  # class: 'kp'
        Keyword.Reserved: f"bold {green}",  # class: 'kr'
        Keyword.Type: f"bold {green}",  # class: 'kt'
        Operator: black,  # class: 'o'
        Operator.Word: f"bold {purple}",  # class: 'ow' - like keywords
        Punctuation: black,  # class: 'p'
        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name: black,  # class: 'n'
        Name.Attribute: salmon,  # class: 'na' - to be revised
        Name.Builtin: green,  # class: 'nb'
        Name.Builtin.Pseudo: green,  # class: 'bp'
        Name.Class: f"bold {blue}",  # class: 'nc' - to be revised
        Name.Constant: black,  # class: 'no' - to be revised
        Name.Decorator: purple,  # class: 'nd' - to be revised
        Name.Entity: salmon,  # class: 'ni'
        Name.Exception: f"bold {salmon}",  # class: 'ne'
        Name.Function: blue,  # class: 'nf'
        Name.Property: black,  # class: 'py'
        Name.Label: salmon,  # class: 'nl'
        Name.Namespace: f"bold {blue}",  # class: 'nn' - to be revised
        Name.Other: black,  # class: 'nx'
        Name.Tag: f"bold {green}",  # class: 'nt' - like a keyword
        Name.Variable: black,  # class: 'nv' - to be revised
        Name.Variable.Class: black,  # class: 'vc' - to be revised
        Name.Variable.Global: black,  # class: 'vg' - to be revised
        Name.Variable.Instance: black,  # class: 'vi' - to be revised
        # since the tango light blue does not show up well in text, we choose
        # a pure blue instead.
        Number: black,  # class: 'm'
        Number.Float: black,  # class: 'mf'
        Number.Hex: black,  # class: 'mh'
        Number.Integer: black,  # class: 'mi'
        Number.Integer.Long: black,  # class: 'il'
        Number.Oct: black,  # class: 'mo'
        Literal: black,  # class: 'l'
        Literal.Date: black,  # class: 'ld'
        String: red,  # class: 's'
        String.Backtick: red,  # class: 'sb'
        String.Char: red,  # class: 'sc'
        String.Doc: f"italic {dusty_blue}",  # class: 'sd' - like a comment
        String.Double: red,  # class: 's2'
        String.Escape: red,  # class: 'se'
        String.Heredoc: red,  # class: 'sh'
        String.Interpol: red,  # class: 'si'
        String.Other: red,  # class: 'sx'
        String.Regex: red,  # class: 'sr'
        String.Single: red,  # class: 's1'
        String.Symbol: red,  # class: 'ss'
        Generic: black,  # class: 'g'
        Generic.Deleted: salmon,  # class: 'gd'
        Generic.Emph: f"italic {black}",  # class: 'ge'
        Generic.Error: "#ef2929",  # class: 'gr'
        Generic.Heading: f"bold {green}",  # class: 'gh'
        Generic.Inserted: green,  # class: 'gi'
        Generic.Output: black,  # class: 'go'
        Generic.Prompt: black,  # class: 'gp'
        Generic.Strong: f"bold {black}",  # class: 'gs'
        Generic.Subheading: f"bold {purple}",  # class: 'gu'
        Generic.Traceback: f"bold {salmon}",  # class: 'gt'
    }
