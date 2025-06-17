
```
ICT-TechInsight-Platform/
├── README.md                          # 项目主README文档
├── LICENSE                            # 开源许可证
├── .gitignore                         # Git忽略文件配置
├── CHANGELOG.md                       # 版本更新日志
├── CONTRIBUTING.md                    # 贡献指南
│
├── docs/                              # 📚 文档目录
│   ├── README.md
│   ├── architecture/                  # 架构文档
│   │   ├── system-architecture.md
│   │   ├── data-lake-design.md
│   │   └── api-specifications.md
│   ├── deployment/                    # 部署文档
│   │   ├── installation-guide.md
│   │   ├── configuration-guide.md
│   │   └── troubleshooting.md
│   ├── user-guides/                   # 用户指南
│   │   ├── dashboard-user-guide.md
│   │   ├── api-usage-guide.md
│   │   └── data-interpretation.md
│   └── development/                   # 开发文档
│       ├── coding-standards.md
│       ├── testing-guidelines.md
│       └── contribution-workflow.md
│
├── workflows/                         # 🔄 Make.com工作流配置
│   ├── README.md
│   ├── academic-research/             # 学术研究收集工作流
│   │   ├── academic-collection-workflow.json
│   │   ├── config.json
│   │   ├── data-mapping.json
│   │   └── README.md
│   ├── opensource-ecosystem/          # 开源生态收集工作流
│   │   ├── github-collection-workflow.json
│   │   ├── config.json
│   │   ├── data-mapping.json
│   │   └── README.md
│   ├── patent-intelligence/           # 专利情报收集工作流
│   │   ├── patent-collection-workflow.json
│   │   ├── config.json
│   │   ├── data-mapping.json
│   │   └── README.md
│   ├── news-intelligence/             # 新闻情报收集工作流
│   │   ├── news-collection-workflow.json
│   │   ├── config.json
│   │   ├── data-mapping.json
│   │   └── README.md
│   ├── competitor-intelligence/       # 竞争对手情报工作流
│   │   ├── competitor-collection-workflow.json
│   │   ├── config.json
│   │   ├── data-mapping.json
│   │   └── README.md
│   ├── ai-analysis/                   # AI分析工作流
│   │   ├── multi-model-analysis-workflow.json
│   │   ├── ai-config.json
│   │   ├── prompt-templates.json
│   │   └── README.md
│   └── common/                        # 公共组件
│       ├── error-handlers.json
│       ├── data-validators.json
│       ├── notification-templates.json
│       └── utility-functions.json
│
├── data-schemas/                      # 📋 数据模式定义
│   ├── README.md
│   ├── raw-data/                      # 原始数据模式
│   │   ├── academic-papers-schema.json
│   │   ├── github-projects-schema.json
│   │   ├── patent-data-schema.json
│   │   ├── news-data-schema.json
│   │   └── competitor-data-schema.json
│   ├── standardized-data/             # 标准化数据模式
│   │   ├── technology-registry-schema.json
│   │   ├── standardized-academic-schema.json
│   │   ├── standardized-github-schema.json
│   │   ├── standardized-patent-schema.json
│   │   └── standardized-news-schema.json
│   ├── analytics-results/             # 分析结果模式
│   │   ├── technology-assessment-schema.json
│   │   ├── ai-analysis-details-schema.json
│   │   ├── investment-recommendations-schema.json
│   │   └── risk-assessment-schema.json
│   └── master-data/                   # 主数据模式
│       ├── technology-master-schema.json
│       ├── competitor-master-schema.json
│       ├── data-dictionary-schema.json
│       └── business-rules-schema.json
│
├── scripts/                           # 🛠️ 脚本和工具
│   ├── README.md
│   ├── data-migration/                # 数据迁移脚本
│   │   ├── migrate-to-bigquery.py
│   │   ├── data-export-tools.py
│   │   ├── backup-scripts.sh
│   │   └── README.md
│   ├── data-validation/               # 数据验证脚本
│   │   ├── quality-checker.py
│   │   ├── schema-validator.py
│   │   ├── data-profiler.py
│   │   └── README.md
│   ├── monitoring/                    # 监控脚本
│   │   ├── health-check.py
│   │   ├── performance-monitor.py
│   │   ├── alert-manager.py
│   │   └── README.md
│   ├── utilities/                     # 工具脚本
│   │   ├── config-generator.py
│   │   ├── data-anonymizer.py
│   │   ├── api-tester.py
│   │   └── README.md
│   └── deployment/                    # 部署脚本
│       ├── setup-environment.sh
│       ├── deploy-workflows.py
│       ├── configure-apis.py
│       └── README.md
│
├── configs/                           # ⚙️ 配置文件
│   ├── README.md
│   ├── environments/                  # 环境配置
│   │   ├── development.json
│   │   ├── staging.json
│   │   ├── production.json
│   │   └── README.md
│   ├── apis/                          # API配置
│   │   ├── crossref-api-config.json
│   │   ├── github-api-config.json
│   │   ├── serpapi-config.json
│   │   ├── news-api-config.json
│   │   ├── xai-api-config.json
│   │   ├── openai-api-config.json
│   │   └── README.md
│   ├── data-sources/                  # 数据源配置
│   │   ├── technology-topics.json
│   │   ├── competitor-list.json
│   │   ├── data-quality-rules.json
│   │   └── README.md
│   ├── ai-models/                     # AI模型配置
│   │   ├── grok-model-config.json
│   │   ├── gpt4-model-config.json
│   │   ├── risk-model-config.json
│   │   ├── prompt-templates/
│   │   │   ├── technical-analysis-prompts.json
│   │   │   ├── market-analysis-prompts.json
│   │   │   └── risk-assessment-prompts.json
│   │   └── README.md
│   ├── dashboards/                    # 仪表板配置
│   │   ├── looker-studio-config.json
│   │   ├── dashboard-layouts.json
│   │   ├── chart-configurations.json
│   │   └── README.md
│   ├── monitoring/                    # 监控配置
│   │   ├── alert-rules.json
│   │   ├── notification-config.json
│   │   ├── performance-thresholds.json
│   │   └── README.md
│   └── security/                      # 安全配置
│       ├── access-policies.json
│       ├── encryption-config.json
│       ├── audit-rules.json
│       └── README.md
│
├── templates/                         # 📄 模板文件
│   ├── README.md
│   ├── workflow-templates/            # 工作流模板
│   │   ├── data-collection-template.json
│   │   ├── ai-analysis-template.json
│   │   ├── notification-template.json
│   │   └── README.md
│   ├── report-templates/              # 报告模板
│   │   ├── daily-report-template.html
│   │   ├── weekly-analysis-template.html
│   │   ├── monthly-summary-template.html
│   │   ├── email-notification-template.html
│   │   └── README.md
│   ├── dashboard-templates/           # 仪表板模板
│   │   ├── technology-overview-template.json
│   │   ├── ai-analysis-monitor-template.json
│   │   ├── competitive-intelligence-template.json
│   │   └── README.md
│   └── api-templates/                 # API模板
│       ├── rest-api-template.json
│       ├── webhook-template.json
│       ├── response-template.json
│       └── README.md
│
├── tests/                             # 🧪 测试文件
│   ├── README.md
│   ├── unit-tests/                    # 单元测试
│   │   ├── data-validation-tests.py
│   │   ├── schema-validation-tests.py
│   │   ├── api-integration-tests.py
│   │   └── README.md
│   ├── integration-tests/             # 集成测试
│   │   ├── workflow-integration-tests.py
│   │   ├── ai-analysis-tests.py
│   │   ├── dashboard-tests.py
│   │   └── README.md
│   ├── performance-tests/             # 性能测试
│   │   ├── load-testing.py
│   │   ├── stress-testing.py
│   │   ├── benchmark-tests.py
│   │   └── README.md
│   ├── security-tests/                # 安全测试
│   │   ├── vulnerability-tests.py
│   │   ├── penetration-tests.py
│   │   ├── compliance-tests.py
│   │   └── README.md
│   └── test-data/                     # 测试数据
│       ├── sample-academic-data.json
│       ├── sample-github-data.json
│       ├── sample-patent-data.json
│       ├── sample-news-data.json
│       └── README.md
│
├── tools/                             # 🔧 开发工具
│   ├── README.md
│   ├── data-generators/               # 数据生成器
│   │   ├── mock-data-generator.py
│   │   ├── test-data-creator.py
│   │   ├── schema-generator.py
│   │   └── README.md
│   ├── validators/                    # 验证工具
│   │   ├── json-schema-validator.py
│   │   ├── workflow-validator.py
│   │   ├── config-validator.py
│   │   └── README.md
│   ├── converters/                    # 转换工具
│   │   ├── csv-to-json-converter.py
│   │   ├── schema-converter.py
│   │   ├── format-converter.py
│   │   └── README.md
│   └── analytics/                     # 分析工具
│       ├── data-profiler.py
│       ├── performance-analyzer.py
│       ├── usage-statistics.py
│       └── README.md
│
├── samples/                           # 📝 示例文件
│   ├── README.md
│   ├── workflow-samples/              # 工作流示例
│   │   ├── simple-data-collection.json
│   │   ├── ai-analysis-example.json
│   │   └── README.md
│   ├── api-samples/                   # API调用示例
│   │   ├── crossref-api-example.py
│   │   ├── github-api-example.py
│   │   ├── ai-api-example.py
│   │   └── README.md
│   ├── data-samples/                  # 数据示例
│   │   ├── technology-assessment-sample.json
│   │   ├── ai-analysis-sample.json
│   │   ├── competitor-intelligence-sample.json
│   │   └── README.md
│   └── dashboard-samples/             # 仪表板示例
│       ├── basic-dashboard-config.json
│       ├── advanced-analytics-config.json
│       └── README.md
│
├── migrations/                        # 🔄 数据迁移
│   ├── README.md
│   ├── version-1.0/                   # 版本1.0迁移
│   │   ├── init-database.sql
│   │   ├── create-tables.sql
│   │   └── README.md
│   ├── version-2.0/                   # 版本2.0迁移
│   │   ├── add-ai-analysis-tables.sql
│   │   ├── update-schemas.sql
│   │   └── README.md
│   └── version-3.0/                   # 版本3.0迁移
│       ├── multi-model-ai-upgrade.sql
│       ├── performance-optimization.sql
│       └── README.md
│
├── monitoring/                        # 📊 监控配置
│   ├── README.md
│   ├── grafana/                       # Grafana配置
│   │   ├── dashboards/
│   │   │   ├── system-overview.json
│   │   │   ├── ai-performance.json
│   │   │   └── data-quality.json
│   │   ├── alerts/
│   │   │   ├── system-alerts.json
│   │   │   └── business-alerts.json
│   │   └── README.md
│   ├── prometheus/                    # Prometheus配置
│   │   ├── prometheus.yml
│   │   ├── alert-rules.yml
│   │   └── README.md
│   └── logs/                          # 日志配置
│       ├── log-config.json
│       ├── log-rotation.conf
│       └── README.md
│
├── security/                          # 🔒 安全配置
│   ├── README.md
│   ├── policies/                      # 安全策略
│   │   ├── access-control-policy.json
│   │   ├── data-protection-policy.json
│   │   ├── api-security-policy.json
│   │   └── README.md
│   ├── certificates/                  # 证书管理
│   │   ├── cert-config.json
│   │   ├── ssl-config.json
│   │   └── README.md
│   └── audit/                         # 审计配置
│       ├── audit-rules.json
│       ├── compliance-checklist.json
│       └── README.md
│
└── .github/                           # 🐙 GitHub配置
    ├── workflows/                     # GitHub Actions
    │   ├── ci-cd.yml
    │   ├── testing.yml
    │   ├── security-scan.yml
    │   └── deployment.yml
    ├── ISSUE_TEMPLATE/               # Issue模板
    │   ├── bug_report.md
    │   ├── feature_request.md
    │   └── question.md
    ├── PULL_REQUEST_TEMPLATE.md      # PR模板
    └── dependabot.yml                # 依赖更新配置
```

## 🔍 重要JSON文件归档说明

### **1. 工作流配置JSON**
```yaml
workflows/academic-research/academic-collection-workflow.json:
  # Make.com学术研究收集工作流的完整JSON配置
  # 包含所有步骤、条件、错误处理逻辑

workflows/ai-analysis/multi-model-analysis-workflow.json:
  # AI多模型分析工作流配置
  # 包含xAI Grok-3、OpenAI GPT-4的调用配置
```

### **2. 数据模式JSON**
```yaml
data-schemas/analytics-results/technology-assessment-schema.json:
  # 技术评估结果的JSON Schema
  # 定义overall_score、final_recommendation等字段

data-schemas/master-data/technology-registry-schema.json:
  # 技术主题注册表的数据模式
  # 包含13个核心技术主题的结构定义
```

### **3. 配置管理JSON**
```yaml
configs/ai-models/prompt-templates/technical-analysis-prompts.json:
  # AI技术分析的Prompt模板
  # 包含xAI Grok-3的专业提示词

configs/data-sources/technology-topics.json:
  # 当前监控的13个技术主题配置
  # 包含优先级、关键词、分类等信息
```

### **4. 仪表板配置JSON**
```yaml
configs/dashboards/looker-studio-config.json:
  # Looker Studio仪表板的配置
  # 包含数据源连接、图表配置等

templates/dashboard-templates/technology-overview-template.json:
  # 技术洞察总览仪表板模板
  # 可复用的仪表板配置模板
```

## 📋 使用指南

### **快速开始**
```bash
# 克隆仓库
git clone https://github.com/your-org/ICT-TechInsight-Platform.git

# 进入目录
cd ICT-TechInsight-Platform

# 查看主要配置
cat configs/environments/production.json

# 部署工作流
python scripts/deployment/deploy-workflows.py
```

### **主要特性**
- 🎯 **清晰分层**：按功能模块明确分层组织
- 📚 **完整文档**：每个目录都有详细的README
- 🔧 **开发友好**：丰富的工具和脚本支持
- 🧪 **测试完备**：全面的测试覆盖
- 🔒 **安全保障**：完整的安全配置管理
- 📊 **监控就绪**：内置监控和告警配置

这个目录结构遵循了软件工程最佳实践，便于团队协作开发、版本控制管理和系统维护。所有关键的JSON配置都有明确的归档位置，支持环境管理、版本控制和自动化部署。
