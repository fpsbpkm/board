from django import template
import re
register = template.Library()


@register.filter
def anchor(text):
    matched = re.findall(r'&gt;&gt;\d+', text)
    # NOTE:1回だけのループでは置換した文字列を更に置換してしまうため、2回連続ループの処理を行う
    #      例えば, 「>>1」 -> 「<a href="#1"> >>1 </a>」 と置換できるが、1回のみのループでは
    #      置換後の文字列の「>>1」を再び置換してしまう
    for i in range(len(matched)):
        # HACK:一時的にアンカーがあった箇所を示す文字列を「%&##%&」としているが、
        #      ユーザが入力する可能性がある
        text = re.sub(matched[i], '%&##%&', text)
    for i in range(len(matched)):
        replace_template = \
            '<a href="#' + matched[i][8:] + '">' + matched[i] + '</a>'
        text = re.sub('%&##%&', replace_template, text)
    return text
