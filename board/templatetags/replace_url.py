from django import template
import re
register = template.Library()


@register.filter
def replace_url(text):
    # FIXME:URLの正規表現が不十分
    matched_url_list = re.findall(r'https?://.*', text)
    # NOTE:1回だけのループでは置換した文字列を更に置換してしまうため、2回連続ループの処理を行う
    for i in range(len(matched_url_list)):
        text = re.sub(matched_url_list[i], '##%%##%%##', text)
    for i in range(len(matched_url_list)):
        replace_template = \
            '<a href="' + matched_url_list[i] + '">' + matched_url_list[i] + '</a>'
        text = re.sub('##%%##%%##', replace_template, text)
    return text
