
#!/bin/bash
# 在Docker容器内部运行CT质量评估

# 首先在容器内部创建Result目录并设置权限
docker run --rm -v $(pwd)/Result:/app/Result -w /app ct_quality_evaluator bash -c "
    echo '在Docker容器内部...'
    echo '当前目录:'
    pwd
    echo '目录内容:'
    ls -la
    echo '检查/app/Result目录:'
    ls -la /app/Result/
    echo '设置Result目录权限...'
    chmod -R 777 /app/Result
    echo '运行评估脚本...'
    python test_demo.py
"
