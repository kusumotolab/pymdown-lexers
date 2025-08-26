from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("MultibyteBnfLexer",)

class MultibyteBnfLexer(RegexLexer):
    name = 'MultibyteBNF'
    aliases = ['mbnf']
    filenames = ['*.mbnf']
    mimetypes = ['text/x-bnf']

    tokens = {
        'root': [
            (r'(<)(.*?)(>)', bygroups(Punctuation, Name.Builtin, Punctuation)),
            (r'::=', Operator),
            (r'\|+', Operator),
            (r'"(.*?)"', String.Double),
            (r"'(.*?)'", String.Single),
            (r';', Punctuation),
            (r'//.*?$', Comment),
        ],
    }
