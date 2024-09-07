from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("BetterTextLexer",)

class BetterTextLexer(RegexLexer):
    name = 'Better Text'
    aliases = ['btxt', 'better-text']
    filenames = ['*.btxt']

    tokens = {
        'root': [
            (r'\?\?\?', String.Escape),
            (r'^[\da-zA-Z]+:', Name.Function),

            (r'[↑↓→←]', Operator),

            (r'^(#)( .*)$', bygroups(Operator, Text)),

            (r'[(){}\[\]]', Punctuation),

            (r';.*?$', Comment),
            (r'//.*?$', Comment),
            (r'#\s.*?$', Comment),

            (r'[-~@#$%\^!+*<>\\/|&=:.]+', Operator),

            (r'\'([^\'\\]|\\(x[\da-fA-F]+|\d+|.))\'', Literal.Char),

            (r'[+~-]?\d+\b', Number.Integer),
            (r'\b[\dA-F]{2}\b', Number),  # FF AB
            (r'\b[\da-f]{8}\b', Number),  # ffffcc24
            #(r'[+~-]?[\da-fA-F]+\b', Name),


            (r'\b(for|in|while|do|break|return|continue|switch|case|default|if|else|'
             r'throw|try|catch|finally|yield|await|async|this|of|static|export|'
             r'import|debugger|extends|super|private|final)\b', Keyword),
            (r'\b(abstract|boolean|byte|char|double|enum|final|float|goto|'
             r'implements|int|interface|long|native|package|private|protected|'
             r'public|short|synchronized|throws|transient|volatile)\b', Keyword.Reserved),

            (r'\s+', Whitespace),

        ]
    }
