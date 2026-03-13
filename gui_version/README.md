# 數獨游戏 (Sudoku Game)

一个使用 Python Tkinter 开发的经典數獨游戏，支持三种难度級別（简单、中等、困难），具有完整的數獨生成和求解邏輯。

![游戲截图](sudoku_ui.png)

## 功能特性

-  图形化界面，基于 Tkinter 原生库，无需额外安装
-  自动生成具有唯一解的完整數獨棋盘
- 三种难度級別：简单（挖30-35洞）、中等（挖40-45 洞）、困难（挖50-55 洞）
-  实时输入验证（仅允许 1-9 数字）
-  一键檢查答案，錯誤格子高亮顯示
- 💡提示功能，自動填入正確數字
-    重置謎題，恢復初始狀態

## 环境要求

- Python 3.6 或更高版本
- Tkinter（Python 标准库，通常随 Python 一起安装，無需另外安裝）

## 安装与运行

1. **克隆仓库**
   ```bash
   git clone https://github.com/caihongni/sudoku_game.git

2. **運行游戲**
   cd gui_version
   python main.py
