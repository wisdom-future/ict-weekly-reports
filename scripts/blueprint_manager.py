#!/usr/bin/env python3
"""
蓝图管理器
ICT TechInsight 自动化系统组件
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import argparse

class BlueprintManager:
    def __init__(self, base_path: str = "workflows/blueprints"):
        self.base_path = Path(base_path)
        
        # 工作流映射
        self.workflow_mapping = {
            "competitor": "competitor_intelligence",
            "academic": "academic_research", 
            "opensource": "opensource_ecosystem",
            "ai_analysis": "ai_analysis"
        }
    
    def organize_blueprints(self):
        """整理蓝图文件到相应目录"""
        print("开始整理蓝图文件...")
        
        blueprint_files = {
            "Competitor_Intelligence_Collection.blueprint.json": "competitor_intelligence",
            "Academic_Research_Collection.blueprint.json": "academic_research",
            "OpenSource_Ecosystem_Collection.blueprint.json": "opensource_ecosystem", 
            "ICT_TechInsight_MultiModel_AI_Analysis_v3.0.blueprint.json": "ai_analysis"
        }
        
        for filename, category in blueprint_files.items():
            source_path = Path(filename)
            if source_path.exists():
                target_dir = self.base_path / category
                target_dir.mkdir(parents=True, exist_ok=True)
                target_path = target_dir / filename
                
                shutil.copy2(source_path, target_path)
                print(f"已移动 {filename} 到 {target_path}")
            else:
                print(f"文件不存在: {filename}")
    
    def list_workflows(self) -> Dict:
        """列出所有工作流"""
        workflows = {}
        
        for category_dir in self.base_path.iterdir():
            if category_dir.is_dir():
                category_workflows = []
                for blueprint_file in category_dir.glob("*.json"):
                    category_workflows.append({
                        "file": blueprint_file.name,
                        "path": str(blueprint_file)
                    })
                workflows[category_dir.name] = category_workflows
        
        return workflows

def main():
    parser = argparse.ArgumentParser(description="ICT TechInsight Blueprint Manager")
    parser.add_argument("action", choices=["organize", "list"],
                       help="要执行的操作")
    
    args = parser.parse_args()
    
    manager = BlueprintManager()
    
    if args.action == "organize":
        manager.organize_blueprints()
    elif args.action == "list":
        workflows = manager.list_workflows()
        print(json.dumps(workflows, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
