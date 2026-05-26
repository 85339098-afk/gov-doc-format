# 字体安装和映射指南

---

## 1. 公文所需字体一览

| 字体名称 | 用途 | Windows | Mac |
|---------|------|---------|-----|
| 方正小标宋简体 | 公文标题 | ⚠️ 需安装 | ⚠️ 需安装 |
| 黑体 | 一级标题 | ✅ 系统自带 | ⚠️ 华文黑体/STHeiti |
| 楷体_GB2312 | 二级标题 | ✅ 通常自带 | ⚠️ 回退为"楷体" |
| 仿宋_GB2312 | 正文/三级标题 | ✅ 通常自带 | ⚠️ 回退为"仿宋" |
| 宋体 | 页码 | ✅ 系统自带 | ⚠️ 回退为"宋体-简" |

## 2. 字体下载安装

### 方正小标宋简体

该字体非系统自带，需单独安装：

```bash
# 下载后安装方法：
# Windows：右键 → 安装（复制到 C:\Windows\Fonts\）
# Mac：双击 → 安装（复制到 ~/Library/Fonts/）
```

### 楷体_GB2312 / 仿宋_GB2312

- **Windows**：Win 7/10/11 通常内置
- **Mac**：无 `_GB2312` 后缀版本，系统自带"楷体""仿宋"
  - 字体名称分别为 "Kaiti SC" 和 "FangSong"

## 3. 跨平台字体映射表

```python
# set_font.py 中的映射逻辑

FONT_MAP = {
    # Windows → Mac 回退
    '仿宋_GB2312': '仿宋',
    '楷体_GB2312': '楷体',
}

# Mac 上黑体需特殊处理
# Windows: '黑体' → Mac: '华文黑体' 或 'STHeiti'
# Mac 上宋体: '宋体' → '宋体-简' 或 'STSong'
```

## 4. 字体缺失时的回退策略

| 情况 | 回退方案 |
|------|---------|
| 无方正小标宋简体 | 回退为"宋体"二号（效果不如小标宋，但可接受） |
| 无楷体_GB2312 | 使用"楷体"（Mac 默认行为） |
| 无仿宋_GB2312 | 使用"仿宋"（Mac 默认行为） |
| 无黑体（Mac） | 使用"华文黑体"或"STHeiti" |

## 5. 验证字体是否安装

```bash
# Windows（PowerShell）
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts' | Select-Object *方正*小标*

# Mac（使用 system_profiler 或 atsutil，fc-list 在 Mac 上不可用）
atsutil fonts -list | grep -i "小标"
atsutil fonts -list | grep -i "楷"
atsutil fonts -list | grep -i "仿宋"

# 或使用 system_profiler（输出更详细）
system_profiler SPFontsDataType | grep -E "小标|楷体|仿宋"
```
