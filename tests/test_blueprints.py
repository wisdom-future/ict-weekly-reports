"""
蓝图测试模块
"""
import pytest
import json
from pathlib import Path

def test_project_structure():
    """测试项目结构"""
    assert Path("config").exists()
    assert Path("scripts").exists()
    assert Path("utils").exists()
    assert Path("workflows/blueprints").exists()
    assert Path("data/sample").exists()

def test_sample_data():
    """测试示例数据"""
    sample_files = [
        "data/sample/competitor_sample.json",
        "data/sample/academic_sample.json",
        "data/sample/opensource_sample.json"
    ]
    
    for sample_file in sample_files:
        path = Path(sample_file)
        assert path.exists(), f"示例文件不存在: {sample_file}"
        
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, dict), f"{sample_file} 必须是JSON对象"
        assert len(data) > 0, f"{sample_file} 不能为空"

def test_imports():
    """测试Python模块导入"""
    try:
        import sys
        sys.path.append('.')
        
        from utils.logger import setup_logger
        from scripts.blueprint_manager import BlueprintManager
        
        # 测试日志设置
        logger = setup_logger("test")
        assert logger is not None
        
        # 测试蓝图管理器
        manager = BlueprintManager()
        workflows = manager.list_workflows()
        assert isinstance(workflows, dict)
        
    except ImportError as e:
        pytest.fail(f"模块导入失败: {e}")
