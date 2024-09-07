from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("LambdaExpressionLexer",)

class LambdaExpressionLexer(RegexLexer):
    name = 'Lambda Expression'
    aliases = ['lexp', 'lambda-expression']
    filenames = ['*.lexp']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'(λ)(\w*)', bygroups(Name.Function, Name.Entity)),
            (r'[\(\)]', Punctuation),
            (r'->\w?', Operator),
            (r'=', Operator),
            (r'[\.\+\-\*/]', Operator),
            (r';.*?$', Comment.Singleline),
            (r'//.*?$', Comment.Singleline),
            (r'[a-zA-Z]+', Name),
            (r'[0-9]+', Number),
        ]
    }
