#!/bin/bash
# 推送到 GitHub 的完整步骤
# 请在 gh auth login 完成后执行

# 1. 创建远程仓库（公开）
gh repo create eyawkmath/book --public --description "Everything You Always Wanted To Know About Mathematics — 中英双语对照阅读" --source=. --push

# 2. 设置 GitHub Pages（从 Actions 部署）
gh api repos/{owner}/eyawkmath/book/pages -X POST -f source.branch=main -f source.path=/ -f build_type=workflow

# 3. 验证
echo "✅ 推送完成！"
echo "📖 在线地址: https://eyawkmath.github.io/book/"
echo "⚙️ Actions: https://github.com/eyawkmath/book/actions"
