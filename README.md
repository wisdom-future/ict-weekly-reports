# ICT TechInsight 自动化系统

基于Make.com的ICT技术洞察自动化数据收集和分析系统。

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/your-username/ICT-TechInsight-Automation.git
cd ICT-TechInsight-Automation
```

### 2. 设置Python环境
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境 (Windows)
venv\Scripts\activate

# 激活虚拟环境 (Linux/Mac)
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3. 配置API密钥
```bash
# 复制配置文件
cp config/api_keys.example.env .env

# 编辑配置文件
# 填入您的 Make.com API 密钥和其他必要配置
```

### 4. 上传蓝图文件
将您的Make.com蓝图文件上传到对应目录：
- `workflows/blueprints/competitor_intelligence/`
- `workflows/blueprints/academic_research/`
- `workflows/blueprints/opensource_ecosystem/`
- `workflows/blueprints/ai_analysis/`

### 5. 运行测试
```bash
pytest tests/
```

## 📁 项目结构

```
ICT-TechInsight-Automation/
├── README.md
├── requirements.txt
├── .gitignore
├── config/                 # 配置文件
│   ├── settings.py
│   └── api_keys.example.env
├── workflows/              # Make.com工作流
│   ├── blueprints/        # 蓝图文件
│   │   ├── competitor_intelligence/
│   │   ├── academic_research/
│   │   ├── opensource_ecosystem/
│   │   └── ai_analysis/
│   ├── docs/              # 工作流文档
│   └── schemas/           # 数据架构
├── scripts/               # 管理脚本
│   └── blueprint_manager.py
├── utils/                 # 工具模块
│   └── logger.py
├── tests/                 # 测试文件
│   └── test_blueprints.py
├── data/                  # 数据文件
│   └── sample/           # 示例数据
└── deployment/            # 部署配置
```

## 🛠️ 工具使用

### 蓝图管理
```bash
python scripts/blueprint_manager.py organize
python scripts/blueprint_manager.py list
```

## 📊 核心功能

- 🔍 **竞争对手情报收集** - 自动监控竞争对手动态
- 📚 **学术研究收集** - 收集和分析学术论文
- 🌟 **开源生态监控** - 跟踪开源项目和技术趋势
- 🤖 **多模型AI分析** - 智能分析和决策支持

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
