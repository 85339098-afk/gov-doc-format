"""
字体设置工具 — 公文格式规范

提供跨平台字体设置函数，处理 run 级别字体、段落批量设置、Mac/Windows 字体映射。
"""

import platform
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn

# ============================================================
# 字体映射（跨平台兼容）
# ============================================================
# Windows 优先使用 _GB2312 后缀字体
# Mac 没有 _GB2312 字体，自动回退到无后缀版本

FONT_MAP = {
    '仿宋_GB2312': '仿宋',        # Mac 回退
    '楷体_GB2312': '楷体',        # Mac 回退
}

# Mac 上黑体名称
MAC_HEI_TI = '华文黑体'  # 或 'STHeiti'


def get_platform():
    """返回当前系统平台：'windows' | 'darwin' | 'linux'"""
    sys_name = platform.system()
    if sys_name == 'Windows':
        return 'windows'
    elif sys_name == 'Darwin':
        return 'darwin'
    return 'linux'


def resolve_font_name(font_name):
    """
    根据系统和字体名称返回可用的字体名。

    Args:
        font_name: 原始字体名称（如 '仿宋_GB2312'）

    Returns:
        当前系统可用的字体名称
    """
    if get_platform() == 'darwin':
        return FONT_MAP.get(font_name, font_name)
    return font_name


def set_run_font(run, font_name, size=Pt(16), bold=False, color=RGBColor(0, 0, 0)):
    """
    设置 run 级别字体（含 rPr 空值防护）。

    Args:
        run: python-docx Run 对象
        font_name: 字体名称（如 '仿宋_GB2312'）
        size: 字号，默认 16pt（三号）
        bold: 是否加粗，默认 False
        color: 颜色，默认纯黑 RGB(0,0,0)
    """
    resolved = resolve_font_name(font_name)
    run.font.name = resolved
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color

    # ⚠️ rPr 和 rFonts 都可能不存在，需双重防护
    rPr = run.element.rPr
    if rPr is None:
        rPr = run.element.get_or_add_rPr()
    # get_or_add_rFonts() 确保 rFonts 子元素一定存在
    rPr.get_or_add_rFonts().set(qn('w:eastAsia'), resolved)


def set_paragraph_font(paragraph, font_name, size=Pt(16), bold=False):
    """
    批量设置段落中所有 run 的字体。

    Args:
        paragraph: python-docx Paragraph 对象
        font_name: 字体名称
        size: 字号
        bold: 是否加粗
    """
    for run in paragraph.runs:
        set_run_font(run, font_name, size=size, bold=bold)


def set_paragraph_spacing(paragraph, line_spacing=Pt(28), space_before=Pt(0), space_after=Pt(0)):
    """设置段落行距和段前段后间距。"""
    pf = paragraph.paragraph_format
    pf.line_spacing = line_spacing
    pf.space_before = space_before
    pf.space_after = space_after


def set_first_line_indent(paragraph, indent=Pt(32)):
    """设置首行缩进（默认 2 字符 = 32pt）。"""
    paragraph.paragraph_format.first_line_indent = indent
