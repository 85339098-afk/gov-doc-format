# gov-doc-format 变更日志

> 公文排版规范（GB/T 9704-2012）

---

> 最新版本：V2.2.9

---


## V2.2.9 (2026-05-26)

- **重要更正**：根据国家标准化管理委员会官网核实，**不存在 GB/T 9704-2022 版本**，GB/T 9704-2012 仍是现行有效标准
- 删除虚构的 `gb9704_2022.md` 参考文件
- 新增 `gb33476_2_2016.md`（GB/T 33476.2-2016《党政机关电子公文格式规范 第2部分：显现》关键条款）
- 更新 `gb9704_2012.md`：修正"2022版"不实信息，补充行距精确计算公式（来自 GB/T 33476.2-2016 附录A）
- 更新 `jg_standards.md`：补充 33476.2 参考
- 更新 SKILL.md：移除所有"2022版"引用，替换为 GB/T 33476.2-2016 正确引用

## V2.2.8 (2026-05-25)

- 修复 `add_signature.py` 中 `add_signee(doc, text="签发人：张三")` 默认参数含占位数据的问题，改为 `text` 必选参数
- 修复 `add_footer.py` 中 `RULER_W = Pt(442 - 16)` 硬编码魔法数字，改为从文档节动态计算版心宽度
- 修复 `add_page_number.py` 中 `_add_field_run` 使用原生 XML 设置字体的问题，统一为调用 `set_run_font()`
- 修复 `create_doc.py` 缺少 `add_signee` 导入的问题
- 所有 `.py` 文件的模块间导入改为相对导入（`from .xxx import`），支持从外部包导入
- 移除 `create_doc.py` 中的 `sys.path.insert` workaround

## V2.2.7 (2026-05-25)

- 修复 5 个子脚本（add_heading.py、add_footer.py、add_page_number.py、add_signature.py、format_body.py）中的绝对导入问题：`from set_font import ...` → `from .set_font import ...`
- 修复 `create_doc.py` 中 6 处模块间绝对导入为相对导入
- 移除 `create_doc.py` 中的 `sys.path.insert` workaround

## V2.2.6 (2026-05-21)

- 修复 `add_page_number.py` 中 `._r.` 私有 API 调用（`run._r.append()` → `run.element.append()`）
- 修复 `__init__.py` 中绝对导入为相对导入（`from .set_font import ...`）
- 修复 `_skillhub_meta.json` 缺少 version 字段的问题
- 新增参考文档：checklist.md、doc_types.md、font_map.md、gb9704_2012.md、gb9704_2022.md、jg_standards.md

## V2.1.0 (2026-05-21)

- 初始公开发布版本
- 核心功能：创建 A4 标准公文文档，支持标题/正文/落款/版记/页码排版
- 跨平台字体映射（Windows + Mac）
- 8 个 Python 工具模块
