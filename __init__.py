"""
公文格式规范 — 脚本工具包

提供公文排版所需的全部 Python 工具函数。

注意：使用相对导入（加 . 前缀），确保不论从哪个入口导入都能正确解析。
"""

from .set_font import (
    set_run_font, set_paragraph_font, set_paragraph_spacing,
    set_first_line_indent, resolve_font_name, FONT_MAP, get_platform,
)
from .add_heading import (
    add_title, add_heading1, add_heading2, add_heading3,
)
from .add_page_number import add_page_number
from .format_body import add_body_text, add_body_text_no_indent
from .add_signature import add_doc_number, add_signee, add_organization, add_date
from .add_footer import add_cc_line, add_dispatch_info
from .create_doc import create_official_doc
