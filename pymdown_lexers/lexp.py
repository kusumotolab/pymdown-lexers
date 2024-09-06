from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ("LexpLexer",)

class LexpLexer(RegexLexer):
    name = 'lexp'
    aliases = ['lexp']
    filenames = ['*.lexp']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'λ\w*', Name.Function),
            (r'->\w?', Keyword),
            (r'=', Keyword),
            (r';.*?$', Comment.Singleline),
            (r'//.*?$', Comment.Singleline),
            (r'\(', Punctuation),
            (r'\)', Punctuation),
            (r'\.', Operator),
            (r'[a-z]+', Name),
            (r'[A-Z]+', Name),
            (r'[0-9]+', Number),
        ]
    }
