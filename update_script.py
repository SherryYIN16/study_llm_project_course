import re
file_path = r'C:\Users\yinxu\Documents\Codex\2026-08-04\new-chat\workflow_diagram_final.html'
md_path = r'C:\Users\yinxu\Documents\Codex\2026-08-04\new-chat\Design_Patterns_Lesson.md'

with open(file_path, 'r', encoding='utf-8') as f:
    html_c = f.read()
with open(md_path, 'r', encoding='utf-8') as f:
    md = f.read()

# Markdown 渲染转换
def render(text):
    text = re.sub(r'^# (.*)', r'<h1>\1</h1>', text, flags=re.M)
    text = re.sub(r'^## (.*)', r'<h2>\1</h2>', text, flags=re.M)
    text = re.sub(r'^### (.*)', r'<h3>\1</h3>', text, flags=re.M)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # 处理 list 列表
    text = re.sub(r'^- (.*)', r'<li>\1</li>', text, flags=re.M)
    text = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', text, flags=re.S)
    return text.replace('\n', '<br>')

md_html = render(md).replace('\'', "\\'")
wrapped_html = f'<div style=\"font-family: Segoe UI, sans-serif; font-size: 15px; color: #333;\">{md_html}</div>'

# 替换
new_c = re.sub(r'design: \{ content: \'.*?\' \}', \"design: { content: '\" + wrapped_html + \"' }\", html_c, flags=re.S)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_c)
