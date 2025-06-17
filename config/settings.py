"""
ICT TechInsight 配置设置
"""
import os
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# API配置
MAKE_API_BASE_URL = "https://us1.make.com/api/v2"
MAKE_API_KEY = os.getenv("MAKE_API_KEY", "")
MAKE_TEAM_ID = os.getenv("MAKE_TEAM_ID", "")

# 邮件配置
ALERT_EMAIL = os.getenv("ALERT_EMAIL", "")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# 数据目录
DATA_DIR = PROJECT_ROOT / "data"
BLUEPRINTS_DIR = PROJECT_ROOT / "workflows" / "blueprints"
LOGS_DIR = PROJECT_ROOT / "logs"

# 创建必要目录
LOGS_DIR.mkdir(exist_ok=True)
