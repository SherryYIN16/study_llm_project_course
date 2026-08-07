file_path = r'C:\Users\yinxu\Documents\Codex\2026-08-04\new-chat\workflow_diagram_final.html'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

# ??????????
start_idx = c.find('design: { content: \'')
end_idx = c.find('\'\n        };', start_idx)

# ???????
design_part = \"design: { content: '<div style=\\\"font-family: Segoe UI, sans-serif; line-height: 1.6; color: #333; font-size: 15px;\\\">????????</div>' }\"

final_content = c[:start_idx] + design_part + c[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)
