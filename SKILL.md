---
name: gov-doc-format
display_name: 公文格式规范
description: 基于GB/T 9704-2012公文格式及JG报送规范的专业公文排版工具。当用户需要生成正式公文（方案、报告、通知、请示）、制作Word文档、排版材料、调整公文格式、设置页面边距/字体/行距/页码时触发。支持AI自动排版，一键生成符合国标的公文Word文档。
description_zh: 专业公文格式规范工具，严格遵循国家标准和政府报送要求，自动处理页面设置、字体字号、行距缩进、奇偶页页码等。覆盖通知、请示、报告、函、纪要、批复、通报、决定等常用文种。
triggers:
  - 公文排版
  - 公文格式
  - GB/T 9704
  - 机关公文
  - 红头文件
  - 报送格式
  - 公文规范
  - 党政机关公文
  - 通知
  - 请示
  - 报告
  - 函
  - 会议纪要
  - 批复
  - 通报
  - 决定
version: 2.2.9
date: 2026-05-25
category: 文档排版/公文格式
author: 豚豚
tags: 公文, 文档, Word, 格式, 排版, 国标, GB/T 9704, docx, python-docx, 通知, 请示, 报告
---

# 公文格式规范 Skill

严格遵循 **GB/T 9704-2012**）及 GB/T 33476.2-2016《党政机关电子公文格式规范 第2部分：显现》，生成符合标准的正式公文。

## 文件结构

```
公文格式规范/
├── SKILL.md              # 主文件（本文件）— 触发逻辑、快速参数
├── *.py                    # 可执行 Python 脚本
│   ├── create_doc.py     # 主入口 — 创建 A4 文档，设页边距，插页码
│   ├── set_font.py       # 字体设置 — 跨平台字体映射、run/paragraph 设置
│   ├── add_heading.py    # 标题生成 — 公文标题、一二三级标题
│   ├── add_page_number.py# 页码插入 — PAGE 域代码、奇偶页、格式 — N —
│   ├── format_body.py    # 正文排版 — 28磅行距、首行缩进2字符
│   ├── add_signature.py  # 落款生成 — 发文字号、签发人、落款、日期
│   └── add_footer.py     # 版记生成 — 抄送机关、印发机关、印发日期
└── *.md                    # 知识库参考文件
    ├── gb9704_2012.md    # GB/T 9704-2012 关键条款摘录
    ├── jg_standards.md   # JG 报送规范（地方标准）
    ├── font_map.md       # 字体安装和映射指南
    ├── doc_types.md      # 各文种格式速查
    └── checklist.md      # 排版完成后的自查清单
```

**使用方式**：AI 加载此 skill 后，直接调用 `` 中的函数生成公文文档，
查阅 `*.md` 参考文件获取格式规范和文种要求。

> **版本说明**：本 skill 依据 **GB/T 9704-2012**（现行有效标准，经国家标准化管理委员会官网核实，不存在 2022 版本）。

---

## 📋 快速检查清单

使用本 skill 生成公文后，逐项核对：

```
☐ 纸张 A4（210×297mm）
☐ 页边距 上37mm 下35mm 左28mm 右26mm
☐ 标题：方正小标宋简体 二号(22pt) 居中
☐ 一级标题（一、）：黑体 三号(16pt) 左空二字
☐ 二级标题（（一））：楷体 三号(16pt) 左空二字
☐ 正文：仿宋 三号(16pt)
☐ 行距：固定值 28磅（严格对标标准为29.5pt，见GB/T 33476.2-2016附录A）
☐ 首行缩进 2字符
☐ 段前段后 0磅
☐ 页码奇偶页不同（奇数页居右，偶数页居左）
☐ 首页不显示页码
☐ 页码格式：— N —
☐ 全文颜色：纯黑 RGB(0,0,0)
☐ 发文字号规范（如有）
☐ 上行文标注签发人（如有）
☐ 版记齐全（如有）
```

---

## 一、核心功能

### 1.1 页面设置
- 纸张：A4（210mm × 297mm）
- 上边距 37mm / 下边距 35mm / 左边距 28mm / 右边距 26mm
- 版心：156mm × 225mm
- 左侧装订
- 段前段后：均为 0 磅

### 1.2 字体字号

| 元素 | 字体 | 字号 | 备注 |
|------|------|------|------|
| 公文标题 | 方正小标宋简体 | 2号(22pt) 居中 | 首选方正小标宋简体 |
| 一级标题（一、） | 黑体 | 3号(16pt) 左空二字 | 不加粗 |
| 二级标题（（一）） | 楷体 | 3号(16pt) 左空二字 | 不加粗 |
| 三级标题（1.） | 仿宋 | 3号(16pt) | 可加粗 |
| 正文 | 仿宋 | 3号(16pt) | |
| 页码 | 宋体 或 Times New Roman | 4号(14pt) | 格式：— N — |
| 版记（抄送/印发） | 仿宋 | 4号(14pt) | 末页偶数页 |

**字体大小对照表：**

| 字号 | 磅值 | 用途 |
|------|------|------|
| 二号 | 22pt | 公文标题 |
| 三号 | 16pt | 正文章节标题 |
| 四号 | 14pt | 页码 |
| 小四 | 12pt | 其他 |

### 1.3 行距与排版
- 正文行距：固定值 **28 磅**
  - 严格对标标准为 **29.5pt**（见 GB/T 33476.2-2016 附录A），多数机关沿用 28pt
- 首行缩进：2 字符（≈32pt）
  - 2 字符 = 正文字号（16pt）× 2 = 32pt
  - Word 中直接设置"首行缩进 2 字符"即可，无需手动输入 32pt
- 标题（一、二级）左空二字（效果同首行缩进 2 字符）
- 段前段后：均为 0 磅
- 颜色：全文纯黑 RGB(0,0,0)

### 1.4 页码（奇偶页不同）
- 奇数页居右，偶数页居左
- 首页不显示页码（设 titlePg=True）
- 启用 evenAndOddHeaders + titlePg
- 格式：— N —（N 两侧各一字线）

### 1.5 标点符号规范
- 双引号使用中文全角：""
- 标题一、（一）、1. 后不加句号
- 正文段落结束要有句号
- 段落结束使用回车（Enter），而非换行符（Shift+Enter）

---

## 二、公文必备要素

### 2.1 发文字号
- 格式：**机关代字 + 六角括号〔〕+ 年份 + 顺序号**
- 示例：`工办〔2026〕15号`
- 年份用六角括号〔〕，不写"年"字
- 顺序号不编虚位（写"15"不写"015"）
- 标题下空一行，居中排列
- 函的发文字号中带"函"字，如：`工办函〔2026〕15号`

### 2.2 签发人
- **上行文**（请示、报告）必须标注
- 位于发文字号同行右侧
- "签发人"三字用 3 号仿宋
- 签发人姓名用 3 号楷体

### 2.3 主送机关
- 标题下空一行，左顶格
- 3 号仿宋
- 最后一个主送机关后加冒号
- ⚠️ 请示的主送机关只能有一个

### 2.4 附件说明
- 正文下空一行，左空二字
- "附件"二字用 3 号仿宋
- 附件名称后不加标点
- 有多个附件时用阿拉伯数字编号

### 2.5 落款和成文日期
- 成文日期右空四字
- 格式：`2026年5月25日`（用阿拉伯数字）
- 发文单位名称在日期上方居中
- 单位名称与日期之间空一行

### 2.6 版记
- 位于最后一页底部（末页须为偶数页 — JG 报送规范要求）
- 包含：抄送机关、印发机关、印发日期
- 抄送机关后加句号
- 印发日期右空一字

### 2.7 行文方向对照

| 方向 | 文种 | 特点 |
|------|------|------|
| 上行文 | 请示、报告 | 必须有签发人；请示一文一事、主送唯一 |
| 下行文 | 通知、通报、批复、决定 | 无签发人 |
| 平行文 | 函 | 发文字号带"函"字 |

---

## 三、常用文种模板

### 3.1 通知
- 标题：`关于……的通知`
- 发文字号居中
- 主送机关：可有多个，用逗号分隔
- 结尾：`特此通知。`
- 下行文，无需签发人

### 3.2 请示
- 标题：`关于……的请示`
- **一文一事**，主送机关**只能一个**
- **上行文，必须标注签发人**
- 结尾：`妥否，请批示。` 或 `以上请示，请予审批。`

### 3.3 报告
- 标题：`关于……的报告`
- 可一文多事
- **上行文，必须标注签发人**
- **不得夹带请示事项**
- 结尾：`特此报告。`

### 3.4 函
- 发文字号：带"函"字，如 `工办函〔2026〕15号`
- 标题：`关于……的函`
- 结尾：`特此函复。` / `此复。` / `请研究函复。`
- 平行文或下行文

### 3.5 会议纪要
- 标题：`……会议纪要`
- 不加盖公章
- 标题居中，不标发文字号
- 正文首段记录时间、地点、参会人员

### 3.6 批复
- 标题：`关于……的批复`
- 首段引述来文：`你单位《关于……的请示》收悉。`
- 结尾：`此复。` / `特此批复。`
- 下行文

### 3.7 通报
- 标题：`关于……的通报`
- 正文包含事实陈述与评价
- 结尾：`特此通报。`
- 下行文

### 3.8 决定
- 标题：`关于……的决定`
- 正文含决定事项，常用`决定如下` / `特作如下决定`
- 下行文

---

## 四、正文层次序数

| 层级 | 格式 | 说明 |
|------|------|------|
| 第一层 | 一、二、三…… | 黑体三号 |
| 第二层 | （一）（二）（三）…… | 楷体三号 |
| 第三层 | 1. 2. 3.…… | 仿宋三号（可加粗） |
| 第四层 | （1）（2）（3）…… | 仿宋三号 |

> **标题换行规则**：标题过长须换行时，一般不超过两行。换行时顶格书写（不加缩进），保持"一、二、三……"的字样完整。

---

## 五、文件命名规范

格式：`机关代字〔年份〕顺序号-文种.docx`
示例：`工办〔2026〕15号-通知.docx`

> 密级和紧急程度如涉及，在版心左上角标注。密级："绝密""机密""秘密"；紧急程度："特急""加急"。

---

## 六、辅助函数

### 6.1 段落类型自动识别（含日期行检测）

遍历现有 docx 段落时，自动判断每段该用什么格式，无需手动标记。

```python
import re


def classify_paragraph(text):
    """
    根据段落文本内容自动判断段落类型。

    Args:
        text: 段落纯文本

    Returns:
        dict: {
            'type': 'title'|'heading1'|'heading2'|'heading3'|'body'|'date'|'doc_number'|'signee',
            'style': 对应格式名称,
            'font': 字体名,
            'size': 字号(Pt),
            'bold': 是否加粗,
            'alignment': 对齐方式,
            'indent': 首行缩进(Pt),
            'right_indent': 右缩进(Pt),
        }
    """
    text = text.strip()
    if not text:
        return {'type': 'empty', 'font': None}

    # --- 公文标题检测（居中、无编号，与其他段落区分） ---
    # 特征：行首无编号、长度适中、不含句号
    if (not re.match(r'^[一二三四五六七八九十（〔\[【]', text)
            and not re.match(r'^[①②③④]', text)
            and len(text) <= 40
            and not text.endswith('。')
            and '年' not in text
            and '号' not in text):
        return {
            'type': 'title',
            'font': '方正小标宋简体',
            'size': Pt(22),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'indent': Pt(0),
        }

    # --- 日期行检测 ---
    if re.search(r'\d{4}年\d{1,2}月\d{1,2}日', text):
        return {
            'type': 'date',
            'font': '仿宋_GB2312',
            'size': Pt(16),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.RIGHT,
            'indent': Pt(0),
            'right_indent': Pt(64),  # 右空四字
        }

    # --- 发文字号检测 ---
    if re.search(r'〔\d{4}〕\d+号', text):
        return {
            'type': 'doc_number',
            'font': '仿宋_GB2312',
            'size': Pt(16),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.CENTER,
            'indent': Pt(0),
        }

    # --- 签发人检测 ---
    if text.startswith('签发人'):
        return {
            'type': 'signee',
            'font': '仿宋_GB2312',
            'size': Pt(16),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.RIGHT,
            'indent': Pt(0),
        }

    # --- 一级标题（一、二、三……） ---
    if re.match(r'^[一二三四五六七八九十]+、', text):
        return {
            'type': 'heading1',
            'font': '黑体',
            'size': Pt(16),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'indent': Pt(32),
        }

    # --- 二级标题（（一）（二）（三）……） ---
    if re.match(r'^（[一二三四五六七八九十]+）', text):
        return {
            'type': 'heading2',
            'font': '楷体_GB2312',
            'size': Pt(16),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'indent': Pt(32),
        }

    # --- 三级标题（1. 2. 3.……） ---
    if re.match(r'^\d+[．.、]', text):
        return {
            'type': 'heading3',
            'font': '仿宋_GB2312',
            'size': Pt(16),
            'bold': True,  # 三级标题推荐加粗与正文区分
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'indent': Pt(32),
        }

    # --- 附件说明检测 ---
    if text.startswith('附件'):
        return {
            'type': 'attachment',
            'font': '仿宋_GB2312',
            'size': Pt(16),
            'bold': False,
            'alignment': WD_ALIGN_PARAGRAPH.LEFT,
            'indent': Pt(32),
        }

    # --- 普通正文（兜底） ---
    return {
        'type': 'body',
        'font': '仿宋_GB2312',
        'size': Pt(16),
        'bold': False,
        'alignment': WD_ALIGN_PARAGRAPH.LEFT,
        'indent': Pt(32),
    }
```

### 6.2 统一段落格式设置函数

升级版 `set_paragraph_format`，替代原有的 `set_run_font`。改进点：
- 使用 `rPr.get_or_add_rFonts()` 避免 rFonts 为 None 时报错
- 行距使用 `Pt(28)` 而非硬编码
- 一次调用即可设置字体、字号、加粗、对齐、缩进、行距

```python
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement


def set_paragraph_format(p, font_name, size=Pt(16), bold=False,
                         alignment=None, indent=Pt(32), line_spacing=Pt(28),
                         right_indent=Pt(0)):
    """
    统一设置段落格式。

    Args:
        p: Paragraph 对象
        font_name: 字体名称（如 '仿宋_GB2312'）
        size: 字号，默认 16pt（三号）
        bold: 是否加粗
        alignment: 对齐方式（WD_ALIGN_PARAGRAPH 枚举）
        indent: 首行缩进，默认 2 字符（32pt），标题设 Pt(0)
        line_spacing: 行距，默认固定值 28 磅
        right_indent: 右缩进（用于日期右空四字 = Pt(64)）
    """
    # 对齐方式
    if alignment is not None:
        p.alignment = alignment

    # 段落缩进与行距
    pf = p.paragraph_format
    pf.line_spacing = line_spacing
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.first_line_indent = indent
    if right_indent:
        pf.right_indent = right_indent

    # 设置 run 级别字体
    for run in p.runs:
        run.font.name = font_name
        run.font.size = size
        run.font.bold = bold
        run.font.color.rgb = RGBColor(0, 0, 0)
        # 双重防护：rPr 和 rFonts 都可能不存在
        rPr = run.element.rPr
        if rPr is None:
            rPr = run.element.get_or_add_rPr()
        rPr.get_or_add_rFonts().set(qn('w:eastAsia'), font_name)
```

### 6.3 表格格式化

修复 `row_index` 未定义 bug，使用 `enumerate`。

```python
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def format_table(table, font_name='仿宋', font_size=Pt(16)):
    """
    格式化表格：设置所有单元格字体为公文规范字体。

    Args:
        table: Table 对象（python-docx）
        font_name: 字体名称，默认仿宋
        font_size: 字号，默认 16pt（三号）
    """
    for row_idx, row in enumerate(table.rows):  # ✅ 改用 enumerate 修复 row_index 未定义
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                # 表格内段落首行不缩进
                paragraph.paragraph_format.first_line_indent = Pt(0)
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(0)
                for run in paragraph.runs:
                    run.font.name = font_name
                    run.font.size = font_size
                    run.font.color.rgb = RGBColor(0, 0, 0)
                    rPr = run.element.rPr
                    if rPr is None:
                        rPr = run.element.get_or_add_rPr()
                    rPr.get_or_add_rFonts().set(qn('w:eastAsia'), font_name)
```

### 6.4 整合调用示例

利用 `classify_paragraph` + `set_paragraph_format` 实现自动化排版：

```python
def auto_format_paragraph(doc, text, table=None):
    """
    自动识别段落类型并应用对应格式。

    Args:
        doc: Document 对象
        text: 段落文本
        table: 可选，Table 对象（如有则先格式化表格）
    """
    # 如有表格，先格式化
    if table is not None:
        format_table(table)

    # 自动识别段落类型
    info = classify_paragraph(text)

    if info['type'] == 'empty':
        return None

    # 添加段落
    p = doc.add_paragraph(text)

    # 应用格式
    set_paragraph_format(
        p,
        font_name=info['font'],
        size=info['size'],
        bold=info['bold'],
        alignment=info.get('alignment'),
        indent=info.get('indent', Pt(32)),
        right_indent=info.get('right_indent', Pt(0)),
    )

    return p


# ===== 使用示例 =====
texts = [
    "×××办公室关于印发《公文格式规范》的通知",    # → 公文标题
    "工办〔2026〕15号",                           # → 发文字号
    "各科室、各下属单位：",                       # → 正文
    "一、总体要求",                               # → 一级标题
    "为规范公文格式，提高办文质量……",             # → 正文
    "（一）页面设置",                              # → 二级标题
    "1. 字体字号要求",                            # → 三级标题
    "×××办公室",                                # → 落款
    "2026年5月25日",                              # → 日期行（自动右空四字）
]

doc = Document()
for t in texts:
    auto_format_paragraph(doc, t)
```

---

## 七、python-docx 实现要点

### 7.1 环境准备

```bash
pip install python-docx
```

### 7.2 ⚠️ 关键陷阱：标题字体必须显式设置在 run 级别

`doc.add_heading()` 创建的标题段落，**仅设置 style 不够**，必须遍历每个 run 显式设置字体，否则 Word 会显示默认字体。

推荐使用 §6.2 的 `set_paragraph_format()` 统一设置段落格式，它已内置 run 级别字体防护逻辑：

```python
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_heading1(doc, text):
    """添加一级标题（黑体三号左空二字）"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.first_line_indent = Pt(32)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    set_paragraph_format(p, '黑体', size=Pt(16), bold=False,
                         alignment=WD_ALIGN_PARAGRAPH.LEFT)
    return p
```

### 7.3 完整文档初始化

```python
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsdecls

def create_official_doc():
    """创建标准公文文档"""
    doc = Document()
    
    # === 页面设置 ===
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(3.7)
    section.bottom_margin = Cm(3.5)
    section.left_margin = Cm(2.8)
    section.right_margin = Cm(2.6)
    
    # === 奇偶页页码设置 ===
    section.different_first_page_header_footer = True  # titlePg
    section.even_and_odd_header_footer = True  # evenAndOddHeaders
    
    return doc
```

### 7.4 页码插入（PAGE 域代码）

```python
def add_page_number(section):
    """为文档节添加页码 — N — 格式"""
    # 奇数页页码（居右）
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    # 插入 "— "
    run = p.add_run('— ')
    run.font.name = '宋体'
    run.font.size = Pt(14)
    
    # 插入 PAGE 域代码
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    run.element.append(fldChar1)
    
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = ' PAGE '
    run.element.append(instrText)
    
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    run.element.append(fldChar2)
    
    # 插入 " —"
    run = p.add_run(' —')
    run.font.name = '宋体'
    run.font.size = Pt(14)
    
    # 偶数页页码（居左）
    even_footer = section.even_page_footer
    even_footer.is_linked_to_previous = False
    p = even_footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    # ... 同上插入代码
```

### 7.5 表格单元格特殊处理

推荐使用 §7.3 的 `format_table()` 一键格式化整表。如需逐格处理：

```python
def set_cell_content(cell, text, font_name='仿宋', size=Pt(16)):
    """设置表格单元格内容：无缩进"""
    p = cell.paragraphs[0]
    p.paragraph_format.first_line_indent = Pt(0)  # ⚠️ 必须显式设0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.name = font_name
    run.font.size = size
    run.font.color.rgb = RGBColor(0, 0, 0)
    rPr = run.element.rPr
    if rPr is None:
        rPr = run.element.get_or_add_rPr()
    rPr.get_or_add_rFonts().set(qn('w:eastAsia'), font_name)
```

### 7.6 字体兼容说明

**推荐写法（跨平台兼容）：**

```python
FONT_MAP = {
    '仿宋_GB2312': '仿宋',    # Mac 回退
    '楷体_GB2312': '楷体',    # Mac 回退
}
# Mac 上黑体需用 '华文黑体' 或 'STHeiti'

def get_available_font(font_gb2312):
    """根据系统选择可用字体"""
    import platform
    if platform.system() == 'Darwin':
        return FONT_MAP.get(font_gb2312, font_gb2312)
    return font_gb2312  # Windows 直接使用 _GB2312 字体
```

> **⚠️ 字体说明（修正版）**：
> - Windows 优先使用 `仿宋_GB2312`、`楷体_GB2312`
> - Mac 环境没有 `_GB2312` 后缀字体，自动回退为 `仿宋`、`楷体`
> - `_GB2312` 后缀并非强制要求，`resolve_font_name()` 已自动处理跨平台映射
> - 优先使用带 `_GB2312` 后缀的版本，Mac 环境做字体映射回退

---

## 八、常见错误排查表

| 常见错误 | 原因 | 解决方法 |
|---------|------|---------|
| 标题显示为 MS Gothic | 只设了 style 没设 run 级别字体 | 使用 `set_paragraph_format()`（见 §6.2） |
| 表格里文字也缩进了 | first_line_indent 被继承 | 使用 `format_table()`（见 §6.3）或显式设 0 |
| 页码打印时不更新 | 域代码没更新 | 打开文件后全选 → F9 更新域 |
| 第一页也显示页码 | 没设 titlePg | 设置 different_first_page_header_footer=True |
| 奇偶页页码都在同一侧 | 没启用 evenAndOddHeaders | 设置 even_and_odd_header_footer=True |
| 段落间距不对 | 段前段后没设 0 | 显式设 space_before=0 space_after=0 |
| Mac 字体显示异常 | 没有 _GB2312 字体 | 使用字体映射回退（见 §7.6） |
| 发文字号六角括号显示错误 | 用了 [ ] 代替 〔〕 | 使用全角符号：〔〕U+3014/U+3015 |

---

## 九、使用方式

直接描述需求即可，例如：
- "生成一份正式通知，按公文格式排版"
- "把这个文档改成 JG 报送格式"
- "帮我调整段落格式，首行缩进 2 字符，28 磅行距"
- "写一份请示，标题是'关于采购办公设备的请示'"
- "帮我生成会议纪要，含参会人员和时间"

---

## 十、快速参数速查

| 参数 | 值 |
|------|-----|
| 页边距-上 | 37mm |
| 页边距-下 | 35mm |
| 页边距-左 | 28mm |
| 页边距-右 | 26mm |
| 正文行距 | 固定值 28 磅（严格对标为 29.5pt，见 GB/T 33476.2-2016） |
| 首行缩进 | 2 字符（≈32pt） |
| 标题字号 | 2 号（22pt） |
| 正文字号 | 3 号（16pt） |
| 页脚字号 | 4 号（14pt） |
| 页码格式 | — N — |
| 纸张 | A4（210×297mm） |
| 段前段后 | 0 磅 |
| 全文颜色 | RGB(0,0,0) |
