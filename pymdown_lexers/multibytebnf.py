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
            (r'(<)(.+?)(>)',
            #(r'(<)([ -;=?-~]+)(>)',
             bygroups(Punctuation, Name.Class, Punctuation)),
            (r'\{', String.Escape),
            (r'\}\*', String.Escape),
            (r'\+', String.Escape),
            #.*?(\}\*)', String.Escape, String.Escape),

            # an only operator
            (r'::=', Operator),

            # fallback
            (r'[^<>:{}*\+]+', Text),  # for performance
            (r'.', Text),
        ],
    }
