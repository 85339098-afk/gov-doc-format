## gov-doc-format V2.2.9 — 标准修正版

### 背景

根据对国家标准化管理委员会官网（https://std.samr.gov.cn）的核实：

1. **GB/T 9704-2012** 是「党政机关公文格式」的唯一现行有效标准（2012-06-29 发布，2012-07-01 实施）
2. **不存在 GB/T 9704-2022 版本** — 此前 skill 中引用的"2022版"为不实信息
3. **GB/T 33476.2-2016**《党政机关电子公文格式规范 第2部分：显现》是与公文排版高度相关的配套标准

### 主要变更

#### 🔴 标准引用修正

| 文件 | 操作 | 说明 |
|------|------|------|
| `gb9704_2022.md` | 删除 | 基于不存在的标准，全部内容不可靠 |
| `gb9704_2012.md` | 重写 | 标明为现行有效标准；行距引用 33476.2 的精确计算 |
| `gb33476_2_2016.md` | 新增 | 含行距计算公式、版心验证、22行/页、25个公文域命名表 |
| `jg_standards.md` | 更新 | 补充 33476.2 参考 |
| `SKILL.md` | 更新 | 6处"2022版"引用全部替换为 33476.2 引用 |
| `_skillhub_meta.json` | 更新 | 修正描述中的标准版本号 |
| `format_body.py` | 更新注释 | 移除"2022版行距28.95pt"误导性注释 |

#### 🔧 代码修复（V2.2.8 延续）

| 修复项 | 说明 |
|--------|------|
| `add_signee()` 默认参数 | 移除占位数据"张三"，`text` 改为必选参数 |
| `RULER_W` 硬编码 | 改为从文档节动态计算版心宽度 |
| `_add_field_run` 字体设置 | 统一为调用 `set_run_font()`，消除原生 XML 旧代码 |
| `create_doc.py` import | 补全 `add_signee` 导入 |
| 模块间导入路径 | 5个子脚本统一改为相对导入（`from .xxx import`） |
| `sys.path.insert` workaround | 移除 |

### 行距精确公式（来自 GB/T 33476.2-2016 附录A）

```
3号字字高     ≈ 5.54mm
7/8字高      ≈ 4.84mm（3号字高度 × 7/8）
一行总高度    ≈ 10.39mm
Word固定值   ≈ 29.5pt（10.39mm ÷ 25.4 × 72dpi）
```

> 28pt 是实践中形成的通用值，并非标准规定。

### 文件列表

```
CHANGELOG.md
SKILL.md
_skillhub_meta.json
__init__.py
add_footer.py
add_heading.py
add_page_number.py
add_signature.py
checklist.md
create_doc.py
doc_types.md
font_map.md
format_body.py
gb33476_2_2016.md
gb9704_2012.md
jg_standards.md
set_font.py
```
