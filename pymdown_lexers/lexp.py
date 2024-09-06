from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ("LexpLexer",)

class LexpLexer(RegexLexer):
    name = 'lexp'
    aliases = ['lexp']
    filenames = ['*.lexp']

    tokens = {
        'root': [
            (r'[a-z]+', Name),
            (r'[A-Z]+', Name),
            (r'\s+', Whitespace),
            (r'[0-9]+', Number),
            (r'λ', Keyword),
            (r'->', Keyword),
            (r'//.*?$', Comment.Singleline),
            (r'\(', Punctuation),
            (r'\)', Punctuation),
            (r'\.', Operator),
        ]
    }
